from llm.model import build_chain
from Rag.vector_store import build_vectorStore,get_vectorStore
from Rag.retriever import get_retriever
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.prompts import ChatPromptTemplate



def format_docs(docs : list)->str:
    return "\n\n".join(doc.page_content for doc in docs)

def rag_pipeline(transcript : str = None , collection_name : str = None , store : bool = False):
    if store and not collection_name:
        raise ValueError(
            "collection_name is required when loading an existing collection"
        )

    if store:
        vector_store = get_vectorStore(collection_name)

    else:
        vector_store, collection_name, title = build_vectorStore(transcript)

    #this is beacuse at the very time when we loaded the transcript we use to build vector store beacuse we have to create mbeddings of this transcipt and then store it into the vector store and then after all when ever i have to perform functions like suppose i want to retrieve documents from the vector store based on some query then we do not build vector store we simply get it and then use its function vector_store.as_retriever and simply get documents.

    retriever = get_retriever(vector_store , k = 4) 

    #basically we get a retiever and it is a runnable and we can call it by using .invoke() function and pass a question into it and the it retrieve automatically the relevant chunks according to the instructions from the vector store.but here we use LCEL chains so we just pass it in chain and when we call the chain it automatically start working and in these chains the previous output act as the input for the next. 

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an expert meeting assistant. Answer the user's question based ONLY on the meeting transcript context provided below.

    If the answer is not found in the context, say:
    "I could not find this information in the meeting transcript."

    Always be concise and precise. If quoting someone, mention it clearly.

    Context from meeting transcript:
    {context}
    """,
            ),
            ("human", "{question}"),
        ]
    )

    chain1 = RunnableParallel(
        {
            'context' : retriever | RunnableLambda(format_docs),
            'question' : RunnablePassthrough()
        }
    )

    chain2 = build_chain(prompt)

    final_chain = chain1 | chain2

    return final_chain,collection_name,title


def ask_question(rag_chain , question : str)->str:
    print("="*50)
    response = rag_chain.invoke(question)
    return response