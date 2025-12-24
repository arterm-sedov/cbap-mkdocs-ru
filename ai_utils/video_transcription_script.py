#!/usr/bin/env python3
"""
Video Transcription Script using Google Gemini API
Transcribes video with 0.5 FPS frame rate for detailed analysis

Requirements:
- google-genai library
- Valid Gemini API key
- Video file in supported format (MP4, MOV, AVI, etc.)
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional
from google import genai
import json
from datetime import datetime

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, continue without it
    pass

class VideoTranscriber:
    def __init__(self, api_key: str):
        """
        Initialize the video transcriber with Gemini API key
        
        Args:
            api_key (str): Google Gemini API key
        """
        self.client = genai.Client(api_key=api_key)
        self.supported_formats = [
            'video/mp4', 'video/mpeg', 'video/mov', 'video/avi',
            'video/x-flv', 'video/mpg', 'video/webm', 'video/wmv', 'video/3gpp'
        ]
    
    def get_mime_type(self, file_path: str) -> str:
        """
        Get MIME type for video file
        
        Args:
            file_path (str): Path to video file
            
        Returns:
            str: MIME type of the video file
        """
        import mimetypes
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type not in self.supported_formats:
            raise ValueError(f"Unsupported video format: {mime_type}")
        return mime_type
    
    def upload_video_file(self, file_path: str) -> genai.File:
        """
        Upload video file using Files API
        
        Args:
            file_path (str): Path to video file
            
        Returns:
            genai.File: Uploaded file object
        """
        print(f"Uploading video file: {file_path}")
        
        # Check file size
        file_size = os.path.getsize(file_path)
        file_size_mb = file_size / (1024 * 1024)
        print(f"File size: {file_size_mb:.2f} MB")
        
        if file_size_mb > 20:
            print("File is larger than 20MB, using Files API...")
            return self.client.files.upload(file=file_path)
        else:
            print("File is smaller than 20MB, using inline upload...")
            return self.client.files.upload(file=file_path)
    
    def transcribe_video(self, file_path: str, fps: float = 0.25, 
                        output_file: Optional[str] = None, 
                        prompt_file: Optional[str] = None) -> str:
        """
        Transcribe video with custom frame rate
        
        Args:
            file_path (str): Path to video file
            fps (float): Frames per second (default: 0.25)
            output_file (str, optional): Output file path for transcription
            
        Returns:
            str: Transcription text in markdown format
        """
        try:
            # Validate file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Video file not found: {file_path}")
            
            # Get MIME type
            mime_type = self.get_mime_type(file_path)
            print(f"Video format: {mime_type}")
            
            # Upload file
            uploaded_file = self.upload_video_file(file_path)
            print(f"File uploaded successfully: {uploaded_file.uri}")
            
            # Load transcription prompt from external file
            if prompt_file:
                prompt_file_path = Path(prompt_file)
            else:
                prompt_file_path = Path(__file__).parent / "prompts" / "video_transcription_prompt.md"
            
            try:
                with open(prompt_file_path, 'r', encoding='utf-8') as f:
                    prompt = f.read()
                print(f"Loaded prompt from: {prompt_file_path}")
            except FileNotFoundError:
                print(f"Warning: Prompt file not found at {prompt_file_path}, using default prompt")
                prompt = """
                Транскрибируйте как речь, так и видеоконтент в прикрепленном видео. Выводите на русском языке. Транскрибируйте самым подробным образом. Выводите структурированный Markdown с временными метками. После транскрипции включите очень подробное резюме и объяснения.
                """
            
            # Generate content with custom FPS
            print(f"Processing video with {fps} FPS...")
            
            if os.path.getsize(file_path) < 20 * 1024 * 1024:  # < 20MB
                # Use inline data for smaller files
                with open(file_path, 'rb') as f:
                    video_bytes = f.read()
                    
                video_file = self.client.files.upload(file=file_path)
                
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        {
                            "parts": [
                                types.Part(
                                    file_data=video_file,
                                    video_metadata=types.VideoMetadata(fps=fps)
                                ),
                                types.Part(text=prompt)
                            ]
                        }
                    ]
                )
            else:
                # Use file reference for larger files
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        {
                            "parts": [
                                {
                                    "file_data": {
                                        "file_uri": uploaded_file.uri,
                                        "mime_type": mime_type
                                    },
                                    "video_metadata": {
                                        "fps": fps
                                    }
                                },
                                {"text": prompt}
                            ]
                        }
                    ]
                )
            
            transcription = response.text
            print("Transcription completed successfully!")
            
            # Save to file if specified
            if output_file:
                self.save_transcription(transcription, output_file)
            
            return transcription
            
        except Exception as e:
            print(f"Error during transcription: {str(e)}")
            raise
    
    def save_transcription(self, transcription: str, output_file: str):
        """
        Save transcription to markdown file
        
        Args:
            transcription (str): Transcription text in markdown format
            output_file (str): Output file path
        """
        try:
            # Create output directory if it doesn't exist
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Add header information to the markdown file
            header = f"""# Video Transcription

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Model:** Gemini 2.5 Flash  
**Processing:** Detailed video transcription with analysis

---

"""
            
            # Save transcription with header
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(header + transcription)
            
            print(f"Transcription saved to: {output_file}")
            
            # Also save metadata
            metadata_file = output_file.replace('.md', '_metadata.json')
            metadata = {
                "timestamp": datetime.now().isoformat(),
                "fps": 0.5,
                "model": "gemini-2.5-flash",
                "file_size_mb": os.path.getsize(output_file) / (1024 * 1024),
                "format": "markdown"
            }
            
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)
            
            print(f"Metadata saved to: {metadata_file}")
            
        except Exception as e:
            print(f"Error saving transcription: {str(e)}")
            raise

def main():
    """Main function to run the video transcription script"""
    parser = argparse.ArgumentParser(
        description="Transcribe video using Google Gemini API with 0.5 FPS"
    )
    parser.add_argument(
        "video_file", 
        help="Path to the video file to transcribe"
    )
    parser.add_argument(
        "--api-key", 
        help="Google Gemini API key (can also be set via GEMINI_API_KEY environment variable)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path for transcription (default: video_name_transcription.md)"
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=0.25,
        help="Frames per second for video processing (default: 0.25)"
    )
    parser.add_argument(
        "--prompt-file",
        help="Path to custom prompt file (default: ai_utils/prompts/video_transcription_prompt.md)"
    )
    
    args = parser.parse_args()
    
    # Get API key from command line argument or environment variable
    api_key = args.api_key or os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: API key is required. Provide it via --api-key argument or GEMINI_API_KEY environment variable.")
        sys.exit(1)
    
    # Set default output file if not specified
    if not args.output:
        video_name = Path(args.video_file).stem
        args.output = f"{video_name}_transcription.md"
    
    try:
        # Initialize transcriber
        transcriber = VideoTranscriber(api_key)
        
        # Transcribe video
        transcription = transcriber.transcribe_video(
            file_path=args.video_file,
            fps=args.fps,
            output_file=args.output,
            prompt_file=args.prompt_file
        )
        
        print("\n" + "="*50)
        print("TRANSCRIPTION COMPLETED")
        print("="*50)
        print(transcription)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
