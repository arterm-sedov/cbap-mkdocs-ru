<!-- cef902af-b944-421b-b9d0-9c1ef7737ea1 73ae2715-1323-4847-a179-189d9c6ba51a -->
#  MkDocs RAG Engine Implementation Plan

## Architecture Overview

The RAG engine follows a modern retrieval-augmented generation architecture with these key components:

```
MkDocs Source Files (*.md)
    ↓
[1] Document Processor (frontmatter + markdown parsing)
    ↓
[2] Smart Text Splitter (semantic chunking with overlap)
    ↓
[3] Metadata Enricher (kbId, URL, tags, section anchors)
    ↓
[4] Embedding Generator (multilingual Russian-English models)
    ↓
[5] ChromaDB Vector Store (persistent, with rich metadata)
    ↓
[6] Query Pipeline:
    → Embed user query
    → Vector search (top-k=20)
    → Cross-encoder reranking (top-k=5)
    → Article reconstruction from chunks
    → Feed to multi-LLM manager
    → Stream response with citations
```

## Implementation Steps

### Phase 1: Project Structure and Core Components

#### 1.1 Create Project Structure

Create a new standalone RAG service under `rag_engine/`:

```
rag_engine/
├── config/
│   ├── __init__.py
│   ├── settings.py          # Configuration management
│   └── embeddings.yaml      # Embedding model configs
├── core/
│   ├── __init__.py
│   ├── document_processor.py   # Frontmatter + markdown parsing
│   ├── chunker.py              # Smart text splitting
│   ├── metadata_enricher.py    # Metadata extraction & enrichment
│   └── vector_store.py         # ChromaDB operations
├── llm/
│   ├── __init__.py
│   ├── llm_manager.py       # Borrowed from cmw-platform-agent
│   ├── provider_adapters.py # Borrowed from cmw-platform-agent
│   ├── langsmith_config.py  # Borrowed from cmw-platform-agent
│   └── langfuse_config.py   # Borrowed from cmw-platform-agent
├── retrieval/
│   ├── __init__.py
│   ├── embedder.py          # Embedding generation
│   ├── retriever.py         # Vector search operations
│   └── reranker.py          # Cross-encoder reranking
├── tools/
│   ├── __init__.py
│   ├── pdf_utils.py         # Borrowed from cmw-platform-agent
│   └── file_utils.py        # Borrowed from cmw-platform-agent
├── api/
│   ├── __init__.py
│   ├── app.py               # FastAPI or Gradio interface
│   └── models.py            # Request/response models
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── helpers.py
├── scripts/
│   ├── build_index.py       # Index building script
│   └── test_queries.py      # Testing script
├── requirements.txt
├── .env.example
└── README.md
```

**Reference repos**:

https://github.com/AsyncFuncAI/deepwiki-open

https://github.com/arterm-sedov/cmw-platform-agent

https://github.com/arterm-sedov/agent-course-final-assignment

**Reuse from existing repos:**

- `llm/` - Copy entire LLM manager module from `cmw-platform-agent/agent_ng/llm_manager.py` and dependencies
- `tools/pdf_utils.py` & `file_utils.py` - Copy from `cmw-platform-agent/tools/`

#### 1.2 Configuration Management

Create `config/settings.py` with these configurable parameters:

