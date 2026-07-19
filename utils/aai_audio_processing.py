import os
import yt_dlp
from pydub import AudioSegment

DOWNLOAD_DIR = "Downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_youtube_audio(url: str) -> str:
    """Download YouTube audio and convert it to WAV."""

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "ffmpeg_location": r"C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return os.path.splitext(filename)[0] + ".wav"


def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to a mono 16 kHz WAV."""

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Audio file not found: {input_path}")

    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    audio.export(output_path, format="wav")

    return output_path


def prepare_audio(source: str) -> str:

    if source.startswith(("http://", "https://")):
        print("Detected YouTube URL. Downloading audio...")
        audio_path = download_youtube_audio(source)

    elif os.path.exists(source):
        print("Detected local file...")
        audio_path = source

    else:
        raise ValueError("Invalid URL or file path.")

    print("Converting audio to WAV...")

    wav_path = convert_to_wav(audio_path)

    print("Audio is ready for transcription.")

    return wav_path