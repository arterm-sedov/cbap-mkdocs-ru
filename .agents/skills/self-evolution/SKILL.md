---
name: self-evolution
description: Use when you've completed a non-trivial task and need to document discoveries, patterns, or gotchas for future sessions. Also use to review the discovery log before starting similar work.
---

# Self-Evolution — Documenting Discoveries

After completing a non-trivial task, review what was learned and capture it so it benefits future sessions.

## When To Document

- A pattern that took debugging to figure out (e.g., silent macro errors, missing anchor warnings).
- A workflow step not covered by existing skills (e.g., which PHPKB category ID to use, which script signature fits which context).
- A recurring gotcha that cost time and would cost again.

## Where To Document

| Finding type | Destination |
|---|---|
| **Process/skill gap** | Update the matching skill under `.agents/skills/<name>/SKILL.md` |
| **Recurring authoring pitfall** | Add a concise rule to `AGENTS.md` under the relevant heading |
| **One-off context note** (category IDs, naming conventions) | Add to the relevant skill's `references/` folder |
| **Session discovery** (more than a one-off, not yet migrated) | Add to `references/discovery_log.md` (alongside this skill) |

## How

1. State the symptom and the fix in 1–2 lines.
2. Add it to the most specific skill or rule file — prefer updating existing docs over creating new ones.
3. Keep it agnostic: no absolute paths, no secrets, no machine-specific notes.
4. Add to [references/discovery_log.md](references/discovery_log.md) under a `## YYYY-MM-DD` heading — **newest dates at the top** of the file (prepend a new date block immediately after the intro; add bullets under an existing today heading if one is already there). One date heading per day — merge into the existing block, do not duplicate the date.

**Why newest-first:** agents and partial reads see recent gotchas first; that matches “review before starting.” Git merge conflicts at the top are acceptable — this file cherry-picks safely between platform branches.

## Review Before Starting

When starting a non-trivial task, read **from the top** of `references/discovery_log.md` — recent entries are first. Scan date headings and bullets relevant to the work at hand. Many gotchas are domain-specific and won't surface in generic search.

## Periodic Cleanup

Move entries from `references/discovery_log.md` into durable skill/rule files when they've proven useful across multiple sessions.

### Pruning the discovery log (operator approval required)

**Never prune the log on your own.** After a non-trivial task — or when the log feels long or stale — analyze what can leave the log, **present suggestions to the operator**, and apply removals **only if they approve**.

**How to build suggestions (delta analysis):**

1. Read `references/discovery_log.md` (newest-first).
2. For each bullet (or date block), check whether the same fact already lives in durable docs:
   - `AGENTS.md` (rules, cherry-pick, link formatting, …)
   - `readme.md` / `readme-ru.md` (operator workflows)
   - `.agents/skills/<name>/SKILL.md` and skill `references/`
   - Codebase reality (scripts, YAML, comments) — log entry may be **stale** if the repo changed
3. Classify each item:
   - **Migrate** — still valuable but belongs in a skill/rule/readme; propose target file and a one-line rule to add there
   - **Prune from log** — fully absorbed or redundant; safe to delete from the log once durable home exists
   - **Keep in log** — operational detail, not yet documented elsewhere, or still the best agent entry point
   - **Fix** — outdated or wrong; propose corrected wording (do not delete without operator OK)

**Present to the operator** as a short table or list: log bullet → status → proposed action → where content lives (or will live). Example:

| Log entry (date + gist) | Status | Proposed action |
| --- | --- | --- |
| 2026-06-18 · empty cherry-pick | Prune | Delete — covered in `AGENTS.md` → Cherry-picking |

**Ask explicitly:** “Apply these pruning/migration changes?” Wait for yes/no. If no, leave the log unchanged. If yes, edit only what was approved (log, and any agreed skill/`AGENTS.md` updates).

**Do not** bulk-delete cherry-pick or workflow bullets without this check — operators may want log reminders even when `AGENTS.md` also documents the rule.

### When `AGENTS.md` or the log accumulates recipes (operator approval required)

During delta analysis, watch for **bloat**: multi-step workflows, repeated command blocks, or domain-specific “recipes” piling up in `AGENTS.md` or `discovery_log.md`. `AGENTS.md` should stay **rules and pointers**; long playbooks belong in **skills** (see `AGENTS.md` → Skills Reference).

If you see a cluster of related entries (e.g. SSH tunnel + keyring + MySQL, or a repeated publish sub-flow), you may **recommend a new skill** — name, one-line `description`, and what would move out of the log or `AGENTS.md` into `.agents/skills/<name>/SKILL.md`.

**Always talk to the operator first.** They know ownership, naming, and whether a topic deserves its own skill vs extending an existing one. Present the recommendation; do **not** create skills, split `AGENTS.md`, or prune until they agree.

Typical prompt: “These N log/`AGENTS.md` items look like a `<name>` skill — want me to draft `SKILL.md` and migrate them?”

## Sync across branches (remind the operator)

After documenting discoveries or cleaning up skills/rules/readmes, **mention branch sync** — do not cherry-pick or push across branches unless the operator asks.

These paths are **version-agnostic** and usually safe to sync **both ways** between `platform_v5`, `platform_v6`, `master`, or other branches the operator uses (see `AGENTS.md` → Cherry-picking; `readme.md` / `readme-ru.md` → Merge and cherry-pick):

- `.agents/skills/**` (including `self-evolution` and `discovery_log.md`)
- `AGENTS.md`
- `readme.md`, `readme-ru.md`

**Do not assume sync is wanted.** Operators may:

- **Want to sync** — cherry-pick doc-only commits to other platform branches so all teams share rules, skills, and operator guides.
- **Want to defer or skip** — keep branch-specific workflow docs until a release, avoid merge noise, or sync manually later.

**Remind periodically** (e.g. after a substantial self-evolution pass): “These changes are on `<branch>`. Cherry-pick to `platform_v5` / `platform_v6` / `master`, or leave as-is?” Wait for their choice — they know which branches they maintain and when cross-branch alignment matters.

**Never sync version-specific artifacts** in the same breath without explicit approval — `docs/ru/` kbIds, `for_kb_import_ru/`, `phpkb_content*`, LLM bundles follow different cherry-pick rules (`AGENTS.md` → Cherry-picking).
