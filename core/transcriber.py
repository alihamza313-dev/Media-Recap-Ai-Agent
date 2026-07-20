from core.Whisper_transcriber import transcribe_all
from core.Assembly_AI import transcribe

from utils.audio_processor import process_audio
from utils.aai_audio_processing import prepare_audio

ENGLISH_LANGUAGES = {"english", "en"}
HINDI_LANGUAGES = {"hindi" , "hi"}


def get_transcript(source: str, language: str) -> str:
    """
    Generate a transcript using the appropriate transcription provider.
    """

    language = language.lower().strip()

    if language in ENGLISH_LANGUAGES:
        #these two functions are are related to the whisper if language is detected as english then call whisper 
        chunks = process_audio(source)
        return transcribe_all(chunks)
    
    elif language in HINDI_LANGUAGES:
        #these two functions are related to the Assembly ai if language other than english
        audio_path = prepare_audio(source)
        return transcribe(audio_path, language=language)
    
    else:
        print("No language detected!! ('Language options : en/hi')")
        return
    