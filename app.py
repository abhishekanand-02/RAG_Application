import streamlit as st
import time
import asyncio
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

st.title("RAG Application built on Gemini Model")

# Set up asyncio policy for Windows
if os.name == 'nt':  # Windows
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

@st.cache_resource
def initialize_components():
    """Initialize and cache the RAG components"""
    try:
        # Ensure we have an event loop
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        # Load and split documents
        loader = PyPDFLoader("GOT-OCR-2.0-paper.pdf")
        data = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
        docs = text_splitter.split_documents(data)
        
        # Initialize embeddings and vectorstore
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
        
        # Create retriever
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
        
        # Initialize LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            max_tokens=None,
            timeout=None
        )
        
        return retriever, llm
    except Exception as e:
        st.error(f"Error initializing components: {str(e)}")
        return None, None


# Initialize components
retriever, llm = initialize_components()

if retriever is None or llm is None:
    st.error("Failed to initialize RAG components. Please check your API keys and try again.")
    st.stop()

query = st.chat_input("Say something: ")

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

if query:
    try:
        with st.spinner("Processing your query..."):
            question_answer_chain = create_stuff_documents_chain(llm, prompt)
            rag_chain = create_retrieval_chain(retriever, question_answer_chain)
            
            response = rag_chain.invoke({"input": query})
            st.write(response["answer"])
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")
        st.info("Please try again or check your internet connection.")

