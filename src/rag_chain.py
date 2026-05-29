from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.prompts import RAG_PROMPT

import os
from dotenv import load_dotenv


load_dotenv()


def create_rag_chain():

    llm = ChatGroq(

        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"

    )


    prompt = ChatPromptTemplate.from_template(RAG_PROMPT)


    chain = prompt | llm

    return chain