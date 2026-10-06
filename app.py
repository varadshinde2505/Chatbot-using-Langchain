import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Find the folder where app.py is located
BASE_DIR = Path(__file__).resolve().parent

# Explicitly load .env from the same folder as app.py
ENV_FILE = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_FILE)

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="LangChain ChatBot",
    page_icon="🌍"
)

st.title("🌍 LangChain ChatBot")


# Debug check
if not api_key:
    st.error(f"OPENAI_API_KEY not found!")
    st.write(f"Looking for .env at: `{ENV_FILE}`")
    st.write(f"Does .env exist? `{ENV_FILE.exists()}`")
    st.stop()


# Create LLM
llm = ChatOpenAI(
    model="gpt-6-luna",
    api_key=api_key
)


def get_openai_response(query):
    response = llm.invoke(query)
    return response.content


user_input = st.text_input(
    "Enter your query here",
    key="user_input"
)


if user_input:
    response = get_openai_response(user_input)
    st.write(response)