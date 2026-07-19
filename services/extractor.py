from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

from llm.model import build_chain



def extract_action_items(transcript: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert AI assistant.

            Extract all action items mentioned in the transcript.

            - Return the results as bullet points.
            - Include only explicit action items.
            - If no action items exist, return:
              "No action items found."
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

    return chain.invoke({"transcript": transcript})


def extract_key_decisions(transcript: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert AI assistant.

            Extract all important decisions mentioned in the transcript.

            - Return the results as bullet points.
            - Include only decisions that were clearly made.
            - If no decisions are mentioned, return:
              "No key decisions found."
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

    return chain.invoke({"transcript": transcript})


def extract_questions(transcript: str):
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert AI assistant.

            Extract all questions asked or discussed in the transcript.

            - Return the questions as bullet points.
            - If no questions are present, return:
              "No questions found."
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

    return chain.invoke({"transcript": transcript})