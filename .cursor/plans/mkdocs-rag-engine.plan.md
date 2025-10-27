<!-- cef902af-b944-421b-b9d0-9c1ef7737ea1 de81aee6-21d7-4324-92ca-ca0ec2f84f93 -->
# MkDocs RAG Engine Implementation Plan

## Overview

Build a production-ready RAG (Retrieval-Augmented Generation) engine for the MkDocs documentation repository that handles Jinja2-rich source files through MkDocs build pipeline integration. Uses FRIDA (best Russian embedder), ChromaDB vector store, cross-encoder reranking, and multi-LLM support with streaming responses.

## Project Rationale & Design Decisions

This section addresses the original requirements that guided the design:

### 1. ChromaDB vs Supabase

**Question:** "Is chromadb better then the supabase I used in my other MVPs?"

**Answer: YES, ChromaDB is the better choice for documentation RAG.**

**Rationale:**

- **Purpose-built for RAG**: Designed specifically for vector search, not general-purpose DB
- **Local/self-hosted**: No cloud dependencies, runs alongside MkDocs
- **Rich metadata**: Native arbitrary metadata per vector (kbId, URLs, anchors)
- **Better performance**: Optimized for similarity search
- **Persistent storage**: Built-in disk persistence
- **Simpler stack**: One less external service
- **Cost-effective**: No subscription costs

**Supabase advantages** (not needed here): Multi-user real-time, auth, PostgreSQL relations

### 2. Metadata-Enriched Chunks

**Question:** "Can we enrich each chunk with metadata (article id, url, summary) and use them to feed the LLM with complete articles instead of naive chunks? Can we use metadata in the reranker?"

**Answer: YES, this is a CORE design principle.**

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

### 3. Lean Solution with Metadata

**Question:** "Can we create a lean solution with minimum overhead that still uses metadata?"

**Answer: YES, through smart architecture.**

**Lean implementation:**

- Minimal deps: ChromaDB (local), FRIDA (one model), sentence-transformers, Gradio
- Fast metadata: Parse frontmatter (~1ms), not LLM calls
- Optional LLM enrichment when needed
- Batch processing, CPU-friendly
- Persistent caching
- No cloud costs

**Result**: 15-20min indexing, ~4GB RAM, zero ongoing costs

### 4. DeepWiki-Open Usage

**Question:** "Is deepwiki-open a good starting point? Or start clean?"

**Answer: Start clean, borrow architectural patterns.**

**Why not fork:**

- Built for code repos (AST parsing), not docs
- Python/JS focus, not Markdown
- Lacks MkDocs specifics (Jinja2, kbId)

**What we borrow:**

- RAG architecture flow
- Chunking strategies
- Query pipeline design
- ChromaDB patterns

**Our additions:**

- MkDocs pipeline integration
- Jinja2 resolution hook
- Documentation metadata
- FRIDA embeddings
- 3 input modes

### 5. MVP Component Reuse

**Question:** "What can we use from our MVP agents?"

**Answer: ~40% code reuse.**

**From `cmw-platform-agent`:**

- ✅ LLM Manager (multi-provider)
- ✅ Provider Adapters
- ✅ Observability configs
- ✅ PDF/File utils

**From `agent-course-final-assignment`:**

- ✅ Vector store patterns
- ✅ Document processing

**From `rag_agent`:**

- ✅ Chunking strategy (700/300)
- ✅ Recursive scanning
- ✅ Query loop

**New (~60%):**

- 🆕 MkDocs hook
- 🆕 3-mode processor
- 🆕 FRIDA integration
- 🆕 Cross-encoder reranker

## Reference Repos & Docs

https://github.com/arterm-sedov/cmw-platform-agent

https://github.com/arterm-sedov/agent-course-final-assignment

https://github.com/AsyncFuncAI/deepwiki-open

https://habr.com/ru/articles/955798/

https://github.com/CodeCutTech/Data-science/blob/master/machine_learning/open_source_rag_pipeline_intelligent_qa_system.ipynb

https://huggingface.co/ai-forever/FRIDA

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
         Metadata Enricher (rich metadata + optional LLM)
                    ↓
         FRIDA Embedder (4 prefix modes: search_query, search_document, 
                         categorize_topic, paraphrase)
                    ↓
         ChromaDB Vector Store (persistent, metadata-rich)
                    ↓
         Query Pipeline:
           → Embed query with FRIDA (search_query prefix)
           → Vector search (top-20)
           → Cross-encoder reranking (top-5)
           → Article reconstruction
           → Multi-LLM generation
           → Stream response + citations
```

## Phase 1: MkDocs Integration & Project Setup

### 1.0 MkDocs Build Pipeline Integration (NEW)

**Problem:** Raw MkDocs files contain Jinja2 syntax (`{{ productName }}`, `{% if %}`) that cannot be indexed directly.

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
│   ├── settings.py          # 3 input modes
│   └── input_modes.py
├── core/
│   ├── __init__.py
│   ├── document_processor.py   # 3 modes support
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
│   ├── embedder.py          # FRIDA
│   ├── retriever.py
│   └── reranker.py
├── tools/
│   ├── __init__.py
│   ├── pdf_utils.py         # From cmw-platform-agent
│   └── file_utils.py
├── api/
│   ├── __init__.py
│   ├── app.py               # Gradio
│   └── models.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── helpers.py
├── scripts/
│   ├── build_mkdocs_for_rag.sh
│   ├── build_index.py
│   └── test_queries.py
├── requirements.txt
├── .env.example
└── README.md
```

### 1.2 Configuration

**File:** `config/settings.py`

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

"compiled_kb_file": {

"enabled": True,

"source_file": "kb.comindware.ru.platform_v5_for_llm_ingestion.md"

},

"compiled_md_folder": {

"enabled": True,

"source_folder": "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"

}

},

"chunk_size": 700,

"chunk_overlap": 300,

"min_chunk_size": 100,

### To-dos

- [ ] Create mkdocs_for_rag_indexing.yml config inheriting from complete guide config
- [ ] Create rag_indexing_hook.py to export Jinja2-compiled markdown (similar to kb_html_cleanup_hook.py)
- [ ] Create rag_engine/ project structure and copy LLM manager from cmw-platform-agent
- [ ] Implement config/settings.py with 3 input modes (mkdocs_pipeline, compiled_kb_file, compiled_md_folder)
- [ ] Implement document processor supporting 3 input modes with frontmatter parsing and markdown extraction
- [ ] Implement semantic chunker (700 tokens, 300 overlap) with section-based splitting and code preservation
- [ ] Implement metadata enricher for content-based, structural, and search optimization metadata
- [ ] Implement FRIDA embedding generator with prefix support (search_query, search_document, categorize_topic, paraphrase)
- [ ] Implement ChromaDB vector store with rich metadata support and persistence
- [ ] Implement vector retriever with article reconstruction and metadata filtering
- [ ] Implement cross-encoder reranker with metadata boosting (mmarco-mMiniLMv2)
- [ ] Integrate multi-LLM manager from cmw-platform-agent with streaming support
- [ ] Implement response formatter with citations (URLs + section anchors)
- [ ] Create build_mkdocs_for_rag.sh and build_index.py for all 3 input modes
- [ ] Implement Gradio interface with streaming, source display, and LLM selection
- [ ] Create test_queries.py with Russian/English test cases
- [ ] Write comprehensive README with all 3 input modes, usage examples, and deployment guide