<!-- 79df14cf-6fa1-4eaa-83ff-d250b56e4c3e 02877c14-6bc5-441e-92f0-4486a606ea94 -->
# MkDocs RAG Engine Implementation Plan

## Overview

Build a production-ready RAG (Retrieval-Augmented Generation) engine for the MkDocs documentation repository that handles Jinja2-rich source files through MkDocs build pipeline integration. Uses FRIDA (best Russian embedder), ChromaDB vector store, cross-encoder reranking, and multi-LLM support with streaming responses.

## Project Rationale & Design Decisions

### 1. ChromaDB vs Supabase

**Answer: YES, ChromaDB is the better choice for documentation RAG.**

**Rationale:**

- **Purpose-built for RAG**: Designed specifically for vector search, not general-purpose DB
- **Local/self-hosted**: No cloud dependencies, runs alongside MkDocs
- **Rich metadata**: Native arbitrary metadata per vector (kbId, URLs, anchors)
- **Better performance**: Optimized for similarity search
- **Persistent storage**: Built-in disk persistence
- **Simpler stack**: One less external service
- **Cost-effective**: No subscription costs

### 2. Metadata-Enriched Chunks

**This is a CORE design principle.**

**Metadata per chunk:**

```python
{
    "kbId": "4966",
    "url": "https://kb.comindware.ru/article.php?id=4966",
    "title": "Вычисление пользователей...",
    "section_heading": "Настройка вычисления",
    "section_anchor": "#example_n3_calculate_active_task_accounts_configure",
    "chunk_index": 2,
    "tags": ["N3", "Notation 3", ...],
    "has_code": True
}
```

**Usage:**

1. **Article Reconstruction**: Group chunks by kbId → reconstruct full articles
2. **Complete Context**: LLM gets entire article, not fragments
3. **Reranker Boosting**: Tag match +20%, code presence +15%, section match +10%
4. **Precise Citations**: URLs with section anchors

### 3. MVP Component Reuse (~40%)

**From `cmw-platform-agent`:**

- ✅ LLM Manager (multi-provider)
- ✅ Provider Adapters
- ✅ Observability configs (LangSmith, Langfuse)
- ✅ PDF/File utils

**From `agent-course-final-assignment`:**

- ✅ Vector store patterns
- ✅ Document processing

**From `rag_agent`:**

- ✅ Chunking strategy (700/300)
- ✅ Recursive scanning
- ✅ Query loop

**New (~60%):**

- 🆕 MkDocs hook for Jinja2 resolution
- 🆕 3-mode processor (pipeline/KB file/folder)
- 🆕 FRIDA integration with prefix support
- 🆕 Cross-encoder reranker with metadata boosting

### 4. Reference Repos & Docs

- https://github.com/arterm-sedov/cmw-platform-agent
- https://github.com/arterm-sedov/agent-course-final-assignment
- https://github.com/AsyncFuncAI/deepwiki-open
- https://habr.com/ru/articles/955798/
- https://github.com/CodeCutTech/Data-science/blob/master/machine_learning/open_source_rag_pipeline_intelligent_qa_system.ipynb
- https://huggingface.co/ai-forever/FRIDA

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
         FRIDA Embedder (4 prefix modes)
                    ↓
         ChromaDB Vector Store (persistent)
                    ↓
         Query Pipeline:
           → Embed query with FRIDA
           → Vector search (top-20)
           → Cross-encoder reranking (top-5)
           → Article reconstruction
           → Multi-LLM generation
           → Stream response + citations
```

## Phase 1: MkDocs Integration & Project Setup

### 1.0 MkDocs Build Pipeline Integration

**Problem:** Raw MkDocs files contain Jinja2 syntax that cannot be indexed directly.

**Solution:** Custom MkDocs config + hook to export Jinja2-compiled markdown.

#### File 1: `mkdocs_for_rag_indexing.yml`

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

#### File 2: `rag_indexing_hook.py`

```python
"""
MkDocs hook to export Jinja2-compiled markdown for RAG indexing.
Similar to kb_html_cleanup_hook.py but outputs compiled MD files.
"""
import json
import os
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
        # Write frontmatter
        if page.meta:
            f.write('---\n')
            yaml.dump(page.meta, f, allow_unicode=True, default_flow_style=False)
            f.write('---\n\n')
        # Write compiled markdown
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

**Usage:**

