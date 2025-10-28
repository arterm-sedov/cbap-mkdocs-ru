<!-- 79df14cf-6fa1-4eaa-83ff-d250b56e4c3e 205a0b8d-ad59-481c-9bfb-6bb7c1f909c4 -->
# MkDocs RAG Engine Implementation Plan

## Overview

Build a production-ready RAG (Retrieval-Augmented Generation) engine for the MkDocs documentation repository that handles Jinja2-rich source files through MkDocs build pipeline integration. Uses FRIDA (best Russian embedder), ChromaDB vector store, a Russian-capable cross-encoder reranker, and multi-LLM support with streaming responses. MVP is Gradio-first; FastAPI + FastMCP is a deprioritized future migration.

## Project Rationale & Design Decisions

- ChromaDB over Supabase for purpose-built vector search, rich metadata, persistence, local deployment.
- Metadata-enriched chunks enable article reconstruction, better reranking, and precise citations.
- Reuse ~40% from existing repos; focus new code on MkDocs hook, 3-mode ingestion, FRIDA, reranker, Gradio MVP.

## References

- https://github.com/arterm-sedov/cmw-platform-agent
- https://github.com/arterm-sedov/agent-course-final-assignment
- https://github.com/AsyncFuncAI/deepwiki-open
- https://habr.com/ru/articles/955798/
- https://github.com/CodeCutTech/Data-science/blob/master/machine_learning/open_source_rag_pipeline_intelligent_qa_system.ipynb
- https://huggingface.co/ai-forever/FRIDA
- https://www.gradio.app/docs/gradio/api
- https://www.gradio.app/guides/building-mcp-server-with-gradio
- https://www.gradio.app/docs/gradio/mount_gradio_app
- https://www.gradio.app/guides/creating-a-chatbot-fast
- https://www.gradio.app/docs/gradio/chatinterface

## Architecture

```
Input Sources (3 modes):
  1. MkDocs Pipeline → Build Hook → Compiled MD
  2. Compiled KB File → kb.comindware.ru.platform_v5_for_llm_ingestion.md
  3. Compiled MD Folder → phpkb_content/798.../
                    ↓
         Document Processor (handles all 3 modes)
                    ↓
         Smart Chunker (700 tokens, 300 overlap)
                    ↓
         Metadata Enricher (rich metadata)
                    ↓
         FRIDA Embedder (prefixes)
                    ↓
         ChromaDB Vector Store (persistent)
                    ↓
         Query Pipeline → Embed query → Vector search (top-20)
                        → Cross-encoder reranking (top-5)
                        → Article reconstruction → LLM generation
                        → Streaming + citations
```

## Phase 1: MkDocs Integration & Project Setup

### 1.0 MkDocs Build Pipeline Integration (YAML + Hook)

Problem: Raw MkDocs files contain Jinja2 syntax; must index compiled MD.

File: `mkdocs_for_rag_indexing.yml`

```yaml
# Inherit from complete guide to resolve all Jinja2 variables
INHERIT: mkdocs_guide_complete_ru.yml

# Override output directory
site_dir: compiled_md_for_rag

# Add custom hook
hooks:
  - rag_indexing_hook.py

# Disable unnecessary plugins
plugins:
  - search: false
  - with-pdf: !ENV [DISABLE_PDF, true]
```

File: `rag_indexing_hook.py`

```python
"""
MkDocs hook to export Jinja2-compiled markdown for RAG indexing.
Similar to kb_html_cleanup_hook.py but outputs compiled MD files.
"""
import json
from datetime import datetime
from pathlib import Path
import yaml


def on_page_markdown(markdown, page, config, files):
    """Called AFTER Jinja2 processing, BEFORE HTML conversion."""
    page._compiled_md_for_rag = markdown
    return markdown


def on_post_page(output, page, config):
    """Save compiled markdown to RAG folder."""
    compiled_md = getattr(page, '_compiled_md_for_rag', page.markdown)
    output_dir = Path(config['site_dir'])
    rel_path = Path(page.file.src_path)
    output_file = output_dir / rel_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        if page.meta:
            f.write('---\n')
            yaml.dump(page.meta, f, allow_unicode=True, default_flow_style=False)
            f.write('---\n\n')
        f.write(compiled_md)
    return output


def on_post_build(config):
    """Create manifest for RAG indexer."""
    output_dir = Path(config['site_dir'])
    md_files = sorted(output_dir.rglob('*.md'))
    manifest = {
        'total_files': len(md_files),
        'files': [str(f.relative_to(output_dir)) for f in md_files],
        'build_date': datetime.now().isoformat(),
        'config_name': config.get('site_name'),
        'source_type': 'mkdocs_pipeline'
    }
    with open(output_dir / 'rag_manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"✅ RAG Export: {len(md_files)} compiled MD files → {output_dir}")
```

