#!/usr/bin/env python3

from __future__ import annotations

import os
import pathlib
from dotenv import load_dotenv

from yandex_cloud_ml_sdk import YCloudML
from yandex_cloud_ml_sdk.search_indexes import (
    StaticIndexChunkingStrategy,
    TextSearchIndexType,
)

# Load environment variables from .env file
load_dotenv()

mypath = "../docs/ru"


def main():
    # Get credentials from environment variables
    folder_id = os.getenv("YANDEX_FOLDER_ID")
    api_key = os.getenv("YANDEX_API_KEY")
    
    if not folder_id or not api_key:
        raise ValueError("YANDEX_FOLDER_ID and YANDEX_API_KEY must be set in environment variables or .env file")
    
    sdk = YCloudML(
        folder_id=folder_id,
        auth=api_key,
    )

    # Recursively scan for .md files
    base_path = pathlib.Path(mypath)
    md_files = list(base_path.rglob("*.md"))

    # Uploading files with examples.
    # The files will be stored for five days.
    files = []
    print(f"Scanning directory recursively: {mypath}")
    print(f"Found {len(md_files)} .md files")
    
    for path in md_files:
        # Get relative path for better display
        relative_path = path.relative_to(base_path)
        print(f"Uploading file: {relative_path}")
        try:
            file = sdk.files.upload(
                path,
                ttl_days=5,
                expiration_policy="static",
            )
            files.append(file)
            print(f"✓ Successfully uploaded: {relative_path}")
        except Exception as e:
            print(f"✗ Failed to upload {relative_path}: {e}")
    
    if not files:
        print("No files were uploaded. Please check the directory path and file permissions.")
        return
    
    print(f"Total files uploaded: {len(files)}")

    # Creating an index for full-text search through the uploaded files.
    # This example sets the chunk size
    # of up to 700 tokens, with a 300-token overlap.
    print("Creating search index...")
    operation = sdk.search_indexes.create_deferred(
        files,
        index_type=TextSearchIndexType(
            chunking_strategy=StaticIndexChunkingStrategy(
                max_chunk_size_tokens=700,
                chunk_overlap_tokens=300,
            )
        ),
    )

    # Waiting for the search index to be created.
    print("Waiting for search index creation to complete...")
    search_index = operation.wait()
    print("✓ Search index created successfully")

    # Creating a tool to work with the search index.
    # Or even several indexes if that were the case.
    tool = sdk.tools.search_index(search_index)

    # Creating an assistant for the Latest YandexGPT Pro model.
    # It will use the search index tool.
    print("Creating assistant...")
    assistant = sdk.assistants.create(
        "yandexgpt", 
        instruction = "You are an internal corporate documentation assistant. Answer politely. If the information is not in the documents below, don't make up your answer.", 
        tools=[tool])
    thread = sdk.threads.create()
    print("✓ Assistant created successfully")
    print("\n" + "="*60)
    print("DOCUMENTATION ASSISTANT READY")
    print("="*60)
    print("Ask questions about the uploaded documentation.")
    print("Type 'exit' to end the session.")
    print("-" * 60)

    input_text = input('\nEnter your question: ')

    while input_text.lower() != "exit":
        thread.write(input_text)

        # Giving the whole thread content to the model.
        run = assistant.run(thread)

        # To get the result, wait until the run is complete.
        result = run.wait()

        # Displaying the response.
        print("\n" + "="*60)
        print("ASSISTANT RESPONSE:")
        print("="*60)
        print(result.text)
        print("="*60)

        # Displaying some of the _citations_ property attributes: information
        # about utilized chunks created from the source files.
        if result.citations:
            print("\nSOURCES:")
            print("-" * 40)
            count = 1
            for citation in result.citations:
                for source in citation.sources:
                    if source.type != "filechunk":
                        continue
                    print(f"Source {count}:")
                    print(f"  - File: {source.file.id}")
                    print(f"  - Type: {source.file.mime_type}")
                    print(f"  - Content: {source.parts[:100]}...")
                    print()
                count += 1

        input_text = input('\nEnter your next question (or "exit" to end): ')

    # Delete everything you no longer need.
    print("\nCleaning up resources...")
    search_index.delete()
    thread.delete()
    assistant.delete()

    for file in files:
        file.delete()
    print("✓ All resources cleaned up successfully")


if __name__ == "__main__":
    main()
