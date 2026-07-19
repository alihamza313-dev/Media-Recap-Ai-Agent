from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(transcript : str)->list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1500,
        chunk_overlap = 50,
    )

    return splitter.split_text(transcript)