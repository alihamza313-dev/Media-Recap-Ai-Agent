import yt_dlp
from pydub import AudioSegment
import os

Download_Dir = "Downloads"
os.makedirs(Download_Dir,exist_ok=True)

def download_youtube_audio(url : str)->str:
    ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(Download_Dir,"%(title)s.%(ext)s"),
    'ffmpeg_location': r'C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin',
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality" : "192",
        }
    ],
    "quiet" : True,
}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        filename = os.path.splitext(filename)[0] + ".wav"
    return filename


def convert_to_wav(input_path : str)->str:
    """use pydub to convert the audio into the wav format"""

    output_path = os.path.splitext(input_path)[0]+ "_converted.wav"

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Audio file not found: {input_path}")
    
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path,format = "wav")
    return output_path


def chunk_audio(wav_path: str, chunk_min: int = 10) -> list:
    chunks = []

    if not os.path.exists(wav_path):
        raise FileNotFoundError(f"Audio file not found: {wav_path}")

    audio = AudioSegment.from_wav(wav_path)

    chunk_ms = chunk_min * 60 * 1000 
    #convert time into milliseconds Because pydub uses milliseconds.

    base_name = os.path.splitext(wav_path)[0]

    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start:start + chunk_ms]

        chunk_path = f"{base_name}_chunk_{i}.wav"

        chunk.export(chunk_path, format="wav")

        chunks.append(chunk_path)

    return chunks


def process_audio(source: str) -> list:

    if source.startswith(("http://", "https://")):
        print("Detected YouTube URL. Downloading audio...")
        audio_path = download_youtube_audio(source)

    elif os.path.exists(source):
        print("Detected local file...")
        audio_path = source

    else:
        raise ValueError("Invalid URL or file path")

    print("Converting audio to WAV...")
    wav_path = convert_to_wav(audio_path)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)

    print(f"Audio ready - {len(chunks)} chunk(s) created.")

    return chunks

"""For testing audio_processor.py"""
url = "https://www.youtube.com/watch?v=ZVPlLaehjLk"

print(process_audio(url))