```python
INDEXING_CONFIG = {
    "source_options": [
        "docs/ru/**/*.md",  # Full MkDocs repo
        "phpkb_content/798. Версия 5.0. Текущая рекомендованная/**/*.md",
        "kb.comindware.ru.platform_v5_for_llm_ingestion.md"  # Pre-compiled KB
    ],
    # USE ONE OF THESE, not all at once, they are mostly duplicate.
    # But support the MD files and the combined KB comipled file 
    "chunk_size": 700,           # tokens
    "chunk_overlap": 300,        # tokens
    "min_chunk_size": 100,
}

EMBEDDING_CONFIG = {
    "model_name": "ai-forever/FRIDA",  # State-of-the-art Russian embedder
    "device": "cpu",  # or "cuda" if GPU available. Autodetect if possible
    "batch_size": 8,   # Optimized for CPU (use 32 for GPU). Autodetect if possible
    "embedding_dim": 768,
    "max_seq_length": 512,
}

RERANKER_CONFIG = {
    "model_name": "cross-encoder/ms-marco-MiniLM-L-12-v2",
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

### Phase 2: Document Processing Pipeline

#### 2.1 Document Processor (Inspired by deepwiki-open)

**File:** `core/document_processor.py`

Key features:

- Parse YAML frontmatter (kbId, title, tags, url)
- Extract markdown structure (headings, code blocks, lists)
- Preserve anchors from headings (e.g., `{: #section_anchor }`)
- Handle MkDocs-specific syntax (admonitions, snippets)
- Support multiple input formats (individual .md files, folders, pre-compiled KB)

**Reuse from existing code:**

- Document scanning pattern from `rag_agent/search-assistant.py` (recursive .md file finding)
- File reading utilities from `cmw-platform-agent/tools/file_utils.py`

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

#### 2.2 Smart Text Chunker (Based on deepwiki-open strategy)

**File:** `core/chunker.py`

Implement semantic chunking with these strategies:

1. **Section-based chunking:** Respect markdown heading boundaries
2. **Token-aware splitting:** Use LangChain's `RecursiveCharacterTextSplitter` with token counting
3. **Overlap with context preservation:** 300-token overlap that includes heading context
4. **Code block preservation:** Never split code blocks across chunks
5. **Metadata inheritance:** Each chunk inherits parent section metadata

**Key decisions:**

- Primary chunk size: 700 tokens (as tested in existing `rag_agent/search-assistant.py`)
- Overlap: 300 tokens (proven effective)
- Use `tiktoken` for OpenAI-compatible token counting

**Example chunk structure:**

```python
{
    "chunk_id": "4966_chunk_002",
    "content": "...",  # Actual text with ~700 tokens
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

#### 2.3 Metadata Enricher

**File:** `core/metadata_enricher.py`

Enhance chunks with computed metadata for better retrieval and reranking:

1. **Content-based metadata:**

   - `has_code`: Boolean indicating code presence
   - `code_languages`: List of programming languages in chunk
   - `entity_types`: Detected entities (attribute names, template names, etc.)
   - `complexity_score`: Heuristic based on content (0-1)

2. **Structural metadata:**

   - `section_depth`: Heading level (H1=1, H2=2, etc.)
   - `position_in_article`: Relative position (intro/body/conclusion)
   - `related_sections`: Adjacent section anchors

3. **Search optimization metadata:**

   - `keywords`: Extracted key terms (from tags + content)
   - `summary`: First 2-3 sentences of chunk
   - `char_count`: Length for filtering

### Phase 3: Embedding and Vector Store

#### 3.1 Embedding Generator

**File:** `retrieval/embedder.py`

Implement multilingual embedding with fallback options:

**Primary model:** `ai-forever/FRIDA` (state-of-the-art Russian embedder)

**Why FRIDA is the best choice:**

- **Best-in-class performance:** 62.18 avg score on ruMTEB benchmark (vs 58.42 for ru-en-RoSBERTa)
- **Superior Russian-English bilingual support:** Fine-tuned on 4M+ Russian-English pairs
- **Advanced task-specific prefixes:** 4 specialized modes vs 3 in other models
- **Larger model capacity:** 0.8B parameters for richer semantic representations
- **OpenAI-compatible:** 768-dimensional embeddings work with all standard vector databases
- **CPU-friendly:** Works efficiently on CPU-only deployments (100-200ms per query)

**FRIDA's Advanced Prefix System:**

1. `search_query:` + `search_document:` - For retrieval tasks (standard)
2. `paraphrase:` - For finding similar documentation sections (better than generic "classification")
3. `categorize_topic:` - Perfect for grouping articles by technical domain (N3, deployment, API, etc.)
4. `categorize:` - General categorization tasks

**Key features:**

- Task-optimized embeddings via prefix selection
- Batch processing optimized for CPU/GPU
- Normalized embeddings by default
- Memory efficient: ~3-4GB RAM on CPU
- Full compatibility with ChromaDB and OpenAI-like vector databases

**Implementation with FRIDA's prefix support:**

```python
from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name: str = "ai-forever/FRIDA", device: str = "cpu"):
        """
        Initialize FRIDA embedder with optional CPU/GPU device selection.
        FRIDA works efficiently on CPU-only systems (100-200ms per query).
        """
        self.model = SentenceTransformer(model_name, device=device)
        self.model.max_seq_length = 512  # FRIDA's max length
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Batch embed documents using search_document prefix.
        This prefix optimizes embeddings for retrieval tasks.
        Batch size: 32 for GPU, 8 for CPU.
        """
        return self.model.encode(
            texts,
            prompt_name="search_document",
            batch_size=8,  # Adjust based on CPU/GPU
            show_progress_bar=True,
            normalize_embeddings=True  # Already default in FRIDA
        )
    
    def embed_query(self, query: str) -> List[float]:
        """
        Embed single query using search_query prefix.
        This prefix optimizes embeddings for query matching.
        """
        return self.model.encode(
            query,
            prompt_name="search_query",
            normalize_embeddings=True
        )
    
    def embed_for_categorization(self, texts: List[str]) -> List[List[float]]:
        """
        Embed texts for topic categorization using FRIDA's specialized prefix.
        Use this for grouping articles by technical domain (N3, deployment, API).
        This helps with metadata enrichment and article clustering.
        """
        return self.model.encode(
            texts,
            prompt_name="categorize_topic",
            batch_size=8,
            show_progress_bar=True,
            normalize_embeddings=True
        )
    
    def embed_for_paraphrase(self, texts: List[str]) -> List[List[float]]:
        """
        Embed texts for finding similar sections using FRIDA's paraphrase prefix.
        Better than generic similarity for documentation deduplication.
        Use this to find semantically equivalent but differently worded sections.
        """
        return self.model.encode(
            texts,
            prompt_name="paraphrase",
            batch_size=8,
            show_progress_bar=True,
            normalize_embeddings=True
        )
```

**CPU Performance Optimization:**

```python
# For CPU-only deployment, use these optimized settings
EMBEDDING_CONFIG = {
    "model_name": "ai-forever/FRIDA",
    "device": "cpu",  # or "cuda" if GPU available
    "batch_size": 8,   # Optimized for CPU (use 32 for GPU)
    "max_seq_length": 512,
    "embedding_dim": 768,
}

# Expected performance on CPU:
# - Single query: 100-200ms
# - Full indexing (500 docs, ~2000 chunks): 15-20 minutes
# - This is acceptable for production use
```

#### 3.2 ChromaDB Vector Store

**File:** `core/vector_store.py`

Implement ChromaDB operations with rich metadata support:

**Inspiration from:**

- `agent-course-final-assignment/setup_vector_store.py` - Vector store initialization patterns
- `deepwiki-open` - Collection management and query strategies

**Key operations:**

1. **Initialization:**
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
    embedding_function=None  # We'll provide embeddings directly
)
```

2. **Indexing with metadata:**
```python
collection.add(
    ids=chunk_ids,           # ["4966_chunk_001", "4966_chunk_002", ...]
    embeddings=embeddings,    # List[List[float]]
    documents=chunk_texts,    # List[str]
    metadatas=chunk_metadata  # List[Dict] - ALL our rich metadata
)
```

3. **Querying with metadata filters:**
```python
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=20,
    where={"language": "ru"},  # Metadata filtering
    include=["documents", "metadatas", "distances"]
)
```


**Advanced features:**

- Incremental updates (add new documents without rebuilding)
- Metadata filtering during search
- Distance threshold filtering
- Deduplication by kbId

### Phase 4: Retrieval and Reranking

#### 4.1 Vector Retriever

**File:** `retrieval/retriever.py`

Implement retrieval with metadata-aware post-processing:

**Query pipeline:**

1. Embed user query
2. Search ChromaDB (top-k=20)
3. Group chunks by article (kbId)
4. Retrieve full articles for top matches
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

#### 4.2 Cross-Encoder Reranker

**File:** `retrieval/reranker.py`

Implement cross-encoder reranking for improved relevance:

**What is Cross-Encoder Reranking?**

Unlike bi-encoders (which encode query and documents separately), cross-encoders jointly encode the query-document pair, producing a direct relevance score. This provides higher accuracy at the cost of computational overhead.

**Architecture:**

```
Query + Document → Cross-Encoder → Relevance Score (0-1)
```

**Why it's better than vector similarity alone:**

- Captures semantic relationships between query and document
- Understands negation, nuance, and context
- Produces calibrated relevance scores
- Significantly improves top-k accuracy

**Implementation approach:**

1. **Initial retrieval:** Vector search returns top-20 candidates (fast but approximate)
2. **Reranking:** Cross-encoder scores each query-document pair (slow but accurate)
3. **Final selection:** Return top-5 reranked results to LLM

**Model selection:**

```python
from sentence_transformers import CrossEncoder

# Option 1: Multilingual cross-encoder (recommended)
reranker = CrossEncoder('cross-encoder/mmarco-mMiniLMv2-L12-H384-v1')

# Option 2: English-optimized (faster)
# reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')
```

**Reranking with metadata boost:**

```python
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
        # Concatenate best chunks for reranking
        article_text = " ".join([c["content"] for c in article["chunks"][:3]])
        pairs.append([query, article_text])
    
    # Get cross-encoder scores
    scores = reranker.predict(pairs)
    
    # Apply metadata boosting
    for i, article in enumerate(articles):
        base_score = scores[i]
        
        # Boost based on metadata
        boost = 1.0
        
        # 1. Title/tag match boost
        if query_matches_tags(query, article["metadata"]["tags"]):
            boost *= 1.2
        
        # 2. Code presence boost (if query mentions code/N3/скрипт)
        if query_is_about_code(query) and article["metadata"].get("has_code"):
            boost *= 1.15
        
        # 3. Section relevance boost
        if article["metadata"]["section_heading"]:
            if query_matches_heading(query, article["metadata"]["section_heading"]):
                boost *= 1.1
        
        scores[i] = base_score * boost
    
    # Sort and return top-k
    ranked_indices = np.argsort(scores)[::-1][:top_k]
    return [articles[i] for i in ranked_indices]
```

### Phase 5: LLM Integration

#### 5.1 Multi-LLM Manager Integration

**Files to copy from `cmw-platform-agent/agent_ng/`:**

- `llm_manager.py` (complete)
- `provider_adapters.py` (complete)
- `langsmith_config.py` (complete)
- `utils.py` (only the functions used by llm_manager)

**Integration approach:**

1. Copy the LLM manager as a module under `rag_engine/llm/`
2. Update import paths to work in the new project structure
3. Configure supported providers in `.env`:
```env
# Multi-LLM Configuration
GOOGLE_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
OPENROUTER_API_KEY=your_openrouter_key
MISTRAL_API_KEY=your_mistral_key

# Default LLM selection
DEFAULT_LLM_PROVIDER=gemini
DEFAULT_MODEL=gemini-1.5-flash

# LangSmith observability (optional)
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_PROJECT=mkdocs-rag
```


**Usage in RAG pipeline:**

```python
from llm.llm_manager import LLMManager

llm_manager = LLMManager()
llm = llm_manager.get_llm("gemini", use_tools=False)

# Stream response
for chunk in llm.stream(messages):
    yield chunk.content
```

#### 5.2 Prompt Engineering for RAG

**System prompt template:**

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

USER_PROMPT = """Question: {question}

