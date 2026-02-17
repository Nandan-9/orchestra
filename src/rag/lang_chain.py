
import os

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from src.rag.chat_open_router import ChatOpenRouter 


load_dotenv()

def get_rag_chain():
    data_directory = "/home/das/pro/orchestra/src/scraped_data_manim"
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    vector_store_path = "/home/das/pro/orchestra/vector_store"

    if os.path.exists(f"{vector_store_path}/index.faiss") and os.path.exists(f"{vector_store_path}/index.pkl"):
        print("Loading existing vector store...")
        vector = FAISS.load_local(vector_store_path, embeddings, allow_dangerous_deserialization=True)
    else:
        print("Embedding documents...")
        loader = DirectoryLoader(data_directory, glob="**/*.txt", loader_cls=TextLoader)
        docs = loader.load()
        if not docs:
            raise ValueError("No documents found.")
        documents = text_splitter.split_documents(docs)
        vector = FAISS.from_documents(documents, embeddings)
        vector.save_local(vector_store_path)


    prompt = ChatPromptTemplate.from_template("""
    You are an expert Manim animation engineer.

    Your task:
    Write only the complete runnable Python code for the animation requested below.

    Rules:
    - DO NOT include Markdown code fences.
    - DO NOT include explanations, headers, or comments.
    - DO NOT include any text outside the Python code.
    - Output must begin directly with 'from manim import' or 'class ...' and nothing else.

    <context>
    {context}
    </context>

    User request:
    {input}

    Final instruction:
    Return only the clean, runnable Python code — no extra text or formatting.
    """)


    llm = ChatOpenRouter()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever(search_kwargs={"k": 3})
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    return retrieval_chain

# Only run embedding if executed directly
if __name__ == "__main__":
    chain = get_rag_chain()
    print("RAG chain ready!")
