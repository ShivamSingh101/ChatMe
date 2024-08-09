import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain


import dotenv import load_dotenv
load_dotenv()


#groq api key
groq_api_key="xyz"

if "vector" not in st.session_state:


st.title("ChatGroq Demo")
model=ChatGroq(groq_api_key , model_name="Gemma-&b-It")

prompt=ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Question:{input}
     """
)
document_chain=create_stuff_documents_chain(model,prompt)