from langchain_groq import ChatGroq

from dotenv import load_dotenv

import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)