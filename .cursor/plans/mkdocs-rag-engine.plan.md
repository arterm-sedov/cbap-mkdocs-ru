<!-- cef902af-b944-421b-b9d0-9c1ef7737ea1 24f7a203-e358-4d7e-bd48-ec302c2dcaaf -->
# MkDocs RAG Engine Implementation Plan

## Overview

Build a production-ready RAG (Retrieval-Augmented Generation) engine for the MkDocs documentation repository that handles Jinja2-rich source files through MkDocs build pipeline integration. Uses FRIDA (best Russian embedder), ChromaDB vector store, cross-encoder reranking, and multi-LLM support with streaming responses.

## Reference repos & docs

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
         Metadata Enricher (rich metadata + optional LLM enhancement)
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

**Problem:** Raw MkDocs files contain Jinja2 syntax (`{{ productName }}`, `{% if %}`, etc.) that cannot be indexed directly.

**Solution:** Create custom MkDocs config + hook to export Jinja2-compiled markdown before indexing.

#### File 1: `mkdocs_for_rag_indexing.yml`

```yaml
# Inherit from complete guide config to resolve all Jinja2 variables
INHERIT: mkdocs_guide_complete_ru.yml

# Override output directory for RAG-compiled markdown
site_dir: compiled_md_for_rag

# Add custom hook for RAG export
hooks:
 - rag_indexing_hook.py

# Disable unnecessary plugins (we only need compiled MD)
plugins:
 - search: false
 - with-pdf: !ENV [DISABLE_PDF, true]

# Keep all other settings from parent config
```

#### File 2: `rag_indexing_hook.py`

```python
"""
MkDocs hook to export Jinja2-compiled markdown for RAG indexing.
Inspired by kb_html_cleanup_hook.py but outputs clean compiled MD files.

This hook captures markdown AFTER Jinja2 processing but BEFORE HTML conversion,
giving us clean, variable-resolved content ready for RAG indexing.
"""

import json
import os
from datetime import datetime
from pathlib import Path
import yaml


def on_page_markdown(markdown, page, config, files):
    """
    Called AFTER Jinja2 template processing but BEFORE markdown→HTML conversion.
    At this point, all {{ variables }} and {% blocks %} are fully resolved.
    """
    # Store the compiled markdown for later use
    page._compiled_md_for_rag = markdown
    return markdown


def on_post_page(output, page, config):
    """
    After page HTML is built, save the compiled markdown to RAG folder.
    """
    # Get the Jinja2-resolved markdown
    compiled_md = getattr(page, '_compiled_md_for_rag', page.markdown)
    
    # Prepare output path (mirrors source structure)
    output_dir = Path(config['site_dir'])
    rel_path = Path(page.file.src_path)
    output_file = output_dir / rel_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save compiled markdown with frontmatter preserved
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write frontmatter (includes kbId, title, tags, url, etc.)
        if page.meta:
            f.write('---\n')
            yaml.dump(page.meta, f, allow_unicode=True, default_flow_style=False)
            f.write('---\n\n')
        
        # Write Jinja2-resolved markdown content
        f.write(compiled_md)
    
    return output


def on_post_build(config):
    """
    After build completes, create manifest file for RAG indexer.
    """
    output_dir = Path(config['site_dir'])
    manifest_file = output_dir / 'rag_manifest.json'
    
    # Collect all compiled .md files
    md_files = sorted(output_dir.rglob('*.md'))
    
    manifest = {
        'total_files': len(md_files),
        'files': [str(f.relative_to(output_dir)) for f in md_files],
        'build_date': datetime.now().isoformat(),
        'config_name': config.get('site_name'),
        'docs_dir': config['docs_dir'],
        'source_type': 'mkdocs_pipeline'
    }
    
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ RAG Export: {len(md_files)} compiled MD files → {output_dir}")
    print(f"   Manifest: {manifest_file}")
```

**Usage:**

```bash
# Build compiled markdown for RAG indexing
mkdocs build -f mkdocs_for_rag_indexing.yml

# Output: compiled_md_for_rag/ folder with:
#   - Jinja2-resolved .md files (all {{ variables }} replaced)
#   - rag_manifest.json (metadata about exported files)
```

### 1.1 Project Structure

Create standalone RAG service under `rag_engine/`:

