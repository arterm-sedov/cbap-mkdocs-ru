# Search Assistant

This script creates a Yandex Cloud ML assistant for searching through documentation using RAG (Retrieval-Augmented Generation).

## Features

- **Document Upload**: Automatically uploads documentation files from the specified directory
- **Search Index Creation**: Creates optimized search indexes with configurable chunking
- **Interactive Q&A**: Real-time question answering with citation tracking
- **Resource Management**: Automatic cleanup of uploaded files and created resources
- **Error Handling**: Robust error handling with detailed progress feedback

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the `rag_agent` directory with your Yandex Cloud credentials:

```env
# Yandex Cloud credentials
YANDEX_FOLDER_ID=your_folder_id_here
YANDEX_API_KEY=your_api_key_here
```

3. Replace the placeholder values with your actual Yandex Cloud folder ID and API key.

## Usage

Run the script:
```bash
python search-assistant.py
```

The script will:
- Recursively scan and upload all `.md` files from the `../docs/ru/tutorials` directory and its subdirectories
- Create a search index with optimized chunking (700 tokens with 300-token overlap)
- Start an interactive session where you can ask questions about the documentation
- Display responses with source citations
- Clean up all resources when you exit

## Configuration

### File Processing
- **Source Directory**: `../docs/ru/tutorials` (configurable in the script)
- **File Types**: Only `.md` files (recursively scanned)
- **Recursive Scanning**: Automatically finds all `.md` files in subdirectories
- **TTL**: 5 days with static expiration policy

### Search Index Settings
- **Chunk Size**: 700 tokens
- **Overlap**: 300 tokens
- **Strategy**: Static chunking for consistent results

## Environment Variables

- `YANDEX_FOLDER_ID`: Your Yandex Cloud folder ID
- `YANDEX_API_KEY`: Your Yandex Cloud API key

Make sure these are properly set in your `.env` file or as system environment variables.

## Troubleshooting

- **Permission Errors**: Ensure the script has read access to the documentation directory
- **Upload Failures**: Check your Yandex Cloud credentials and network connectivity
- **No Files Uploaded**: Verify the source directory path and file permissions 