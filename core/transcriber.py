from core.Whisper_transcriber import transcribe_all
from core.Assembly_AI import transcribe

from utils.audio_processor import process_audio
from utils.aai_audio_processing import prepare_audio

ENGLISH_LANGUAGES = {"english", "en"}


def get_transcript(source: str, language: str) -> str:
    """
    Generate a transcript using the appropriate transcription provider.
    """

    language = language.lower().strip()

    if language in ENGLISH_LANGUAGES:
        chunks = process_audio(source)
        return transcribe_all(chunks)

    audio_path = prepare_audio(source)
    return transcribe(audio_path, language=language)