```
rag_engine/
├── config/
│   ├── __init__.py
│   ├── settings.py          # Configuration with 3 input modes
│   └── input_modes.py       # Input mode handlers
├── core/
│   ├── __init__.py
│   ├── document_processor.py   # Supports 3 input modes
│   ├── chunker.py              # Smart text splitting
│   ├── metadata_enricher.py    # Metadata extraction
│   └── vector_store.py         # ChromaDB operations
├── llm/
│   ├── __init__.py
│   ├── llm_manager.py       # From cmw-platform-agent
│   ├── provider_adapters.py # From cmw-platform-agent
│   ├── langsmith_config.py  # From cmw-platform-agent
│   └── langfuse_config.py   # From cmw-platform-agent
├── retrieval/
│   ├── __init__.py
│   ├── embedder.py          # FRIDA with 4 prefixes
│   ├── retriever.py         # Vector search
│   └── reranker.py          # Cross-encoder
├── tools/
│   ├── __init__.py
│   ├── pdf_utils.py         # From cmw-platform-agent
│   └── file_utils.py        # From cmw-platform-agent
├── api/
│   ├── __init__.py
│   ├── app.py               # Gradio interface
│   └── models.py            # Request/response models
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── helpers.py
├── scripts/
│   ├── build_mkdocs_for_rag.sh  # Complete build pipeline
│   ├── build_index.py           # Index builder (3 modes)
│   └── test_queries.py          # Testing
├── requirements.txt
├── .env.example
└── README.md
```

**Copy from existing repos:**

- `llm/` modules from `cmw-platform-agent/agent_ng/`
- `tools/` from `cmw-platform-agent/tools/`
- Patterns from `agent-course-final-assignment/setup_vector_store.py`
- Architecture wisdom from `deepwiki-open`

### 1.2 Configuration Management

**File:** `config/settings.py`

```python
INDEXING_CONFIG = {
    # Three input modes to handle different source formats
    "input_modes": {
        "mkdocs_pipeline": {
            "enabled": True,
            "mkdocs_config": "mkdocs_for_rag_indexing.yml",
            "output_dir": "compiled_md_for_rag/",
            "hook_file": "rag_indexing_hook.py",
            "manifest_file": "rag_manifest.json",
            "description": "Build via MkDocs to resolve Jinja2 variables"
        },
        "compiled_kb_file": {
            "enabled": True,
            "source_file": "kb.comindware.ru.platform_v5_for_llm_ingestion.md",
            "description": "Single pre-compiled KB file (all articles merged)"
        },
        "compiled_md_folder": {
            "enabled": True,
            "source_folder": "phpkb_content/798. Версия 5.0. Текущая рекомендованная/",
            "description": "Folder of compiled MD files (phpkb or MkDocs output)"
        }
    },
    "chunk_size": 700,           # tokens
    "chunk_overlap": 300,        # tokens
    "min_chunk_size": 100,
}

EMBEDDING_CONFIG = {
    "model_name": "ai-forever/FRIDA",  # State-of-the-art Russian embedder
    "device": "auto",  # Auto-detect CPU/GPU
    "batch_size": "auto",  # 8 for CPU, 32 for GPU (auto-detected)
    "embedding_dim": 768,
    "max_seq_length": 512,
    "prefixes": {
        "documents": "search_document:",     # For indexing
        "queries": "search_query:",          # For user queries
        "categorization": "categorize_topic:",  # For article grouping
        "paraphrase": "paraphrase:"          # For finding similar sections
    }
}

RERANKER_CONFIG = {
    "model_name": "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1",  # Multilingual
    "top_k_retrieve": 20,    # From vector search
    "top_k_rerank": 5,       # After reranking
    "batch_size": 16,
}

CHROMADB_CONFIG = {
    "persist_directory": "./chromadb_data",
    "collection_name": "mkdocs_kb",
    "distance_function": "cosine",
}
```

## Phase 2: Document Processing Pipeline

### 2.1 Document Processor (3 Input Modes)

**File:** `core/document_processor.py`

**Supports three input modes:**

1. **MkDocs Pipeline Mode**: Read from `compiled_md_for_rag/` after MkDocs build with hook
2. **Compiled KB File Mode**: Parse single `kb.comindware.ru.platform_v5_for_llm_ingestion.md`
3. **Compiled MD Folder Mode**: Process `phpkb_content/798...` or any MD folder

**Key features:**

- Parse YAML frontmatter (kbId, title, tags, url) from compiled files
- Extract markdown structure (headings with anchors, code blocks, lists)
- Handle MkDocs syntax (admonitions, etc.) - already resolved by build
- Detect content features (code presence, languages, entities)

