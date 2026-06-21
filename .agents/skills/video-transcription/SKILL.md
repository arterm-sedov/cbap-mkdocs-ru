---
name: video-transcription
description: Transcribe meeting recordings with Google Gemini for future documentation work. Use when the user provides a video file and needs a structured Markdown transcript with timestamps, visual notes, and summary in .scratch/.
---

# Video Transcription (Gemini)

Transcribe internal meetings and screen recordings before turning them into KB articles or release notes.

## Script

| File | Purpose |
|---|---|
| `scripts/video_transcription.py` | Upload video to Gemini, write Markdown transcript + metadata JSON |
| `prompts/video_transcription_prompt.md` | Default Russian verbose transcript prompt |

Run from repository root with the repo venv:

```powershell
.\.venv\Scripts\python.exe .agents\skills\video-transcription\scripts\video_transcription.py path\to\meeting.mp4
```

## Setup

1. Install deps (once): `google-genai` is listed in `install/requirements.txt`; run `python-env-setup` if the venv is missing packages.
2. Set `GEMINI_API_KEY` in repo `.env`, or pass `--api-key`.

## Output

Default output goes to gitignored `.scratch/`:

- `.scratch/<video_stem>_transcription.md`
- `.scratch/<video_stem>_transcription_metadata.json`

Override with `--output .scratch/custom_name.md`.

## Common options

```powershell
.\.venv\Scripts\python.exe .agents\skills\video-transcription\scripts\video_transcription.py meeting.mp4 --fps 0.5
.\.venv\Scripts\python.exe .agents\skills\video-transcription\scripts\video_transcription.py meeting.mp4 `
  --output .scratch/meeting_notes.md `
  --prompt-file .agents\skills\video-transcription\prompts\video_transcription_prompt.md
```

## Workflow

1. Transcribe the recording into `.scratch/`.
2. Review/edit the Markdown for factual accuracy.
3. Draft or update `docs/ru/` articles from the transcript.
4. Keep disposable transcripts in `.scratch/`; do not commit them unless the user asks.

Supported video types: mp4, mpeg, mov, avi, flv, mpg, webm, wmv, 3gpp.
