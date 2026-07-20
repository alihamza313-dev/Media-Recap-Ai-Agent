import json
import os
import re
import uuid
from langchain_chroma import Chroma


COLLECTION_FILE = "collections.json"

MAX_COLLECTIONS = 5

def can_create_collection():

    if not os.path.exists(COLLECTION_FILE):
        return True
    try:
        with open(COLLECTION_FILE, "r") as f:
            collections = json.load(f)
    except:
        collections = []

    return len(collections) < MAX_COLLECTIONS


def create_collection_name(title: str):

    safe_title = re.sub(
        r"[^a-zA-Z0-9_-]+",
        "_",
        title
    ).strip("_")

    return f"{safe_title}_{uuid.uuid4().hex[:8]}"


def save_collection(title:str ,collection_name: str):
    collections = []

    # Load existing collections
    if os.path.exists(COLLECTION_FILE):
        with open(COLLECTION_FILE, "r") as f:
            collections = json.load(f)

    # Add new collection
    collections.append(
        {
            'title' : title,
            "collection_name" : collection_name,
        }
        )

    # Save updated list
    with open(COLLECTION_FILE, "w") as f:
        json.dump(collections, f, indent=4)


def list_collections():
    if not os.path.exists(COLLECTION_FILE):
        return []

    with open(COLLECTION_FILE, "r") as f:
        collections =  json.load(f)
    
    for i , c in enumerate(collections):
        print(f"{i} : \n Title : {c['title']} \n Collection_name : {c['collection_name']}")


def delete_collection(collection_name):
    if not os.path.exists(COLLECTION_FILE):
        print("No Collection file found")
        return
    with open(COLLECTION_FILE, "r") as f:
        collections = json.load(f)

    not_found = True
    for c in collections:
        if c["collection_name"] == collection_name:
            not_found = False
            break

    if not_found:
        print("No Collection exist of this name")
        return
    
    vector_store = Chroma(
        collection_name=collection_name,
        persist_directory="Vector_db"
    )

    vector_store.delete_collection()
    remove_Collection_name(collection_name)


def remove_Collection_name(collection_name):

    if not os.path.exists(COLLECTION_FILE):
        return
    
    with open("collections.json", "r") as f:
        collections = json.load(f)

    collections = [
        c for c in collections
        if c["collection_name"] != collection_name
    ]

    with open("collections.json", "w") as f:
        json.dump(collections, f, indent=4)