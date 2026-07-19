# Media Recap AI

Media Recap AI is an AI-powered application that transforms long-form audio and video content into structured, searchable knowledge.

The application accepts a YouTube URL or a local media file, automatically extracts the audio, generates an accurate transcript, analyzes the content using Large Language Models (LLMs), stores transcript embeddings in a vector database, and allows users to interact with the content through Retrieval-Augmented Generation (RAG).

---

# Features

## Media Processing

- YouTube video support
- Local audio file support
- Local video file support
- Automatic audio extraction
- Audio normalization (16 kHz Mono WAV)

---

## Hybrid Speech-to-Text Pipeline

Media Recap AI automatically selects the appropriate transcription provider based on the selected language.

| Language | Provider |
|----------|----------|
| English | OpenAI Whisper |
| Hindi | AssemblyAI |
| Urdu | AssemblyAI |
| Other Supported Languages | AssemblyAI |

### Whisper Pipeline

- Local inference
- Audio chunking
- Optimized for English transcription

### AssemblyAI Pipeline

- Cloud-based transcription
- Multilingual support
- Handles complete audio without chunking

---

## AI Analysis

After transcription, the application automatically generates:

- Title
- Summary
- Action Items
- Key Decisions
- Questions

---

## Retrieval-Augmented Generation (RAG)

Each transcript is converted into embeddings and stored inside ChromaDB.

Users can ask natural language questions such as:

- What is the main topic?
- What decisions were made?
- What action items were assigned?
- Explain the discussion about AI.
- Summarize the meeting.

The answers are generated using only the retrieved transcript context.

---

# System Architecture

```
                     User Input
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
   YouTube URL                        Local File
        │                                   │
        └──────────────┬────────────────────┘
                       ▼
               Audio Processing
                       │
                       ▼
              Language Selection
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
     English                   Other Languages
        │                             │
        ▼                             ▼
     Whisper                    AssemblyAI
        │                             │
        └──────────────┬──────────────┘
                       ▼
                  Transcript
                       │
                       ▼
                 AI Analysis
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
     Summary       Title        Information Extraction
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              Action Items   Decisions    Questions
                       │
                       ▼
                  Text Splitter
                       │
                       ▼
                  Embeddings
                       │
                       ▼
                   ChromaDB
                       │
                       ▼
                    RAG Chat
```

---

# Technology Stack

## Programming Language

- Python

## AI & Machine Learning

- OpenAI Whisper
- AssemblyAI
- Mistral AI
- LangChain
- HuggingFace Embeddings

## Retrieval

- ChromaDB
- Retrieval-Augmented Generation (RAG)

## Media Processing

- yt-dlp
- FFmpeg
- PyDub

---

# Processing Workflow

```
User Input
      │
      ▼
Audio Extraction
      │
      ▼
Language Selection
      │
      ▼
Automatic Transcriber Selection
      │
      ▼
Transcript Generation
      │
      ▼
AI Analysis
      │
      ▼
Vector Database
      │
      ▼
Interactive Chat
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/media-recap-ai.git

cd media-recap-ai
```

---

## Create a Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key

ASSEMBLYAI_API_KEY=your_assemblyai_api_key
```

---

# Running the Application

```bash
python main.py
```

Example workflow:

```
Enter Media Source

        │

        ▼

Download / Extract Audio

        │

        ▼

Generate Transcript

        │

        ▼

Generate AI Insights

        │

        ▼

Store Embeddings

        │

        ▼

Ask Questions
```

---

# Example Output

## Generated Title

```
Introduction to Large Language Models
```

---

## Summary

```
• Large Language Models were introduced.

• Transformer architecture was explained.

• Real-world AI applications were discussed.
```

---

## Action Items

```
• Review the research paper.

• Build a prototype.

• Schedule the next discussion.
```

---

## Key Decisions

```
• Use a Retrieval-Augmented Generation architecture.

• Store embeddings using ChromaDB.
```

---

## Questions

```
• How do embeddings work?

• Which LLM should be selected?

• How is semantic search performed?
```

---

# Architecture

The transcription layer follows a provider-based architecture.

- `Whisper_transcriber.py` performs English transcription using OpenAI Whisper.

- `Assembly_AI.py` performs multilingual transcription using AssemblyAI.

- `transcriber.py` automatically selects the appropriate provider based on the selected language.

This design keeps the transcription layer modular and makes it easy to integrate additional providers in the future.

---

# Current Capabilities

- YouTube media processing
- Local media processing
- Automatic audio extraction
- Hybrid transcription pipeline
- AI-generated summaries
- AI-generated titles
- Action item extraction
- Decision extraction
- Question extraction
- Vector database storage
- Retrieval-Augmented Generation
- Interactive transcript chat

---

# Future Improvements

- Automatic language detection
- Speaker diarization
- FastAPI REST API
- Web-based frontend
- User authentication
- Meeting history
- Team collaboration
- Cloud deployment
- Real-time transcription
- Meeting sharing

---

# Author

**Ali Hamza**

Computer Science Student | Backend Engineer | AI Enthusiast