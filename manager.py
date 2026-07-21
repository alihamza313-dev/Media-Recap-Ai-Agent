import json
import os

COLLECTION_FILE = "collections.json"

def check_existing_collection(source : str)->dict | None:
    try:
        with open(COLLECTION_FILE, "r") as file:
            collections = json.load(file)
            
    except (FileNotFoundError , json.JSONDecodeError):
        return None

    for c in collections:
        if c["source"] == source:
            return c
        
    return None