#!/bin/bash

# Reindex an existing index to apply a new mapping on a local OpenSearch cluster.
# This variant supports a platform prefix option that constructs the pattern as
# cmw_<prefix> (discovery adds *), and always deletes any existing _v2 indices
# if they already exist.
#
# Flow:
#  1) Create ${index}_v2 with required mapping
#  2) Reindex from ${index} -> ${index}_v2
#  3) Delete ${index}
#  4) Create ${index} with required mapping
#  5) Reindex from ${index}_v2 -> ${index}
#  6) Delete ${index}_v2

set -euo pipefail

# ------------------------------------------------------------
# Args and configuration (can be overridden via env vars)
# Examples:
#   bash reindex_local_prefix.sh -p support                       # => pattern: cmw_support
#   bash reindex_local_prefix.sh -ip 10.0.0.5:9200 -m custom.json -p support
#

# CLI defaults
prefixArg=""
opensearchServ="localhost:9200"
mapFile="m1.json"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -p|--prefix)
      if [[ $# -lt 2 ]]; then
        echo "--prefix requires a value" >&2
        exit 1
      fi
      prefixArg="$2"
      shift 2
      ;;
    -ip|--journal_srv_ip)
      if [[ $# -lt 2 ]]; then
        echo "--journal_srv_ip requires a value (host:port)" >&2
        exit 1
      fi
      opensearchServ="$2"
      shift 2
      ;;
    -m|--map-file)
      if [[ $# -lt 2 ]]; then
        echo "--map-file requires a value (path to JSON)" >&2
        exit 1
      fi
      mapFile="$2"
      shift 2
      ;;
    -h|--help)
      cat <<USAGE
Usage: $0 -p <prefix> [-ip host:port] [-m file]
  -p,  --prefix <name>                Target indices cmw_<name>* (required)
  -ip, --journal_srv_ip <host:port>   OpenSearch host:port (default: localhost:9200)
  -m,  --map-file <file>              Mapping JSON (default: m1.json)
USAGE
      exit 0
      ;;
    --)
      shift
      break
      ;;
    *)
      # Ignore unknown args to remain compatible with env-var driven usage
      shift
      ;;
  esac
done

# Determine index pattern: require prefix
if [[ -z "${prefixArg}" ]]; then
  echo "--prefix is required (platform prefix)" >&2
  exit 1
fi
indexPattern="cmw_${prefixArg}"

# opensearchServ and mapFile set by CLI with defaults above

# Ensure jq is available when reading external mapping
require_jq() {
  if command -v jq >/dev/null 2>&1; then return; fi
  echo "[info] jq not found. Attempting to install..."
  if command -v apt-get >/dev/null 2>&1; then
    sudo apt-get update && sudo apt-get install -y jq
  elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y jq
  else
    echo "[error] jq not found and no supported package manager (apt-get/dnf) found." >&2
    exit 1
  fi
}

# Load and normalize mapping JSON (accept either full index body or just mappings)
load_mapping_body() {
  if [[ ! -f "${mapFile}" ]]; then
    echo "[error] Mapping file '${mapFile}' not found" >&2
    exit 1
  fi
  require_jq
  local raw
  raw=$(cat "${mapFile}")
  # Validate JSON
  echo "${raw}" | jq . >/dev/null 2>&1 || { echo "[error] Mapping JSON in '${mapFile}' is invalid." >&2; exit 1; }
  # If top-level has "mappings", use as-is; otherwise wrap into {"mappings": ...}
  if echo "${raw}" | jq -e 'has("mappings")' >/dev/null 2>&1; then
    mappingBody="${raw}"
  else
    mappingBody=$(jq -cn --argjson m "${raw}" '{mappings: $m}')
  fi
}

exists_index() {
  local idx="$1"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://${opensearchServ}/${idx}")
  if [[ "$code" == "200" ]]; then
    return 0
  else
    return 1
  fi
}

create_with_mapping() {
  local idx="$1"
  echo "[info] Creating index ${idx} with mapping from '${mapFile}'"
  curl -fsS -X PUT "http://${opensearchServ}/${idx}" -H 'Content-Type: application/json' -d "${mappingBody}" | cat
}

reindex() {
  local src="$1"
  local dst="$2"
  echo "[info] Reindexing ${src} -> ${dst} (wait_for_completion=true)"
  curl -fsS -X POST "http://${opensearchServ}/_reindex?wait_for_completion=true" -H 'Content-Type: application/json' -d @- <<EOF | cat
{
  "source": { "index": "${src}" },
  "dest":   { "index": "${dst}" }
}
EOF
}

delete_index() {
  local idx="$1"
  echo "[info] Deleting index ${idx}"
  curl -fsS -X DELETE "http://${opensearchServ}/${idx}" | cat
}

refresh_index() {
  local idx="$1"
  echo "[info] Refreshing index ${idx}"
  curl -fsS -X POST "http://${opensearchServ}/${idx}/_refresh" | cat
}

count_index() {
  local idx="$1"
  curl -fsS "http://${opensearchServ}/${idx}/_count" | sed -n 's/.*"count"\s*:\s*\([0-9][0-9]*\).*/\1/p'
}

alias_exists() {
  local al="$1"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://${opensearchServ}/_alias/${al}")
  [[ "$code" == "200" ]]
}

remove_alias_glob() {
  local al="$1"
  echo "[info] Removing alias '${al}' from all indices if present"
  curl -fsS -X POST "http://${opensearchServ}/_aliases" -H 'Content-Type: application/json' -d @- <<EOF | cat
{
  "actions": [ { "remove": { "index": "*", "alias": "${al}" } } ]
}
EOF
}

# ---- Start ----

# Resolve pattern path for _cat (append * only if no wildcard present)
if [[ "${indexPattern}" == *"*"* ]]; then
  pathPattern="${indexPattern}"
else
  pathPattern="${indexPattern}*"
fi

# Discover indices by pattern
indexList=$(curl -s "http://${opensearchServ}/_cat/indices/${pathPattern}?h=index" | awk 'NF')

if [[ -z "${indexList}" ]]; then
  echo "[warn] No indices found matching pattern '${indexPattern}' on ${opensearchServ}. Nothing to do."
  exit 0
fi

# Load mapping once
load_mapping_body

for indexName in ${indexList}; do
  echo "[info] Processing index: ${indexName}"
  # Skip temp indices
  if [[ "${indexName}" == *_v2 ]]; then
    echo "[info] Skipping index '${indexName}' because it ends with _v2"
    continue
  fi
  if ! exists_index "${indexName}"; then
    echo "[warn] Skipping ${indexName}: not found"
    continue
  fi

  v2Index="${indexName}_v2"

  # Always delete existing _v2 index if present
  if exists_index "${v2Index}"; then
    delete_index "${v2Index}"
  fi

  # 1) Create v2 index with mapping
  create_with_mapping "${v2Index}"

  # 2) Reindex from original -> v2
  reindex "${indexName}" "${v2Index}"
  refresh_index "${v2Index}"
  src_count=$(count_index "${v2Index}")
  echo "[info] ${v2Index} count after step 2: ${src_count}"

  # 3) Delete original
  delete_index "${indexName}"

  # 4) Recreate original with mapping
  if alias_exists "${indexName}"; then
    echo "[info] Alias named '${indexName}' exists. Removing it before creating index."
    remove_alias_glob "${indexName}"
  fi
  create_with_mapping "${indexName}"

  # 5) Reindex back v2 -> original
  reindex "${v2Index}" "${indexName}"
  refresh_index "${indexName}"
  dst_count=$(count_index "${indexName}")
  echo "[info] ${indexName} count after step 5: ${dst_count}"

  # 6) Delete v2 only if counts match
  if [[ "${src_count}" == "${dst_count}" ]]; then
    delete_index "${v2Index}"
  else
    echo "[warn] Counts differ (v2=${src_count}, dst=${dst_count}). Keeping ${v2Index} for inspection."
  fi

  echo "[done] Reindex flow completed for ${indexName} on ${opensearchServ}"
done


