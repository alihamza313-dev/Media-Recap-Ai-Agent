from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from Rag.splitter import split_text

from Rag.vector_store_collections import create_collection_name,save_collection,can_create_collection
from services.summarizer import create_title

CHROMA_DIR = "Vector_db"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def get_embeddings():
    return embeddings


def build_vectorStore(transcript : str)->tuple[Chroma, str]:
    chunks = split_text(transcript)

    docs = [Document(page_content=chunk , metadata = {'chunk_id' : i}) for i , chunk in enumerate(chunks)]

    if not can_create_collection():
        raise Exception("Maximum 5 meetings stored. Delete an existing collection first.")
    
    title = create_title(transcript)
    collection_name = create_collection_name(title)

    vector_store = Chroma.from_documents(
        documents = docs,
        embedding = get_embeddings(),
        collection_name= collection_name,
        persist_directory=CHROMA_DIR,
    )
    save_collection(title , collection_name)

    return vector_store, collection_name,title


def get_vectorStore(collection_name:str)->Chroma:
    embeddings = get_embeddings()

    vector_store = Chroma(
        embedding_function= embeddings,
        collection_name= collection_name,
        persist_directory=CHROMA_DIR,
    )

    return vector_store
