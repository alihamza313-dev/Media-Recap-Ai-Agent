from core.transcriber import transcribe_all
from utils.audio_processor import process_audio

source = "https://www.youtube.com/watch?v=ZVPlLaehjLk"

chunks = process_audio(source)

print(transcribe_all(chunks))