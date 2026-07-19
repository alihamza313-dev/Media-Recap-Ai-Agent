import os
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

if not ASSEMBLYAI_API_KEY:
    raise ValueError("ASSEMBLYAI_API_KEY not found in .env")

aai.settings.api_key = ASSEMBLYAI_API_KEY


def transcribe(audio_path: str, language: str | None = None) -> str:
    
    config = aai.TranscriptionConfig()

    if language:
        config.language_code = language

    transcriber = aai.Transcriber(config=config)

    transcript = transcriber.transcribe(audio_path)

    if transcript.status == aai.TranscriptStatus.error:
        raise Exception(f"AssemblyAI Error: {transcript.error}")

    return transcript.text