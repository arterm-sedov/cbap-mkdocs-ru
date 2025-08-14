### Video Transcription (Gemini API)

This repository includes a CLI tool to generate complete, structured video transcriptions using Google Gemini (multimodal) with configurable FPS and externalized prompts.

- File: `ai_utils/video_transcription_script.py`
- Default prompt: `ai_utils/prompts/video_transcription_prompt.md`

#### Features

- Transcribes speech and describes visual content with timestamps
- Structured Markdown output (.md) + metadata JSON
- Custom FPS (default 0.25 fps)
- File API for large videos; inline for small videos
- Externalized prompt file; override via `--prompt-file`
- API key via `.env` or `--api-key`

#### Install

```bash
pip install google-genai python-dotenv
```

#### API key setup

Option A (recommended): `.env`

```bash
cp env_example.txt .env
# edit .env and set your key
```

Option B: CLI flag

```bash
python ai_utils/video_transcription_script.py video.mp4 --api-key YOUR_KEY
```

#### Usage

Basic (uses `.env`):

```bash
python ai_utils/video_transcription_script.py path/to/video.mp4
```

Advanced:

```bash
python ai_utils/video_transcription_script.py path/to/video.mp4 \
  --output out/transcript.md \
  --fps 0.5 \
  --prompt-file ai_utils/prompts/video_transcription_prompt.md
```

#### Options

- `video_file` (positional): path to input video
- `--api-key`: Gemini API key (or set `GEMINI_API_KEY` in `.env`)
- `--output`, `-o`: output Markdown file (default: `<video_name>_transcription.md`)
- `--fps`: frames per second for processing (default: 0.25)
- `--prompt-file`: path to a custom Markdown prompt

#### Output

- Markdown transcript: `<name>_transcription.md`
- Metadata JSON: `<name>_transcription_metadata.json`

Markdown contains a header (generation time, model) and a verbose, timestamped transcript per the prompt. JSON contains basic processing metadata.

#### Notes

- Language and structure of the transcript are controlled by the prompt file in `ai_utils/prompts/`. Adjust that file to change output language/structure.
- Supported video MIME types include: mp4, mpeg, mov, avi, x-flv, mpg, webm, wmv, 3gpp.
- For files >20MB, the script uploads via the Files API automatically.
- Timestamps should use MM:SS format as per Gemini docs.