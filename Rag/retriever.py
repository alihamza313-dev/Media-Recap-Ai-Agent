from langchain_chroma import Chroma

def get_retriever(vector_store : Chroma , k : int = 4):
    retriever =  vector_store.as_retriever(
        search_type = 'mmr',
        search_kwargs = {"k" : k ,
                         "fetch_k": 20,
                         "lambda_mult": 0.5 #for balanced diveristy and relevance or (minimum repitition) of chunks in response
                         },
    )
    return retriever