```bash
mkdocs build -f mkdocs_for_rag_indexing.yml
# Output: compiled_md_for_rag/ with Jinja2-resolved files
```

### 1.1 Project Structure

```
rag_engine/
├── config/
│   ├── __init__.py
│   ├── settings.py          # 3 input modes configuration
│   └── input_modes.py
├── core/
│   ├── __init__.py
│   ├── document_processor.py   # Supports all 3 modes
│   ├── chunker.py
│   ├── metadata_enricher.py
│   └── vector_store.py
├── llm/
│   ├── __init__.py
│   ├── llm_manager.py       # From cmw-platform-agent
│   ├── provider_adapters.py
│   ├── langsmith_config.py
│   └── langfuse_config.py
├── retrieval/
│   ├── __init__.py
│   ├── embedder.py          # FRIDA with prefixes
│   ├── retriever.py
│   └── reranker.py
├── tools/
│   ├── __init__.py
│   ├── pdf_utils.py         # From cmw-platform-agent
│   └── file_utils.py
├── api/
│   ├── __init__.py
│   ├── app.py               # Gradio interface
│   └── models.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── helpers.py
├── scripts/
│   ├── build_mkdocs_for_rag.sh
│   ├── build_index.py
│   └── test_queries.py
├── data/                     # ChromaDB persistence
├── tests/                    # Test suite
├── requirements.txt
├── .env.example
└── README.md
```

### 1.2 Configuration (Complete)

**File:** `config/settings.py`

```python
import os
from pathlib import Path

# === Input Source Configuration ===
INDEXING_CONFIG = {
    "input_modes": {
        "mkdocs_pipeline": {
            "enabled": True,
            "mkdocs_config": "mkdocs_for_rag_indexing.yml",
            "output_dir": "compiled_md_for_rag/",
            "hook_file": "rag_indexing_hook.py",
            "manifest_file": "rag_manifest.json"
        },
        "compiled_kb_file": {
            "enabled": True,
            "source_file": "kb.comindware.ru.platform_v5_for_llm_ingestion.md"
        },
        "compiled_md_folder": {
            "enabled": True,
            "source_folder": "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"
        }
    },
    "chunk_size": 700,           # tokens
    "chunk_overlap": 300,        # tokens
    "min_chunk_size": 100,
    "max_chunks_per_doc": 1000,  # Safety limit
}

# === Embedding Configuration ===
EMBEDDING_CONFIG = {
    "model_name": "ai-forever/FRIDA",
    "device": "cpu",  # Auto-detect GPU if available
    "batch_size": 8,   # CPU optimized (32 for GPU)
    "embedding_dim": 768,
    "max_seq_length": 512,
    "normalize_embeddings": True,
}

# === Reranker Configuration ===
RERANKER_CONFIG = {
    "model_name": "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1",
    "top_k_retrieve": 20,
    "top_k_rerank": 5,
    "batch_size": 16,
    "metadata_boost_weights": {
        "tag_match": 1.2,
        "code_presence": 1.15,
        "section_match": 1.1
    }
}

# === ChromaDB Configuration ===
CHROMADB_CONFIG = {
    "persist_directory": "./data/chromadb_data",
    "collection_name": "mkdocs_kb",
    "distance_function": "cosine",
    "anonymized_telemetry": False,
}

# === LLM Configuration ===
LLM_CONFIG = {
    "default_provider": os.getenv("DEFAULT_LLM_PROVIDER", "gemini"),
    "default_model": os.getenv("DEFAULT_MODEL", "gemini-1.5-flash"),
    "temperature": 0.1,
    "max_tokens": 4096,
}
```

## Phase 2: Document Processing Pipeline

### 2.1 Document Processor (3-Mode Support)

**File:** `core/document_processor.py`

Key features:

- Parse YAML frontmatter (kbId, title, tags, url)
- Extract markdown structure (headings, code blocks)
- Preserve anchors (e.g., `{: #section_anchor }`)
- Handle MkDocs-specific syntax
- **Support all 3 input modes**

**Example output:**

```python
{
    "file_path": "docs/ru/examples/n3_calculate_active_task_accounts.md",
    "metadata": {
        "kbId": "4966",
        "title": "Вычисление пользователей с активными задачами",
        "url": "https://kb.comindware.ru/article.php?id=4966",
        "tags": ["N3", "Notation 3", "RDF", ...],
        "language": "ru"
    },
    "sections": [
        {
            "heading": "Введение",
            "anchor": "#example_n3_calculate_active_task_accounts_intro",
            "level": 2,
            "content": "...",
            "has_code": False
        }
    ]
}
```

