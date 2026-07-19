from core.transcriber import get_transcript
from Rag.rag_engine import rag_pipeline, ask_question
from services.summarizer import create_summary
from services.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)
import sys

def print_section(title, content):
    print("-"*50)
    print(f"{title}:\n{content}")

SOURCE = "https://www.youtube.com/watch?v=wioAFuHzcao"
LANGUAGE = "hi"

try:
    transcript = get_transcript(SOURCE, LANGUAGE)

except Exception as e:
    print(f"Processing failed: {e}")
    sys.exit(1)


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
    sys.exit(1)

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