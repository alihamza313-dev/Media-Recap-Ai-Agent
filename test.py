import json
import os
COLLECTION_FILE = "collections.json"

def list_collections():
    if not os.path.exists(COLLECTION_FILE):
        return []

    with open(COLLECTION_FILE, "r") as f:
        collections =  json.load(f)
    
    for i , c in enumerate(collections):
        print(f"{i} : \n Title : {c['title']} \n Collection_name : {c['collection_name']}")


if __name__ == "__main__":
    list_collections()