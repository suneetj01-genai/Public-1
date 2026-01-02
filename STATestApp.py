import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

Prompt = ChatPromptTemplate.from_messages(
    [ ("system", "You are a helpful assistant that translates English to Hindi. Convert text into Hindi and Telgu language."),
     ("user", "Question: {question}")
    
    ]
)


# Title
st.title("Test Chat Bot")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")
input_text=st.text_input("Enter your text here")
llm = Ollama(model="gemma:2b", temperature=0.7)
output_parser=StrOutputParser()
chain=Prompt | llm | output_parser
if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)