Usage:

```bash
mkdocs build -f mkdocs_for_rag_indexing.yml
# Output: compiled_md_for_rag/ with Jinja2-resolved files
```

External MkDocs project support (lean):

- The RAG engine can live outside the MkDocs repo. Use a helper script to run the export inside the MkDocs project directory without modifying the project permanently.
- The script copies the hook and generates a temporary YAML under `.rag_export/` in the MkDocs repo, runs the build, and writes compiled MD to a specified output directory.
- Default output directory is inside the RAG agent repo for easier ingestion, e.g. `rag_engine/data/compiled_md_for_rag/` (configurable).

Helper script (planned): `scripts/run_mkdocs_export.py`

```bash
python rag_engine/scripts/run_mkdocs_export.py \
  --project-dir ../CBAP_MKDOCS_RU \
  --inherit-config mkdocs_guide_complete_ru.yml \
  --output-dir ../rag_engine/data/compiled_md_for_rag
```

Behavior:
- Creates `<project-dir>/.rag_export/`
- Copies `rag_engine/rag_indexing_hook.py` → `.rag_export/rag_indexing_hook.py`
- Writes `.rag_export/mkdocs_for_rag_indexing.yml` with:
  - `INHERIT: <inherit-config>` (resolved within the MkDocs repo)
  - `hooks: [ .rag_export/rag_indexing_hook.py ]`
  - `site_dir: <output-dir>` (absolute or relative; absolute recommended to place output in the RAG agent repo)
- Runs from `--project-dir`:
  - `mkdocs build -f .rag_export/mkdocs_for_rag_indexing.yml`

Notes:
- Works on Windows/macOS/Linux; uses absolute paths where necessary; avoids touching real project files.

### 1.1 Project Structure

```
rag_engine/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── input_modes.py
├── core/
│   ├── __init__.py
│   ├── document_processor.py
│   ├── chunker.py
│   └── metadata_enricher.py
├── retrieval/
│   ├── __init__.py
│   ├── embedder.py
│   ├── vector_search.py
│   ├── retriever.py
│   └── reranker.py
├── storage/
│   ├── __init__.py
│   └── vector_store.py
├── llm/
│   ├── __init__.py
│   ├── llm_manager.py
│   ├── provider_adapters.py
│   ├── langsmith_config.py
│   └── langfuse_config.py
├── observability/
│   ├── __init__.py
│   ├── langfuse_manager.py
│   └── langsmith_manager.py
├── api/
│   ├── __init__.py
│   ├── app.py       # Gradio MVP
│   └── models.py
├── utils/
│   ├── __init__.py
│   ├── logging_manager.py
│   ├── logger.py
│   ├── formatters.py
│   └── file_utils.py   # MD ingestion helpers (no PDF ingestion)
├── scripts/
│   ├── build_index.py
│   └── test_queries.py
├── data/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

### 1.2 Configuration (Complete)

`config/settings.py`

```python
INDEXING_CONFIG = {
    "input_modes": {
        "mkdocs_pipeline": {
            "enabled": True,
            "mkdocs_config": "mkdocs_for_rag_indexing.yml",
            "output_dir": "compiled_md_for_rag/",
            "hook_file": "rag_indexing_hook.py",
            "manifest_file": "rag_manifest.json"
        },
        "compiled_kb_file": {"enabled": True, "source_file": "kb.comindware.ru.platform_v5_for_llm_ingestion.md"},
        "compiled_md_folder": {"enabled": True, "source_folder": "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"}
    },
    "chunk_size": 700,
    "chunk_overlap": 300,
    "min_chunk_size": 100,
    "max_chunks_per_doc": 1000,
}