**Implementation:**

```python
class DocumentProcessor:
    def __init__(self, input_mode: str, config: dict):
        self.input_mode = input_mode
        self.config = config
        
    def process_all(self) -> List[Document]:
        """Process documents based on input mode"""
        if self.input_mode == "mkdocs_pipeline":
            return self._process_mkdocs_output()
        elif self.input_mode == "compiled_kb_file":
            return self._process_kb_file()
        elif self.input_mode == "compiled_md_folder":
            return self._process_md_folder()
    
    def _process_mkdocs_output(self) -> List[Document]:
        """Process MkDocs build output using manifest"""
        output_dir = Path(self.config["output_dir"])
        manifest_path = output_dir / self.config["manifest_file"]
        manifest = json.load(open(manifest_path))
        
        documents = []
        for file_path in manifest["files"]:
            doc = self._parse_md_file(output_dir / file_path)
            documents.append(doc)
        
        return documents
    
    def _parse_md_file(self, file_path: Path) -> Document:
        """Parse single markdown file with frontmatter and structure"""
        # Parse frontmatter + markdown
        # Extract headings, anchors, code blocks
        # Return structured Document object
        pass
```

**Example output structure:**

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
        },
        {
            "heading": "Настройка вычисления",
            "anchor": "#example_n3_calculate_active_task_accounts_configure",
            "level": 2,
            "content": "...",
            "has_code": True,
            "code_blocks": [{"language": "turtle", "content": "..."}]
        }
    ]
}
```

### 2.2 Smart Text Chunker

**File:** `core/chunker.py`

Implement semantic chunking with these strategies:

1. **Section-based chunking**: Respect markdown heading boundaries
2. **Token-aware splitting**: Use LangChain's `RecursiveCharacterTextSplitter` with token counting
3. **Overlap with context preservation**: 300-token overlap including heading context
4. **Code block preservation**: Never split code blocks across chunks
5. **Metadata inheritance**: Each chunk inherits parent section metadata

**Key decisions:**

- Chunk size: 700 tokens (proven effective in `rag_agent/search-assistant.py`)
- Overlap: 300 tokens (maintains context)
- Token counter: `tiktoken` (OpenAI-compatible)

**Example chunk structure:**

```python
{
    "chunk_id": "4966_chunk_002",
    "content": "...",  # ~700 tokens
    "metadata": {
        "kbId": "4966",
        "url": "https://kb.comindware.ru/article.php?id=4966",
        "title": "Вычисление пользователей с активными задачами",
        "section_heading": "Настройка вычисления",
        "section_anchor": "#example_n3_calculate_active_task_accounts_configure",
        "chunk_index": 2,
        "total_chunks": 5,
        "has_code": True,
        "tags": ["N3", "Notation 3", "RDF", ...],
        "article_path": "docs/ru/examples/n3_calculate_active_task_accounts.md",
        "language": "ru"
    }
}
```

### 2.3 Metadata Enricher

**File:** `core/metadata_enricher.py`

**Important Design Note:** Use lean parsing without LLM for basic metadata extraction. Use an LLM and cmw-platform-agent mechanics if needed to fetch or synthesize more sophisticated metadata to avoid if-then-else hardcode.

Also consider a utility to go through the MkDocs files and enrich them with the RAG metadata. This might save compute and tokens during subsequent RAG indexing runs, as most metadata will already be present in the MkDocs files.

Reference: https://github.com/arterm-sedov/cmw-platform-agent/tree/main/agent_ng

**Enhance chunks with computed metadata for better retrieval and reranking:**

1. **Content-based metadata:**

                        - `has_code`: Boolean indicating code presence
                        - `code_languages`: List of programming languages in chunk
                        - `entity_types`: Detected entities (attribute names, template names, etc.)
                        - `complexity_score`: Heuristic based on content (0-1)

2. **Structural metadata:**

                        - `section_depth`: Heading level (H1=1, H2=2, etc.)
                        - `position_in_article`: Relative position (intro/body/conclusion)
                        - `related_sections`: Adjacent section anchors. Take from the article's footer and hyperlinks in the article where possible, deduplicate.

3. **Search optimization metadata:**

                        - `keywords`: Extracted key terms (from tags + content)
                        - `summary`: LLM-generated summary of the chunk (optional, for better retrieval)
                        - `char_count`: Length for filtering

## Phase 3: FRIDA Embeddings & ChromaDB

### 3.1 FRIDA Embedding Generator

**File:** `retrieval/embedder.py`

**Why FRIDA is the best choice:**

- **Best-in-class performance:** 62.18 avg score on ruMTEB benchmark (vs 58.42 for ru-en-RoSBERTa)
- **Superior Russian-English bilingual support:** Fine-tuned on 4M+ Russian-English pairs
- **Advanced task-specific prefixes:** 4 specialized modes vs 3 in other models
- **Larger model capacity:** 0.8B parameters for richer semantic representations
- **OpenAI-compatible:** 768-dimensional embeddings work with all standard vector databases
- **CPU-friendly:** Works efficiently on CPU-only deployments (100-200ms per query)

**FRIDA's Advanced Prefix System:**

1. `search_query:` + `search_document:` - For retrieval tasks
2. `paraphrase:` - For finding similar documentation sections
3. `categorize_topic:` - Perfect for grouping articles by technical domain (N3, deployment, API, etc.)
4. `categorize:` - General categorization tasks

**Implementation:**

```python
from sentence_transformers import SentenceTransformer
import torch

