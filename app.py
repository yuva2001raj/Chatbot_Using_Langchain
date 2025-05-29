import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from tenacity import retry, wait_exponential, stop_after_attempt
from google.api_core.exceptions import ResourceExhausted

load_dotenv()


os.environ["GOOGLE_API_KEY"] = "AIzaSyDRQoF-bJIqoBE8rn02dENYbS4Sv1eRJIE"
os.environ["LANGCHAIN_API_KEY"] = "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"

#initiate the google gemini model
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash", # Model name
    temperature = 0,
    max_tokens = None,
    timeout = None,
    max_retries = 2
)

prompt = ChatPromptTemplate(
    [
        ("system","you are a chatbot"),
        ("human", "Question:{question}")
    ]
)

st.title("💬 Chatbot Using Langchain")
input_text = st.text_input("Enter the question")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser



if input_text:
    with st.spinner("Thinking..."):
        st.write(chain.invoke({"question":input_text}))