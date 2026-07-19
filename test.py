from utils.aai_audio_processing import prepare_audio
from core.Assembly_AI import transcribe

url = "https://www.youtube.com/watch?v=wioAFuHzcao"

audio_path = prepare_audio(url)

transcript = transcribe(audio_path)

print(transcript)