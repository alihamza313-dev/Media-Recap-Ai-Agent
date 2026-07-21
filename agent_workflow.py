from core.transcriber import get_transcript
from Rag.rag_engine import rag_pipeline, ask_question
from services.summarizer import create_summary
from Rag.vector_store_collections import can_create_collection
from services.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)

from manager import check_existing_collection


def print_section(title, content):
    print("-"*50)
    print(f"{title}:\n{content}")


def analyze_media():

    if not can_create_collection():
        raise Exception("Maximum 5 meetings stored. Delete an existing collection first.")

    source = input("\nEnter YouTube URL or local file path: ").strip()

    #first check the collection is already exist into the vector store or not.then if it exist the simple get the collection metadata from the collection.json file by call function check_existing_collections which return the collection_metadata as dictionary.

    existing_collection = check_existing_collection(source=source)

    if existing_collection:
        print("======================[ Collection already exists ]======================")
        rag_chain,collection_name,title = rag_pipeline(existing_collection=existing_collection)

        print(f"\nStored collection: {collection_name}")
        print_section("Title", title)

    else:
        try:
            language = input("Enter language (en / hi): ").strip()
            transcript = get_transcript(source, language)

        except Exception as e:
            print(f"Processing failed: {e}")
            return

        try:
            rag_chain, collection_name, title = rag_pipeline(
                transcript=transcript,source=source
            )

            print(f"\nStored collection: {collection_name}")

            summary = create_summary(transcript)
            key_actions = extract_action_items(transcript)
            key_decisions = extract_key_decisions(transcript)
            questions = extract_questions(transcript)

        except Exception as e:
            print(f"RAG processing failed: {e}")
            return

        print_section("Title", title)
        print_section("Summary", summary)
        print_section("Key Actions", key_actions)
        print_section("Decision Points", key_decisions)
        print_section("Questions", questions)



    print('='*50)
    print("\n💬 Chat with your meeting (type 'exit' to quit)\n")

    while True:
        print('='*50)
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
