from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
def get_llm():
    llm = ChatMistralAI(model = "mistral-small-latest" , mistral_api_key = MISTRAL_API_KEY)
    return llm


def build_chain(prompt : ChatPromptTemplate):
    llm = get_llm()
    parser = StrOutputParser()

    return prompt | llm | parser