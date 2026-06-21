#!/usr/bin/env python3
"""Transcribe meeting recordings with Google Gemini for future documentation work."""

import argparse
import json
import mimetypes
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from google import genai

SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]

try:
    from dotenv import load_dotenv

    load_dotenv(REPO_ROOT / ".env")
except ImportError:
    pass

DEFAULT_PROMPT = SKILL_DIR / "prompts" / "video_transcription_prompt.md"
DEFAULT_SCRATCH = REPO_ROOT / ".scratch"

SUPPORTED_MIME_TYPES = {
    "video/mp4",
    "video/mpeg",
    "video/mov",
    "video/avi",
    "video/x-flv",
    "video/mpg",
    "video/webm",
    "video/wmv",
    "video/3gpp",
}


class VideoTranscriber:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def get_mime_type(self, file_path: str) -> str:
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type not in SUPPORTED_MIME_TYPES:
            raise ValueError(f"Unsupported video format: {mime_type}")
        return mime_type

    def upload_video_file(self, file_path: str):
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        print(f"Uploading video file: {file_path} ({file_size_mb:.2f} MB)")
        return self.client.files.upload(file=file_path)

    def load_prompt(self, prompt_file: Optional[str]) -> str:
        prompt_file_path = Path(prompt_file) if prompt_file else DEFAULT_PROMPT
        try:
            prompt = prompt_file_path.read_text(encoding="utf-8")
            print(f"Loaded prompt from: {prompt_file_path}")
            return prompt
        except FileNotFoundError:
            print(f"Warning: prompt file not found at {prompt_file_path}, using fallback prompt")
            return (
                "Transcribe speech and visual content. Output structured Markdown with timestamps "
                "and a detailed summary at the end."
            )

    def transcribe_video(
        self,
        file_path: str,
        fps: float = 0.25,
        output_file: Optional[str] = None,
        prompt_file: Optional[str] = None,
    ) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Video file not found: {file_path}")

        mime_type = self.get_mime_type(file_path)
        print(f"Video format: {mime_type}")

        uploaded_file = self.upload_video_file(file_path)
        print(f"File uploaded successfully: {uploaded_file.uri}")

        prompt = self.load_prompt(prompt_file)
        print(f"Processing video with {fps} FPS...")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                {
                    "parts": [
                        {
                            "file_data": {
                                "file_uri": uploaded_file.uri,
                                "mime_type": mime_type,
                            },
                            "video_metadata": {"fps": fps},
                        },
                        {"text": prompt},
                    ]
                }
            ],
        )

        transcription = response.text
        print("Transcription completed successfully!")

        if output_file:
            self.save_transcription(transcription, output_file, fps=fps)

        return transcription

    def save_transcription(self, transcription: str, output_file: str, fps: float):
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        header = (
            "# Video Transcription\n\n"
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
            f"**Model:** Gemini 2.5 Flash  \n"
            f"**FPS:** {fps}\n\n"
            "---\n\n"
        )
        output_path.write_text(header + transcription, encoding="utf-8")
        print(f"Transcription saved to: {output_path}")

        metadata_file = output_path.with_name(output_path.stem + "_metadata.json")
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "fps": fps,
            "model": "gemini-2.5-flash",
            "output_md": str(output_path),
            "format": "markdown",
        }
        metadata_file.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        print(f"Metadata saved to: {metadata_file}")


def default_output_path(video_file: str) -> Path:
    DEFAULT_SCRATCH.mkdir(parents=True, exist_ok=True)
    stem = Path(video_file).stem
    return DEFAULT_SCRATCH / f"{stem}_transcription.md"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Transcribe a meeting recording with Google Gemini for documentation prep.",
    )
    parser.add_argument("video_file", help="Path to the video file to transcribe")
    parser.add_argument(
        "--api-key",
        help="Google Gemini API key (or set GEMINI_API_KEY in .env)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output Markdown path (default: .scratch/<video_stem>_transcription.md)",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=0.25,
        help="Frames per second for video processing (default: 0.25)",
    )
    parser.add_argument(
        "--prompt-file",
        help=f"Custom prompt file (default: {DEFAULT_PROMPT.relative_to(REPO_ROOT)})",
    )
    args = parser.parse_args(argv)

    api_key = args.api_key or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: set GEMINI_API_KEY in .env or pass --api-key.")
        sys.exit(1)

    output_file = args.output or str(default_output_path(args.video_file))

    try:
        transcriber = VideoTranscriber(api_key)
        transcription = transcriber.transcribe_video(
            file_path=args.video_file,
            fps=args.fps,
            output_file=output_file,
            prompt_file=args.prompt_file,
        )
        print("\n" + "=" * 50)
        print("TRANSCRIPTION COMPLETED")
        print("=" * 50)
        print(transcription)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