Based on the documentation context above, provide a detailed answer with citations."""
```

**Response formatting:**

```python
def format_response_with_citations(
    answer: str,
    articles: List[Dict]
) -> str:
    """Format response with proper citations"""
    
    citations = "\n\n## Sources:\n\n"
    for i, article in enumerate(articles, 1):
        citations += f"{i}. [{article['title']}]({article['url']})\n"
        
        # Add specific sections if available
        for chunk in article["chunks"]:
            section = chunk["metadata"].get("section_heading")
            anchor = chunk["metadata"].get("section_anchor")
            if section and anchor:
                citations += f"   - Section: [{section}]({article['url']}{anchor})\n"
    
    return answer + citations
```

### Phase 6: Web Interface

#### 6.1 Gradio Interface (Simple deployment)

**File:** `api/app.py`

Create a Gradio web interface with streaming support:

**Features:**

- Real-time streaming responses
- Source citations display
- Query history
- Configuration options (embedding model, LLM provider, top-k)
- Example queries

**Implementation:**

```python
import gradio as gr

def query_rag_system(
    question: str,
    llm_provider: str,
    top_k: int = 5,
    progress=gr.Progress()
):
    """Query the RAG system with streaming response"""
    
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

# Create Gradio interface
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

#### 6.2 Alternative: FastAPI + React (Production-ready)

For more advanced deployment, create a FastAPI backend with REST endpoints:

**Endpoints:**

- `POST /api/query` - Submit question, get streaming response
- `POST /api/index` - Trigger reindexing
- `GET /api/health` - Health check
- `GET /api/stats` - Index statistics

### Phase 7: Build and Deployment Scripts

#### 7.1 Index Building Script

**File:** `scripts/build_index.py`

Command-line tool for building/updating the vector index:

```python
import argparse

def build_index(
    source_path: str,
    collection_name: str = "mkdocs_kb",
    rebuild: bool = False
):
    """Build or update the vector index"""
    
    print(f"📚 Processing documents from: {source_path}")
    
    # 1. Scan documents
    documents = document_processor.scan_directory(source_path)
    print(f"   Found {len(documents)} documents")
    
    # 2. Parse and chunk
    all_chunks = []
    for doc in documents:
        parsed_doc = document_processor.parse_document(doc)
        chunks = chunker.create_chunks(parsed_doc)
        enriched_chunks = metadata_enricher.enrich(chunks)
        all_chunks.extend(enriched_chunks)
    
    print(f"   Created {len(all_chunks)} chunks")
    
    # 3. Generate embeddings
    print("   Generating embeddings...")
    embeddings = embedder.embed_documents([c["content"] for c in all_chunks])
    
    # 4. Store in ChromaDB
    print("   Storing in ChromaDB...")
    vector_store.add_documents(all_chunks, embeddings, rebuild=rebuild)
    
    print("✅ Index built successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Source directory or file")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild index from scratch")
    args = parser.parse_args()
    
    build_index(args.source, rebuild=args.rebuild)
```

**Usage examples:**

```bash
# Index full docs/ru/ directory
python scripts/build_index.py --source docs/ru/

# Index specific phpkb content
python scripts/build_index.py --source "phpkb_content/798. Версия 5.0. Текущая рекомендованная/"

# Index pre-compiled KB file
python scripts/build_index.py --source kb.comindware.ru.platform_v5_for_llm_ingestion.md

# Rebuild index from scratch
python scripts/build_index.py --source docs/ru/ --rebuild
```

#### 7.2 Testing Script

**File:** `scripts/test_queries.py`

Test the RAG system with predefined queries:

```python
TEST_QUERIES = [
    "Как создать вычисляемый атрибут с помощью N3?",
    "What are the system requirements for Comindware Platform?",
    "Как настроить подключение к электронной почте?",
    "How do if-else statements work in N3 expressions?"
]

def test_rag_system():
    for query in TEST_QUERIES:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print('='*60)
        
        response = rag_system.query(query)
        print(response)
```

### Phase 8: Documentation and Deployment

#### 8.1 README Documentation

Create comprehensive README.md with:

- Architecture overview
- Installation instructions
- Configuration guide
- Usage examples
- API documentation (if using FastAPI)
- Troubleshooting

#### 8.2 Requirements File

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
# OR for FastAPI:
# fastapi>=0.104.0
# uvicorn>=0.24.0

# Reranking
# Note: Uses same sentence-transformers library

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

#### 8.3 Environment Configuration

**File:** `.env.example`

```env
# === Embedding Configuration ===
EMBEDDING_MODEL=ai-forever/ru-en-RoSBERTa
# Alternatives: 
# - sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
# - intfloat/multilingual-e5-large

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

#### 8.4 Deployment Configuration

For self-hosted deployment under your existing domain:

1. **Docker deployment:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-ca
che-dir -r requirements.txt


COPY . .

# Download embedding models
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('ai-forever/ru-en-RoSBERTa')"

EXPOSE 7860

CMD ["python", "api/app.py"]
```

2. **Nginx reverse proxy configuration:**
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


## Key Technical Decisions Summary

### Embedding Model: ai-forever/ru-en-RoSBERTa

**Rationale:** Optimized for Russian-English bilingual content, good balance of quality and performance, OpenAI-compatible vector dimensions

### Vector Database: ChromaDB

**Rationale:** Purpose-built for RAG, excellent metadata support, easy self-hosting, persistent storage, no external dependencies

### Chunking Strategy: 700 tokens / 300 overlap

**Rationale:** Proven effective in existing `rag_agent/search-assistant.py`, balances context size with retrieval precision

### Reranking: Cross-encoder with metadata boosting

**Rationale:** Significantly improves relevance over vector similarity alone, metadata boosting leverages rich document structure

### LLM Management: Multi-provider with fallback

**Rationale:** Flexibility for different use cases, proven architecture from `cmw-platform-agent`, easy to extend

### Retrieval Pipeline: Vector search → Rerank → Article reconstruction

**Rationale:** Fast initial retrieval, accurate reranking, complete article context for LLM

## Success Metrics

- **Indexing speed:** < 5 minutes for full docs/ru/ (~500 documents)
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

- [ ] Create project structure under rag_engine/ with all subdirectories and copy LLM manager from cmw-platform-agent
- [ ] Implement configuration management system with settings.py and .env support
- [ ] Implement document processor with frontmatter parsing, markdown structure extraction, and anchor preservation
- [ ] Implement semantic text chunker with section-based splitting, token counting, and overlap management
- [ ] Implement metadata enricher to add computed metadata (has_code, keywords, complexity_score, etc.)
- [ ] Implement embedding generator using ai-forever/ru-en-RoSBERTa with batch processing and GPU support
- [ ] Implement ChromaDB vector store operations with rich metadata support and persistence
- [ ] Implement vector retriever with metadata filtering and article reconstruction
- [ ] Implement cross-encoder reranker with metadata boosting for improved relevance
- [ ] Integrate multi-LLM manager from cmw-platform-agent and implement RAG-specific prompts
- [ ] Implement response formatting with citations, source links, and section anchors
- [ ] Create build_index.py script for indexing documents from various sources
- [ ] Implement Gradio web interface with streaming responses, source display, and configuration options
- [ ] Create test_queries.py script with predefined test cases
- [ ] Write comprehensive README with architecture overview, installation guide, and usage examples
- [ ] Create Docker configuration and nginx reverse proxy setup for production deployment