### 2.2 Smart Text Chunker

**File:** `core/chunker.py`

Strategies:

1. **Section-based**: Respect heading boundaries
2. **Token-aware**: Use `RecursiveCharacterTextSplitter` + `tiktoken`
3. **Overlap with context**: 300-token overlap with heading context
4. **Code preservation**: Never split code blocks
5. **Metadata inheritance**: Each chunk inherits section metadata

**Chunk structure:**

```python
{
    "chunk_id": "4966_chunk_002",
    "content": "...",
    "metadata": {
        "kbId": "4966",
        "url": "https://kb.comindware.ru/article.php?id=4966",
        "title": "...",
        "section_heading": "...",
        "section_anchor": "...",
        "chunk_index": 2,
        "total_chunks": 5,
        "has_code": True,
        "tags": [...],
        "language": "ru"
    }
}
```

### 2.3 Metadata Enricher

**File:** `core/metadata_enricher.py`

Enrich with:

1. **Content-based**: `has_code`, `code_languages`, `entity_types`, `complexity_score`
2. **Structural**: `section_depth`, `position_in_article`, `related_sections`
3. **Search optimization**: `keywords`, `summary`, `char_count`

## Phase 3: Embedding and Vector Store

### 3.1 FRIDA Embedding Generator

**File:** `retrieval/embedder.py`

**Why FRIDA:**

- Best-in-class: 62.18 avg on ruMTEB
- 4M+ Russian-English pairs
- 4 specialized prefixes
- 0.8B parameters
- CPU-friendly (100-200ms/query)

**FRIDA Prefix System:**

1. `search_query` + `search_document` - For retrieval
2. `paraphrase` - For similar sections
3. `categorize_topic` - For domain grouping
4. `categorize` - General categorization

**Implementation:**

```python
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name="ai-forever/FRIDA", device="cpu"):
        self.model = SentenceTransformer(model_name, device=device)
        self.model.max_seq_length = 512
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(
            texts,
            prompt_name="search_document",
            batch_size=8,
            show_progress_bar=True,
            normalize_embeddings=True
        )
    
    def embed_query(self, query: str) -> List[float]:
        return self.model.encode(
            query,
            prompt_name="search_query",
            normalize_embeddings=True
        )
```

### 3.2 ChromaDB Vector Store

**File:** `core/vector_store.py`

Operations:

1. **Initialization** with persistence
2. **Indexing** with rich metadata
3. **Querying** with metadata filters
4. **Incremental updates**
5. **Deduplication** by kbId

## Phase 4: Retrieval and Reranking

### 4.1 Vector Retriever

**File:** `retrieval/retriever.py`

Pipeline:

1. Embed query
2. Search ChromaDB (top-20)
3. Group chunks by kbId
4. Reconstruct full articles
5. Prepare for reranking

**Article reconstruction:**

```python
def reconstruct_articles(chunks: List[Dict]) -> List[Dict]:
    articles = {}
    for chunk in chunks:
        kb_id = chunk["metadata"]["kbId"]
        if kb_id not in articles:
            articles[kb_id] = {
                "kbId": kb_id,
                "title": chunk["metadata"]["title"],
                "url": chunk["metadata"]["url"],
                "chunks": [],
                "best_score": chunk["distance"]
            }
        articles[kb_id]["chunks"].append(chunk)
    
    for article in articles.values():
        article["chunks"].sort(key=lambda c: c["metadata"]["chunk_index"])
    
    return list(articles.values())
```

### 4.2 Cross-Encoder Reranker

**File:** `retrieval/reranker.py`

**What is it:** Jointly encodes query+document for direct relevance score

**Why better:** Captures semantic relationships, understands nuance

**Model:** `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`

**Metadata boosting:**

- Tag match: +20%
- Code presence: +15%
- Section match: +10%

## Phase 5: LLM Integration

### 5.1 Multi-LLM Manager

**Copy from `cmw-platform-agent/agent_ng/`:**

- `llm_manager.py`
- `provider_adapters.py`
- `langsmith_config.py`
- `langfuse_config.py`
- Relevant `utils.py` functions

**Configure in `.env`:**

```env
GOOGLE_API_KEY=...
GROQ_API_KEY=...
OPENROUTER_API_KEY=...
DEFAULT_LLM_PROVIDER=gemini
```