class EmbeddingGenerator:
    def __init__(self, config: dict):
        # Auto-detect device
        device = config.get("device", "auto")
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.model = SentenceTransformer("ai-forever/FRIDA", device=device)
        self.model.max_seq_length = 512  # FRIDA's max length
        
        # Auto-detect batch size
        batch_size = config.get("batch_size", "auto")
        if batch_size == "auto":
            self.batch_size = 32 if device == "cuda" else 8
        else:
            self.batch_size = batch_size
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed documents with search_document prefix"""
        return self.model.encode(
            texts,
            prompt_name="search_document",
            batch_size=self.batch_size,
            show_progress_bar=True,
            normalize_embeddings=True
        )
    
    def embed_query(self, query: str) -> List[float]:
        """Embed query with search_query prefix"""
        return self.model.encode(
            query,
            prompt_name="search_query",
            normalize_embeddings=True
        )
    
    def embed_for_categorization(self, texts: List[str]) -> List[List[float]]:
        """Use categorize_topic prefix for article grouping"""
        return self.model.encode(
            texts,
            prompt_name="categorize_topic",
            batch_size=self.batch_size,
            normalize_embeddings=True
        )
    
    def embed_for_paraphrase(self, texts: List[str]) -> List[List[float]]:
        """Use paraphrase prefix for finding similar sections"""
        return self.model.encode(
            texts,
            prompt_name="paraphrase",
            batch_size=self.batch_size,
            normalize_embeddings=True
        )
```

**CPU Performance:**

- Single query: 100-200ms
- Full indexing (500 docs, ~2000 chunks): 15-20 minutes
- Acceptable for production use

### 3.2 ChromaDB Vector Store

**File:** `core/vector_store.py`

**Inspiration from:**

- `agent-course-final-assignment/setup_vector_store.py` - Initialization patterns
- `deepwiki-open` - Collection management and query strategies (very robust repo)

**Implementation:**

```python
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    persist_directory="./chromadb_data",
    anonymized_telemetry=False
))

collection = client.get_or_create_collection(
    name="mkdocs_kb",
    metadata={"description": "Comindware Platform documentation"},
    embedding_function=None  # We provide embeddings directly
)

# Index with rich metadata
collection.add(
    ids=chunk_ids,           # ["4966_chunk_001", ...]
    embeddings=embeddings,    # List[List[float]] from FRIDA
    documents=chunk_texts,    # List[str]
    metadatas=chunk_metadata  # List[Dict] - ALL our rich metadata
)

# Query with metadata filtering
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=20,
    where={"language": "ru"},  # Optional filtering
    include=["documents", "metadatas", "distances"]
)
```

**Advanced features:**

- Incremental updates (add without rebuilding)
- Metadata filtering during search
- Distance threshold filtering
- Deduplication by kbId

## Phase 4: Retrieval & Cross-Encoder Reranking

### 4.1 Vector Retriever

**File:** `retrieval/retriever.py`

**Query pipeline:**

1. Embed query with FRIDA (`search_query` prefix)
2. Search ChromaDB (top-20)
3. Group chunks by article (kbId)
4. Reconstruct full articles
5. Prepare context for reranking

**Article reconstruction:**

```python
def reconstruct_articles(chunks: List[Dict]) -> List[Dict]:
    """Group chunks by article and reconstruct full content"""
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
    
    # Sort chunks within each article
    for article in articles.values():
        article["chunks"].sort(key=lambda c: c["metadata"]["chunk_index"])
    
    return list(articles.values())
```

### 4.2 Cross-Encoder Reranker

**File:** `retrieval/reranker.py`

**What is Cross-Encoder Reranking?**

Unlike bi-encoders (which encode query and documents separately), cross-encoders jointly encode the query-document pair, producing a direct relevance score. This provides higher accuracy at the cost of computational overhead.

**Architecture:**

```
Query + Document → Cross-Encoder → Relevance Score (0-1)
```

**Why it's better:**

- Captures semantic relationships between query and document
- Understands negation, nuance, and context
- Produces calibrated relevance scores
- Significantly improves top-k accuracy

**Implementation:**

```python
from sentence_transformers import CrossEncoder
import numpy as np

# Use multilingual cross-encoder
reranker = CrossEncoder('cross-encoder/mmarco-mMiniLMv2-L12-H384-v1')

def rerank_with_metadata(
    query: str,
    articles: List[Dict],
    reranker: CrossEncoder,
    top_k: int = 5
) -> List[Dict]:
    """Rerank articles using cross-encoder + metadata signals"""
    
    # Prepare query-document pairs
    pairs = []
    for article in articles:
        article_text = " ".join([c["content"] for c in article["chunks"][:3]])
        pairs.append([query, article_text])
    
    # Get cross-encoder scores
    scores = reranker.predict(pairs)
    
    # Apply metadata boosting
    for i, article in enumerate(articles):
        base_score = scores[i]
        boost = 1.0
        
        # Title/tag match boost
        if query_matches_tags(query, article["metadata"]["tags"]):
            boost *= 1.2
        
        # Code presence boost
        if query_is_about_code(query) and article["metadata"].get("has_code"):
            boost *= 1.15
        
        # Section relevance boost
        if article["metadata"]["section_heading"]:
            if query_matches_heading(query, article["metadata"]["section_heading"]):
                boost *= 1.1
        
        scores[i] = base_score * boost
    
    # Return top-k
    ranked_indices = np.argsort(scores)[::-1][:top_k]
    return [articles[i] for i in ranked_indices]
```

## Phase 5: Multi-LLM Integration

### 5.1 LLM Manager

**Files to copy from `cmw-platform-agent/agent_ng/`:**

- `llm_manager.py` (complete)
- `provider_adapters.py` (complete)
- `langsmith_config.py` (complete)
- `langfuse_config.py` (complete)
- `utils.py` (functions used by llm_manager)

**Configure in `.env`:**

```env
GOOGLE_API_KEY=...
GROQ_API_KEY=...
OPENROUTER_API_KEY=...
MISTRAL_API_KEY=...
DEFAULT_LLM_PROVIDER=gemini
DEFAULT_MODEL=gemini-1.5-flash
```

**Usage:**

```python
from llm.llm_manager import LLMManager

llm_manager = LLMManager()
llm = llm_manager.get_llm("gemini", use_tools=False)

# Stream response
for chunk in llm.stream(messages):
    yield chunk.content
```

### 5.2 Prompt Engineering

**System prompt:**

```python
SYSTEM_PROMPT = """You are a technical documentation assistant for Comindware Platform.

