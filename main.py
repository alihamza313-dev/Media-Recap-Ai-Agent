from core.transcriber import transcribe_all
from utils.audio_processor import process_audio
from Rag.rag_engine import rag_pipeline, ask_question
from services.summarizer import create_summary
from services.extractor import extract_action_items,extract_key_decisions,extract_questions

def print_section(title, content):
    print("-"*50)
    print(f"{title}:\n{content}")

source = "https://www.youtube.com/watch?v=5sLYAQS9sWQ"

try:
    audio_chunks = process_audio(source)

    transcript = transcribe_all(audio_chunks)

except Exception as e:
    print(f"Processing failed: {e}")
    exit()


try:
    rag_chain, collection_name , title = rag_pipeline(
        transcript=transcript
    )

    print(f"Stored collection: {collection_name}")

    summary = create_summary(transcript)
    key_actions = extract_action_items(transcript)
    key_decisions = extract_key_decisions(transcript)
    questions = extract_questions(transcript)
except Exception as e:
    print(f"RAG processing failed: {e}")
    exit()

print_section("Title", title)
print_section("Summary", summary)
print_section("Key Actions", key_actions)
print_section("Decision Points", key_decisions)
print_section("Questions", questions)



print("\n💬 Chat with your meeting (type 'exit' to quit)\n")

while True:
    question = input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    if not question:
        continue

    answer = ask_question(
        rag_chain,
        question
    )

    print(f"\n🤖 Assistant: {answer}\n")
    print("-"*50)