### 5.2 RAG Prompts

**System prompt:**

```python
SYSTEM_PROMPT = """You are a technical documentation assistant for Comindware Platform.

Your role:
- Answer based ONLY on provided context
- Cite sources: [Title](URL#anchor)
- State if info not in context
- Provide code examples when relevant
- Answer in same language as question

Context:
{context}

Instructions:
- Use specific URLs for citations
- Include section anchors
- Format code with syntax highlighting
- Be concise but comprehensive
"""
```

**Citation formatting:**

```python
def format_response_with_citations(answer: str, articles: List[Dict]) -> str:
    citations = "\n\n## Sources:\n\n"
    for i, article in enumerate(articles, 1):
        citations += f"{i}. [{article['title']}]({article['url']})\n"
        for chunk in article["chunks"]:
            section = chunk["metadata"].get("section_heading")
            anchor = chunk["metadata"].get("section_anchor")
            if section and anchor:
                citations += f"   - [{section}]({article['url']}{anchor})\n"
    return answer + citations
```

## Phase 6: Web Interface

### 6.1 Gradio Interface

**File:** `api/app.py`

Features:

- Streaming responses
- Source citations
- LLM provider selection
- Top-k configuration
- Example queries

**Implementation:**

```python
import gradio as gr

def query_rag_system(question: str, llm_provider: str, top_k: int, progress=gr.Progress()):
    progress(0, desc="Embedding query...")
    query_embedding = embedder.embed_query(question)
    
    progress(0.2, desc="Searching...")
    results = vector_store.search(query_embedding, top_k=20)
    
    progress(0.4, desc="Reranking...")
    articles = retriever.reconstruct_articles(results)
    reranked = reranker.rerank_with_metadata(question, articles, top_k)
    
    progress(0.6, desc="Generating answer...")
    context = format_context(reranked)
    
    answer = ""
    for chunk in llm_manager.stream_response(question, context, llm_provider):
        answer += chunk
        yield answer
    
    final = format_response_with_citations(answer, reranked)
    yield final

demo = gr.Interface(
    fn=query_rag_system,
    inputs=[
        gr.Textbox(label="Question", placeholder="Как использовать N3?"),
        gr.Dropdown(["gemini", "groq", "openrouter"], value="gemini"),
        gr.Slider(1, 10, value=5, label="Sources")
    ],
    outputs=gr.Markdown(label="Answer"),
    title="Comindware Platform Documentation Assistant",
    examples=[
        ["Как создать вычисляемый атрибут?", "gemini", 5],
        ["Что такое N3 выражения?", "gemini", 5]
    ]
)

demo.queue().launch(server_name="0.0.0.0", server_port=7860)
```

## Phase 7: Build & Deployment Scripts

### 7.1 Index Building Script

**File:** `scripts/build_index.py`

```python
import argparse

def build_index(source_path: str, rebuild: bool = False):
    print(f"📚 Processing: {source_path}")
    
    # 1. Scan documents
    documents = document_processor.scan_directory(source_path)
    print(f"   Found {len(documents)} documents")
    
    # 2. Parse and chunk
    all_chunks = []
    for doc in documents:
        parsed = document_processor.parse_document(doc)
        chunks = chunker.create_chunks(parsed)
        enriched = metadata_enricher.enrich(chunks)
        all_chunks.extend(enriched)
    
    print(f"   Created {len(all_chunks)} chunks")
    
    # 3. Generate embeddings
    print("   Generating embeddings...")
    embeddings = embedder.embed_documents([c["content"] for c in all_chunks])
    
    # 4. Store
    print("   Storing in ChromaDB...")
    vector_store.add_documents(all_chunks, embeddings, rebuild=rebuild)
    
    print("✅ Index built!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    build_index(args.source, args.rebuild)
```

**Usage:**

```bash
# Mode 1: MkDocs pipeline
mkdocs build -f mkdocs_for_rag_indexing.yml
python scripts/build_index.py --source compiled_md_for_rag/

# Mode 2: Compiled KB file
python scripts/build_index.py --source kb.comindware.ru.platform_v5_for_llm_ingestion.md

# Mode 3: phpkb folder
python scripts/build_index.py --source "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"
```

### 7.2 Testing Script

**File:** `scripts/test_queries.py`

