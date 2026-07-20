from Rag.vector_store_collections import list_collections,delete_collection
import sys
from agent_workflow import analyze_media

def show_menu():

    while True:

        print("\n================================ Media Recap AI ================================")
        print("1. Analyze Media")
        print("2. View Collections")
        print("3. Delete Collection")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            analyze_media()

        elif choice == "2":
            list_collections()

        elif choice == "3":

            collection = input(
                "Enter collection name to delete: "
            ).strip()

            delete_collection(collection)

        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid option.")
