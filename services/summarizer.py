from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

from llm.model import build_chain


def create_summary(transcript : str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert AI assistant.
            Summarize the transcript into concise bullet points.
            Only include the main ideas.
            Do not add information that is not present.
            """
        ),
        (
            "human",
            """
            Transcript:
            {transcript}
            """
        )
    ])

    chain = build_chain(prompt)

    return chain.invoke({'transcript' : transcript})


def create_title(transcript: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert AI assistant.
            Read the transcript and generate a short title that accurately reflects the content of the transcript.
            Return only the title nothing else along with it.
            """
        ),
        (
            "human",
            """
            Transcript:
            {transcript}
            """
        )
    ])

    chain = build_chain(prompt)

    return chain.invoke({"transcript": transcript[:3000]})