EMBEDDING_CONFIG = {
    "model_name": "ai-forever/FRIDA",
    "device": "cpu",
    "batch_size": 8,
    "embedding_dim": 768,
    "max_seq_length": 512,
    "normalize_embeddings": True,
}

# Prioritized rerankers (first available is used); simple and explicit
RERANKERS = [
    {"model_name": "DiTy/cross-encoder-russian-msmarco", "batch_size": 16},
    {"model_name": "BAAI/bge-reranker-v2-m3", "batch_size": 16},
    {"model_name": "jinaai/jina-reranker-v2-base-multilingual", "batch_size": 16},
    {"model_name": "Data-Lab/multilingual-e5-small-cross-encoder-v0.1", "batch_size": 16},
]

# Retrieval knobs
RETRIEVAL_CONFIG = {
    "top_k_retrieve": 20,
    "top_k_rerank": 5,
    "metadata_boost_weights": {"tag_match": 1.2, "code_presence": 1.15, "section_match": 1.1}
}

CHROMADB_CONFIG = {
    "persist_directory": "./data/chromadb_data",
    "collection_name": "mkdocs_kb",
    "distance_function": "cosine",
    "anonymized_telemetry": False,
}

LLM_CONFIG = {
    "default_provider": "gemini",
    "default_model": "gemini-1.5-flash",
    "temperature": 0.1,
    "max_tokens": 4096,
}
```

`config/settings.py` additions (backend toggles):

```python
VECTOR_BACKEND = "chroma"  # alternatives: "qdrant", "milvus", "pgvector", "faiss"
```

## Phase 2: Document Processing Pipeline

- `core/document_processor.py`: parse frontmatter, extract structure, preserve anchors, handle MkDocs syntax, support 3 input modes
- `core/chunker.py`: section-aware, token-aware (tiktoken), 300 overlap, preserve code blocks
- `core/metadata_enricher.py`: content (has_code, code_languages, entities), structural (section_depth, position), search (keywords, summary, char_count)

## Phase 3: Embedding and Vector Store

- `retrieval/embedder.py`: abstract `Embedder` interface + adapters (FRIDA default) with prefixes (`search_query`, `search_document`, `paraphrase`, `categorize_topic`)
- `storage/vector_store.py`: Chroma init, add/upsert/delete/query, metadata filters, incremental updates, dedup by kbId
- `retrieval/vector_search.py`: wrapper over vector_store.query with filters and candidate assembly

### 3.1 FRIDA Prefix Usage (Explicit)

```python
from typing import List
from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """
    FRIDA embedder with explicit prefix usage. Optimized for Russian-English content.
    """

    def __init__(self, model_name: str = "ai-forever/FRIDA", device: str = "cpu"):
        self.model = SentenceTransformer(model_name, device=device)
        # Keep FRIDA sequence length modest for latency; configurable via settings
        self.model.max_seq_length = 512

    def embed_documents(self, texts: List[str], batch_size: int = 8) -> List[List[float]]:
        return self.model.encode(
            texts,
            prompt_name="search_document",
            batch_size=batch_size,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

    def embed_query(self, query: str) -> List[float]:
        return self.model.encode(
            query,
            prompt_name="search_query",
            normalize_embeddings=True,
        )
```

### 3.2 Chroma Document Schema and Deduplication (MVP)

- Document fields (per chunk):
  - `id`: stable unique id, e.g., `f"{kbId}:{chunk_index}:{sha1(content)}"`
  - `text`: chunk content (string)
  - `metadata` (dict):
    - `kbId` (str): article identifier or path
    - `title` (str): article/page title
    - `url` (str): canonical URL to the article
    - `section_heading` (str|optional)
    - `section_anchor` (str|optional, starts with `#`)
    - `chunk_index` (int)
    - `section_depth` (int|optional)
    - `has_code` (bool), `code_languages` (list[str])
    - `tags` (list[str]|optional)
    - `char_count` (int)

- Deduplication rule:
  - Deduplicate on `kbId + chunk_index + sha1(normalized_text)` before upsert.
  - On re-index, upsert replaces entries with the same `id`.

- Query filters (optional):
  - by `kbId`, `tags`, `has_code`.

### 3.3 VectorStore Interface and Adapters (Future-Proofing)

- Define a minimal interface to decouple retrieval from the backend:

```python
class VectorStore:
    def add(self, ids: list[str], embeddings: list[list[float]], metadatas: list[dict], documents: list[str]) -> None: ...
    def upsert(self, ids: list[str], embeddings: list[list[float]], metadatas: list[dict], documents: list[str]) -> None: ...
    def delete(self, ids: list[str] | None = None, where: dict | None = None) -> None: ...
    def query(self, embedding: list[float], top_k: int = 10, where: dict | None = None) -> dict: ...
```

- First adapter: Chroma (MVP). Future adapters: FAISS, Qdrant, Milvus, PgVector.
- Keep schema, IDs, and filters backend-agnostic. Avoid leaking vendor-specific features into `retrieval/`.

## Phase 4: Retrieval and Reranking

- `retrieval/retriever.py`: 
        - Embed query → vector_search (top-20) → group by `kbId`
        - Reconstruct articles: sort chunks by `chunk_index`, merge adjacent short chunks, cap context length
        - Context budgeting: prioritize sections whose `section_heading`/`section_anchor` match query terms; fallback to best chunk scores; keep per-article top-N chunks
- `retrieval/reranker.py`: abstract `Reranker` interface + adapters (HuggingFace cross-encoders). Use prioritized `RERANKERS`; apply metadata boosts (tags +20%, code +15%, section +10%)

## Phase 5: LLM Integration

- `llm/llm_manager.py` + provider adapters; streaming support; bilingual prompting; citation discipline

### 5.1 System Prompt and Citation Formatting

```python
# llm/prompts.py
SYSTEM_PROMPT = """You are a technical documentation assistant for Comindware Platform.

Your role:
- Answer based ONLY on provided context
- Cite sources using [Title](URL#anchor)
- If the answer is not in context, say so explicitly
- Provide short code examples when relevant
- Answer in the same language as the question (RU or EN)

Context:
{context}

Instructions:
- Use specific URLs for citations
- Include section anchors when available
- Format code with proper fences
- Be concise but comprehensive
"""


# utils/formatters.py (additions)
from typing import List, Dict


def format_response_with_citations(answer: str, articles: List[Dict]) -> str:
    citations = "\n\n## Sources:\n\n"
    for i, article in enumerate(articles, 1):
        citations += f"{i}. [{article['title']}]({article['url']})\n"
        for chunk in article.get("chunks", []):
            section = chunk["metadata"].get("section_heading")
            anchor = chunk["metadata"].get("section_anchor")
            if section and anchor:
                citations += f"   - [{section}]({article['url']}{anchor})\n"
    return answer + citations
```

### 5.2 Reuse from agent_ng (MVP-ready)

- `llm_manager.py`, `provider_adapters.py`: multi-provider streaming, retries
- `token_counter.py`: strict context budgeting per model
- `langsmith_config.py`, `langfuse_config.py`: optional observability
- `error_handler.py`: timeouts and graceful degradation

## Phase 6: Gradio App (MVP Focus)

- File: `api/app.py`
- Gradio Blocks UI; expose `gr.api(query_rag_system, api_name="query")` for programmatic calls
- Optional MCP via `demo.launch(mcp_server=True)`
- Keep business logic in retrieval/storage modules

### 6.1 Streaming Interface with API Exposure

```python
# api/app.py
import gradio as gr


def query_rag_system(question: str, provider: str = "gemini", top_k: int = 5, progress=gr.Progress()):
    if not question or not question.strip():
        yield "Please enter a question."
        return

    progress(0.1, desc="Embedding query")
    query_vec = embedder.embed_query(question)

    progress(0.3, desc="Searching")
    candidates = vector_search.search(query_vec, top_k=20)

    progress(0.5, desc="Reconstructing & reranking")
    articles = retriever.reconstruct_articles(candidates)
    reranked = reranker.rerank_with_metadata(question, articles, top_k)

    progress(0.7, desc="Generating answer")
    context = format_context(reranked)
    answer = ""
    for token in llm_manager.stream_response(question, context, provider):
        answer += token
        yield answer

    final = format_response_with_citations(answer, reranked)
    yield final


demo = gr.Interface(
    fn=query_rag_system,
    inputs=[
        gr.Textbox(label="Question", placeholder="Как использовать N3? / How to use N3?", lines=2),
        gr.Dropdown(["gemini", "groq", "openrouter"], value="gemini", label="LLM"),
        gr.Slider(1, 10, value=5, label="Sources (top_k)")
    ],
    outputs=gr.Markdown(label="Answer"),
    title="Comindware Platform Documentation Assistant",
)

# Expose an API endpoint for programmatic access
demo.api(fn=query_rag_system, inputs=[gr.Textbox(), gr.Textbox(), gr.Number()], api_name="query")

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
```

### 6.2 Preferred UI: ChatInterface (lean MVP)

```python
# api/app.py (alternative)
import gradio as gr


def chat_handle(message: str, history: list):
    if not message or not message.strip():
        yield "Введите вопрос / Enter a question."
        return

    query_vec = embedder.embed_query(message)
    candidates = vector_search.search(query_vec, top_k=20)
    articles = retriever.reconstruct_articles(candidates)
    reranked = reranker.rerank_with_metadata(message, articles, top_k=5)
    context = format_context(reranked)

    answer = ""
    for token in llm_manager.stream_response(message, context, provider="gemini"):
        answer += token
        yield answer

    yield format_response_with_citations(answer, reranked)


demo = gr.ChatInterface(
    fn=chat_handle,
    title="Comindware Docs Assistant",
    description="RU/EN RAG with citations",
)

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
```

## Testing & Evaluation (Concise)

- Golden set: 50 RU/EN queries with expected `kbId` and optional `section_anchor`
- Metrics: recall@5 by `kbId`, MRR, latency P95 < 3s, citation URL/anchor validity
- Report: per-query scores; failure cases (wrong article, missing anchor, timeout)

## Citations (Concise)

- Prefer section-level links: `[Title](URL#anchor)`; group by article with matched sections listed beneath
- Validate anchors exist; fallback to article URL if anchor missing

## Config & Env Knobs (Concise)

- EMBEDDING_MODEL, DEVICE, BATCH_SIZE
- EMBEDDING_BACKEND (default: sentence-transformers)
- RERANKERS prioritized list (first available), with batch sizes
- TOP_K_RETRIEVE, TOP_K_RERANK, CHUNK_SIZE, CHUNK_OVERLAP
- CHROMADB_PERSIST_DIR, CHROMADB_COLLECTION
- VECTOR_BACKEND (chroma|qdrant|milvus|pgvector|faiss)
- GRADIO_SERVER_NAME, GRADIO_SERVER_PORT, MCP_SERVER
- MKDOCS_CONFIG, RAG_OUTPUT_DIR, MANIFEST_FILE

## Phase 6.9 (Deprioritized): Future Migration to FastAPI + FastMCP

- When REST auth/rate-limiting/observability is needed
- Path: mount Gradio, or call via `gradio_client`; replace `gr.api` with FastAPI routes; add MCP via FastMCP + MCP SDK
- References: https://www.gradio.app/docs/gradio/mount_gradio_app, https://www.gradio.app/guides/fastapi-app-with-the-gradio-client, https://gofastmcp.com/integrations/fastapi, https://github.com/jlowin/fastmcp?tab=readme-ov-file, https://github.com/modelcontextprotocol/python-sdk

## Local Setup (venv) & Requirements

- `scripts/build_index.py`: scan → parse/chunk → enrich → embed → store (supports all 3 modes)
- `scripts/test_queries.py`: bilingual test set + metrics
- `requirements.txt`: minimal set for MD-based RAG; no PDF/Doc ingestion; no Docker
- `.env.example`: embedding/LLM keys, RAG knobs, Chroma, reranker, Gradio server

### 8.1 Create and use a virtual environment

```bash
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt

# Build MkDocs compiled MD (mode 1)
mkdocs build -f mkdocs_for_rag_indexing.yml

# Build index (choose one source)
python rag_engine/scripts/build_index.py --source compiled_md_for_rag/
python rag_engine/scripts/build_index.py --source kb.comindware.ru.platform_v5_for_llm_ingestion.md
python rag_engine/scripts/build_index.py --source "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"

# Run UI
python rag_engine/api/app.py
```

### 8.1.1 build_index.py CLI (MVP)

```bash
python rag_engine/scripts/build_index.py \
  --source <PATH-OR-FILE> \
  --mode {mkdocs|combined|folder} \
  --persist-dir ./data/chromadb_data \
  --collection mkdocs_kb \
  --chunk-size 700 \
  --chunk-overlap 300 \
  --max-chunks-per-doc 1000 \
  --reindex
```

- `--source`: path to compiled MD folder or combined MD file
- `--mode`: ingestion mode (mkdocs: compiled_md_for_rag/, combined: single MD file, folder: compiled MD tree)
- `--reindex`: force rebuild embeddings for changed/new files
- Defaults are read from `config/settings.py`, CLI flags override settings

Companion CLI to export MkDocs from an external project (optional step before indexing). Default output lives in the RAG agent repo:

```bash
python rag_engine/scripts/run_mkdocs_export.py \
  --project-dir <PATH-TO-MKDOCS-REPO> \
  --inherit-config mkdocs_guide_complete_ru.yml \
  --output-dir <PATH-TO-RAG-REPO>/rag_engine/data/compiled_md_for_rag
```

- Produces `<PATH-TO-RAG-REPO>/rag_engine/data/compiled_md_for_rag/` which you pass to `--source` in `build_index.py` with `--mode mkdocs`.

### MVP leanness decisions

- Python venv only (no Docker), minimal dependencies
- MD-only ingestion via 3 modes (MkDocs pipeline, combined MD file, compiled MD folder)
- Single embedder (FRIDA), single vector store (Chroma), single UI (Gradio ChatInterface)
- Keep metadata-enriched chunks; postpone heavy observability and advanced ranking to Phase 2

### 8.2 requirements.txt (MD-only)

```txt
# Core
chromadb>=0.4.22
sentence-transformers>=2.2.2
langchain-text-splitters>=0.0.1
tiktoken>=0.5.2

# LLM providers (LangChain adapters)
langchain>=0.1.0
langchain-google-genai>=0.0.5
langchain-groq>=0.0.1
langchain-mistralai>=0.0.1
langchain-openai>=0.0.5

# Web interface
gradio>=4.0.0

# Utilities
python-dotenv>=1.0.0
pyyaml>=6.0
pydantic>=2.5.0
numpy>=1.24.0
tqdm>=4.66.0
```

### 8.3 .env.example

```env
# Embedding
EMBEDDING_MODEL=ai-forever/FRIDA

# LLM Providers
GOOGLE_API_KEY=
GROQ_API_KEY=
OPENROUTER_API_KEY=
MISTRAL_API_KEY=

# RAG Config
DEFAULT_LLM_PROVIDER=gemini
DEFAULT_MODEL=gemini-1.5-flash
CHUNK_SIZE=700
CHUNK_OVERLAP=300
TOP_K_RETRIEVE=20
TOP_K_RERANK=5

# ChromaDB
CHROMADB_PERSIST_DIR=./data/chromadb_data
CHROMADB_COLLECTION=mkdocs_kb

# Paths
RAG_OUTPUT_DIR=./rag_engine/data/compiled_md_for_rag

# Reranker
RERANKER_MODEL=DiTy/cross-encoder-russian-msmarco

# Observability (optional)
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=mkdocs-rag

# Web Interface
GRADIO_SERVER_NAME=0.0.0.0
GRADIO_SERVER_PORT=7860
```

Optional future switches (do not set for MVP):

```env
# Embeddings backend (keep default for MVP)
EMBEDDING_BACKEND=sentence-transformers

# Vector store backend (keep chroma for MVP)
VECTOR_BACKEND=chroma
```

### 8.4 Acceptance criteria for successful index build (MVP)

- Manifest count ~= number of indexed `.md` files (± files with `max_chunks_per_doc` cap)
- No empty chunks; average `char_count` > 100
- Chroma collection `${CHROMADB_COLLECTION}` exists with > 1k vectors (for full repo)
- Random query returns > 1 result with valid `kbId`, `url`, `section_anchor`
- Reranker runs without errors; top-5 contain at least 2 distinct `kbId`

## Phase 2: Hardening & Optimizations (deferred)

- Dynamic top-K for retrieval based on query length/ambiguity
- MMR diversification and per-`kbId` caps before context assembly
- Minimum relevance threshold + explicit "no answer from context" fallback
- Batched/async cross-encoder reranker for latency smoothing
- Lightweight TTL caches for query embeddings and retrieval results
- Structured outputs with timings and applied thresholds for UI/logs
- Anchor existence validation with precomputed index; repair missing anchors
- Optional observability (LangSmith/Langfuse) and analytics
- Optional MCP or FastAPI migration; mount Gradio or call via gradio_client
- Define `Chunker` and `MetadataEnricher` interfaces to allow strategy swaps (keep current implementations as defaults)
- Constructor injection across modules (retriever, reranker, embedder, vector store) to ease swapping components

## Success Metrics

- Indexing < 20m; latency < 3s; Top-5 accuracy > 90%; citations 100% valid

## Todos (Single Atomic Checklist)

- [ ] Create `mkdocs_for_rag_indexing.yml` and `rag_indexing_hook.py`; verify compiled MD + manifest
- [ ] Scaffold project tree; add `__init__.py`, `.env.example`, `requirements.txt`, `README.md`
- [ ] Implement `config/settings.py` (3 modes, DiTy default reranker + alternatives, FRIDA, Chroma, LLM)
- [ ] Implement `core/document_processor.py`, `core/chunker.py` (section-aware, token-aware, code-safe), `core/metadata_enricher.py`
- [ ] Implement `storage/vector_store.py` (Chroma CRUD + filters), `retrieval/vector_search.py`, `retrieval/embedder.py` (abstract + adapters; FRIDA default)
  - [ ] Define `VectorStore` interface; implement Chroma adapter; keep interface vendor-agnostic
  - [ ] Define abstract `Embedder` + adapter; implement FRIDA; allow model/provider override via config
- [ ] Implement `retrieval/retriever.py` (group/sort/merge/budget), `retrieval/reranker.py` (abstract + adapters; prioritized `RERANKERS` + boosts)
- [ ] Integrate `llm_manager.py` + providers; prompts + citation formatter
- [ ] Build Gradio ChatInterface `api/app.py`; also expose `gr.api("/query")`
- [ ] Implement `scripts/build_index.py` with CLI flags; implement `scripts/test_queries.py` (RU/EN, metrics); add basic unit tests
- [ ] Local venv workflow: finalize requirements, update README with usage, CLI flags, and Phase 2 roadmap
  - [ ] Implement `scripts/run_mkdocs_export.py` to export compiled MD from an external MkDocs repo
  
  Phase 2 (deferred):
  - [ ] Define `Chunker` and `MetadataEnricher` interfaces; keep current implementations as defaults
  - [ ] MMR diversification, per-`kbId` caps, thresholds, async reranker, caches, structured outputs

### To-dos

- [ ] Create mkdocs_for_rag_indexing.yml and rag_indexing_hook.py
- [ ] Create expanded tree and __init__.py files
- [ ] Add .env.example, requirements.txt, README.md
- [ ] Implement config/settings.py with 3 modes and defaults
- [ ] Implement core/document_processor.py
- [ ] Implement core/chunker.py (token-aware, section-aware, code-safe)
- [ ] Implement core/metadata_enricher.py
- [ ] Implement retrieval/embedder.py (FRIDA + prefixes)
- [ ] Implement storage/vector_store.py (Chroma CRUD + filters)
- [ ] Implement retrieval/vector_search.py wrapper
- [ ] Implement retrieval/retriever.py pipeline + reconstruction
- [ ] Implement retrieval/reranker.py (DiTy default + alternatives + boosts)
- [ ] Integrate llm_manager.py + provider adapters
- [ ] Add RAG prompts and citation formatter
- [ ] Build Gradio app api/app.py + gr.api endpoint
- [ ] Optionally enable MCP server (launch mcp_server=True)
- [ ] Create scripts/build_index.py for all 3 modes
- [ ] Create scripts/test_queries.py (RU/EN)
- [ ] Add unit tests under tests/
- [ ] Create Dockerfile and Nginx config
- [ ] Update README with usage and migration notes