Your role:
- Answer questions based ONLY on the provided documentation context
- Cite sources using the format: [Article Title](URL#anchor)
- If information is not in the context, clearly state this
- Provide code examples when relevant
- Answer in the same language as the question (Russian or English)

Context provided:
{context}

Instructions:
- Use specific article URLs for citations
- Include section anchors when referencing specific parts
- Format code blocks with proper syntax highlighting
- Be concise but comprehensive
"""
```

**Response formatting:**

```python
def format_response_with_citations(answer: str, articles: List[Dict]) -> str:
    citations = "\n\n## Sources:\n\n"
    for i, article in enumerate(articles, 1):
        citations += f"{i}. [{article['title']}]({article['url']})\n"
        for chunk in article["chunks"]:
            section = chunk["metadata"].get("section_heading")
            anchor = chunk["metadata"].get("section_anchor")
            if section and anchor:
                citations += f"   - Section: [{section}]({article['url']}{anchor})\n"
    return answer + citations
```

## Phase 6: Gradio Web Interface

**File:** `api/app.py`

```python
import gradio as gr

def query_rag_system(
    question: str,
    llm_provider: str,
    top_k: int = 5,
    progress=gr.Progress()
):
    progress(0, desc="Embedding query...")
    query_embedding = embedder.embed_query(question)
    
    progress(0.2, desc="Searching documentation...")
    initial_results = vector_store.search(query_embedding, top_k=20)
    
    progress(0.4, desc="Reranking results...")
    articles = retriever.reconstruct_articles(initial_results)
    reranked_articles = reranker.rerank_with_metadata(question, articles, top_k=top_k)
    
    progress(0.6, desc="Generating answer...")
    context = format_context(reranked_articles)
    
    # Stream response
    answer = ""
    for chunk in llm_manager.stream_response(question, context, llm_provider):
        answer += chunk
        yield answer
    
    # Add citations
    final_response = format_response_with_citations(answer, reranked_articles)
    yield final_response

demo = gr.Interface(
    fn=query_rag_system,
    inputs=[
        gr.Textbox(label="Question", placeholder="Как использовать N3 выражения?"),
        gr.Dropdown(["gemini", "groq", "openrouter"], label="LLM Provider", value="gemini"),
        gr.Slider(1, 10, value=5, step=1, label="Number of sources")
    ],
    outputs=gr.Markdown(label="Answer with Citations"),
    title="Comindware Platform Documentation Assistant",
    description="Ask questions about Comindware Platform documentation",
    examples=[
        ["Как создать вычисляемый атрибут?", "gemini", 5],
        ["Что такое N3 выражения?", "gemini", 5],
        ["How to configure email connections?", "gemini", 5]
    ],
    allow_flagging="never"
)

demo.queue().launch(server_name="0.0.0.0", server_port=7860, share=False)
```

## Phase 7: Build Scripts

### 7.1 Complete Build Script

**File:** `scripts/build_mkdocs_for_rag.sh`

```bash
#!/bin/bash
# Complete RAG indexing from MkDocs sources

echo "📚 Building RAG index from MkDocs sources..."

# Step 1: Build MkDocs with RAG hook
echo "1️⃣  Building MkDocs (resolving Jinja2)..."
mkdocs build -f mkdocs_for_rag_indexing.yml

# Step 2: Index compiled markdown
echo "2️⃣  Indexing compiled markdown..."
python scripts/build_index.py \
  --source compiled_md_for_rag/ \
  --mode mkdocs_pipeline

echo "✅ RAG indexing complete!"
```

### 7.2 Index Builder

**File:** `scripts/build_index.py`

```python
import argparse

def build_index(source: str, mode: str, rebuild: bool = False):
    """
    Build vector index from source.
    
    Modes:
  - mkdocs_pipeline: Read from compiled_md_for_rag/
  - compiled_kb_file: Read single KB file
  - compiled_md_folder: Read folder of MD files
    """
    processor = DocumentProcessor(mode, config)
    documents = processor.process_all()
    
    chunker = Chunker(config)
    chunks = chunker.create_chunks(documents)
    
    enricher = MetadataEnricher(config)
    enriched = enricher.enrich(chunks)
    
    embedder = EmbeddingGenerator(config)
    embeddings = embedder.embed_documents([c["content"] for c in enriched])
    
    vector_store = VectorStore(config)
    vector_store.add_documents(enriched, embeddings, rebuild=rebuild)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--mode", choices=["mkdocs_pipeline", "compiled_kb_file", "compiled_md_folder"])
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    
    build_index(args.source, args.mode, args.rebuild)
```

**Usage examples:**

```bash
# Option 1: MkDocs pipeline (recommended)
./scripts/build_mkdocs_for_rag.sh

# Option 2: Pre-compiled KB file
python scripts/build_index.py \
  --source kb.comindware.ru.platform_v5_for_llm_ingestion.md \
  --mode compiled_kb_file

# Option 3: Compiled MD folder
python scripts/build_index.py \
  --source "phpkb_content/798. Версия 5.0. Текущая рекомендованная/" \
  --mode compiled_md_folder

# Rebuild from scratch
python scripts/build_index.py --source docs/ru/ --mode mkdocs_pipeline --rebuild
```

## Phase 8: Deployment

### 8.1 Requirements

**File:** `requirements.txt`

```txt
# Core dependencies
chromadb>=0.4.22
sentence-transformers>=2.2.2
langchain>=0.1.0
langchain-text-splitters>=0.0.1
tiktoken>=0.5.2

# LLM providers (from cmw-platform-agent)
langchain-google-genai>=0.0.5
langchain-groq>=0.0.1
langchain-huggingface>=0.0.1
langchain-mistralai>=0.0.1
langchain-openai>=0.0.5

# File processing
pymupdf4llm>=0.0.3
python-docx>=0.8.11
openpyxl>=3.1.0
pandas>=2.0.0

# Web interface
gradio>=4.0.0

# Utilities
python-dotenv>=1.0.0
pyyaml>=6.0
pydantic>=2.5.0
numpy>=1.24.0
tqdm>=4.66.0

# Optional: Observability
langsmith>=0.0.70
langfuse>=2.0.0
```

### 8.2 Environment Configuration

**File:** `.env.example`

```env
# === Embedding Configuration ===
EMBEDDING_MODEL=ai-forever/FRIDA
# Best-in-class Russian embedder with advanced prefix system

# === LLM Provider Keys ===
GOOGLE_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here

# === RAG Configuration ===
DEFAULT_LLM_PROVIDER=gemini
CHUNK_SIZE=700
CHUNK_OVERLAP=300
TOP_K_RETRIEVE=20
TOP_K_RERANK=5

# === ChromaDB Configuration ===
CHROMADB_PERSIST_DIR=./chromadb_data
CHROMADB_COLLECTION=mkdocs_kb

# === Reranker Configuration ===
RERANKER_MODEL=cross-encoder/mmarco-mMiniLMv2-L12-H384-v1

# === Observability (Optional) ===
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=mkdocs-rag

LANGFUSE_TRACING=false
LANGFUSE_SECRET_KEY=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_HOST=https://cloud.langfuse.com

# === Web Interface ===
GRADIO_SERVER_NAME=0.0.0.0
GRADIO_SERVER_PORT=7860
GRADIO_SHARE=false
```

### 8.3 Docker Deployment

**File:** `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download FRIDA embedding model
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('ai-forever/FRIDA')"

EXPOSE 7860

CMD ["python", "api/app.py"]
```

**Nginx reverse proxy:**

```nginx
location /rag/ {
    proxy_pass http://localhost:7860/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## Key Technical Decisions

### Embedding Model: ai-forever/FRIDA

**Rationale:** State-of-the-art Russian embedder (62.18 ruMTEB score vs 58.42 for RoSBERTa), advanced 4-prefix system (search_query, search_document, categorize_topic, paraphrase), 0.8B parameters for richer semantics, OpenAI-compatible 768-dim vectors, CPU-friendly (100-200ms per query)

### Input Strategy: 3 Modes with MkDocs Integration

**Rationale:** MkDocs files contain Jinja2 syntax that must be resolved before indexing. Custom hook exports compiled markdown. Alternative modes (compiled KB file, compiled MD folder) provide flexibility.

### Vector Database: ChromaDB

**Rationale:** Purpose-built for RAG, excellent metadata support, easy self-hosting, persistent storage, no external dependencies

### Chunking: 700 tokens / 300 overlap

**Rationale:** Proven effective in existing `rag_agent/search-assistant.py`, balances context size with retrieval precision

### Reranking: Cross-encoder with metadata boosting

**Rationale:** Significantly improves relevance over vector similarity alone, metadata boosting leverages rich document structure

### LLM Management: Multi-provider with fallback

**Rationale:** Flexibility for different use cases, proven architecture from `cmw-platform-agent`, easy to extend

### Retrieval Pipeline: Vector search → Rerank → Article reconstruction

**Rationale:** Fast initial retrieval, accurate reranking, complete article context for LLM

## Success Metrics

- **Indexing speed:** < 20 min for full docs/ru/ (~500 documents) on CPU
- **Query latency:** < 3 seconds end-to-end (including LLM generation)
- **Retrieval accuracy:** Top-5 results include correct answer > 90% of time
- **Citation accuracy:** All citations link to correct articles and sections

## Next Steps After Implementation

1. **Evaluation:** Create test set of 50 questions with ground truth answers
2. **Fine-tuning:** Adjust chunk size, overlap, top-k based on evaluation results
3. **Monitoring:** Implement query logging and analytics
4. **Continuous improvement:** Add user feedback loop for relevance scoring
5. **Integration:** Connect to existing MkDocs build pipeline for automatic reindexing

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