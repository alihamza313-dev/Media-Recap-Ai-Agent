import whisper
import os

WHISPER_MODEL = os.getenv("WHISPER_MODEL","small")
#Get WHISPER_MODEL from environment, otherwise use "small"

_model = None

def load_model():
    global _model
    if _model is None:
        print("Loading Model ...")
        _model = whisper.load_model(WHISPER_MODEL)
        print("Whisper Model loaded successfully.")

    return _model


def transcribe(chunk_path : str , task : str):
    model = load_model()

    result = model.transcribe(chunk_path , task = task)
    return result['text']


def transcribe_all(chunks : list , translate : bool = False):
    full_transcript = ""

    task = "translate" if translate else "transcribe"

    for i , chunk_path in enumerate(chunks):
        print(f"Transcribing chunk_{i+1}...")

        text = transcribe(chunk_path,task)

        print("Transcription for chunk_{i+1} is done.")
        
        full_transcript+= text + " "

    print("Transcription Completed.")
    return full_transcript