```python
TEST_QUERIES = [
    "Как создать вычисляемый атрибут с помощью N3?",
    "What are the system requirements?",
    "Как настроить подключение к электронной почте?",
    "How do if-else statements work in N3?"
]

def test_rag_system():
    for query in TEST_QUERIES:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print('='*60)
        response = rag_system.query(query)
        print(response)
```

## Phase 8: Documentation & Deployment

### 8.1 Requirements

**File:** `requirements.txt`

```txt
# Core
chromadb>=0.4.22
sentence-transformers>=2.2.2
langchain>=0.1.0
langchain-text-splitters>=0.0.1
tiktoken>=0.5.2

# LLM providers
langchain-google-genai>=0.0.5
langchain-groq>=0.0.1
langchain-mistralai>=0.0.1
langchain-openai>=0.0.5

# File processing
pymupdf4llm>=0.0.3
python-docx>=0.8.11
pandas>=2.0.0

# Web interface
gradio>=4.0.0

# Utilities
python-dotenv>=1.0.0
pyyaml>=6.0
pydantic>=2.5.0
numpy>=1.24.0
tqdm>=4.66.0

# Observability (optional)
langsmith>=0.0.70
langfuse>=2.0.0
```

### 8.2 Environment Configuration

**File:** `.env.example`

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
CHUNK_SIZE=700
CHUNK_OVERLAP=300
TOP_K_RETRIEVE=20
TOP_K_RERANK=5

# ChromaDB
CHROMADB_PERSIST_DIR=./data/chromadb_data
CHROMADB_COLLECTION=mkdocs_kb

# Reranker
RERANKER_MODEL=cross-encoder/mmarco-mMiniLMv2-L12-H384-v1

# Observability
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=mkdocs-rag

# Web Interface
GRADIO_SERVER_NAME=0.0.0.0
GRADIO_SERVER_PORT=7860
```

### 8.3 Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download models
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('ai-forever/FRIDA')"

EXPOSE 7860
CMD ["python", "api/app.py"]
```

### 8.4 Nginx Configuration

```nginx
location /rag/ {
    proxy_pass http://localhost:7860/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

## Success Metrics

- **Indexing speed:** < 20 minutes for full docs (500+ documents)
- **Query latency:** < 3 seconds end-to-end
- **Retrieval accuracy:** Top-5 correct > 90%
- **Citation accuracy:** 100% valid links

## Next Steps After Implementation

1. **Evaluation:** 50-question test set with ground truth
2. **Fine-tuning:** Adjust chunk size, overlap, top-k
3. **Monitoring:** Query logging and analytics
4. **User feedback:** Relevance scoring loop
5. **Auto-reindexing:** Connect to MkDocs build pipeline

### To-dos

- [ ] Create mkdocs_for_rag_indexing.yml config and rag_indexing_hook.py for Jinja2-compiled markdown export
- [ ] Create rag_engine/ project structure with all subdirectories (config, core, llm, retrieval, tools, api, utils, scripts, data, tests)
- [ ] Copy LLM manager from cmw-platform-agent (llm_manager.py, provider_adapters.py, langsmith_config.py, langfuse_config.py, utils.py)
- [ ] Implement complete config/settings.py with 3 input modes, embedding, reranker, ChromaDB, and LLM configurations
- [ ] Implement document processor with frontmatter parsing, markdown extraction, anchor preservation, and support for all 3 input modes
- [ ] Implement semantic chunker with section-based splitting, token counting (tiktoken), 700/300 overlap, and code block preservation
- [ ] Implement metadata enricher for content-based, structural, and search optimization metadata
- [ ] Implement FRIDA embedding generator with 4 prefix modes (search_query, search_document, categorize_topic, paraphrase)
- [ ] Implement ChromaDB vector store with rich metadata support, persistence, and incremental updates
- [ ] Implement vector retriever with article reconstruction, metadata filtering, and grouping by kbId
- [ ] Implement cross-encoder reranker with metadata boosting (tag +20%, code +15%, section +10%)
- [ ] Integrate multi-LLM manager and implement RAG-specific prompts with streaming support
- [ ] Implement response formatter with citations, source links, and section anchors
- [ ] Create build_index.py script supporting all 3 input modes with argparse CLI
- [ ] Implement Gradio web interface with streaming, source display, LLM selection, and example queries
- [ ] Create test_queries.py with Russian/English test cases
- [ ] Write comprehensive README with architecture, installation, 3-mode usage, and deployment guide
- [ ] Create requirements.txt, .env.example, Dockerfile, and nginx configuration for production deployment