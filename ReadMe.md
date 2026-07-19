# Media Recap AI

Media Recap AI is an AI-powered application that transforms long-form audio and video content into structured, searchable knowledge. It supports YouTube videos and local media files, automatically transcribes speech, generates AI-powered insights, and enables semantic search over transcripts using Retrieval-Augmented Generation (RAG).

---

## Features

### Media Processing
- YouTube video support
- Local audio and video file support
- Automatic audio extraction and preprocessing
- Audio chunking for long recordings

### Speech-to-Text
- Local transcription using OpenAI Whisper
- Chunk-based transcription pipeline
- Optimized for long-form media

### AI-Powered Analysis
- Automatic title generation
- Bullet-point summaries
- Action item extraction
- Key decision extraction
- Question extraction

### Retrieval-Augmented Generation (RAG)
- Semantic search over transcripts
- ChromaDB vector database
- HuggingFace embeddings
- Context-aware question answering

---

## System Architecture

```text
             User Input
                  │
        ┌─────────┴─────────┐
        │                   │
 YouTube URL          Local Media
        │                   │
        └─────────┬─────────┘
                  │
          Audio Processing
                  │
          Audio Chunking
                  │
      Whisper Transcription
                  │
             Transcript
                  │
      ┌───────────┴───────────┐
      │                       │
 AI Information         Vector Database
 Extraction             (ChromaDB)
      │                       │
      └───────────┬───────────┘
                  │
              RAG Engine
                  │
             User Queries
                  │
              LLM Response
```

---

## Project Structure

```text
Media_Recap_AI/

├── core/
├── services/
├── Rag/
├── utils/
├── Vector_db/
├── collections.json
├── main.py
└── requirements.txt
```

---

## Technology Stack

### Backend

- Python
- LangChain

### AI

- OpenAI Whisper
- Mistral AI
- HuggingFace Embeddings

### Vector Database

- ChromaDB

### Media Processing

- yt-dlp
- FFmpeg
- Pydub

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/media-recap-ai.git
cd media-recap-ai
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key
```

Run the application.

```bash
python main.py
```

---

## Example Workflow

```text
YouTube URL
      │
      ▼
Download Audio
      │
      ▼
Speech-to-Text
      │
      ▼
Transcript
      │
      ▼
AI Analysis
      │
      ▼
Vector Database
      │
      ▼
Chat with Transcript
```

---

## Roadmap

Planned improvements include:

- AssemblyAI transcription support
- Improved multilingual transcription (Hindi and Urdu)
- User authentication
- Cloud storage
- Team collaboration
- Google Meet and Zoom integration
- Real-time transcription
- Web dashboard

---

## Author

**Ali Hamza**