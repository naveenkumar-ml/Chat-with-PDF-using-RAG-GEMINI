import shutil

import streamlit as st
import os
import tempfile
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

from dotenv import load_dotenv
load_dotenv()

# LangChain imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# ---------------- UI ---------------- #
st.set_page_config(page_title="RAG PDF Chatbot", layout="wide")
st.title("📄 Chat with Your PDFs (RAG + Gemini)")

# ---------------- API KEY ---------------- #
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ Please set GOOGLE_API_KEY in .env file")
    st.stop()

# ---------------- FILE UPLOAD ---------------- #
uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------- PROCESS PDFs ---------------- #
@st.cache_data(show_spinner=False)
def process_pdfs(_files):
    documents = []

    for file in _files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=100
    )

    texts = splitter.split_documents(documents)
    return texts

# ---------------- CREATE VECTOR DB ---------------- #
@st.cache_resource
def create_db(_texts):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # ✅ Stable persistent DB (no UUID issues)
    persist_dir = "chroma_db"

    # 🔥 DELETE OLD DB BEFORE CREATING NEW ONE
    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir)

    vectordb = Chroma.from_documents(
        documents=_texts,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    vectordb.persist()
    return vectordb

# ---------------- CREATE QA CHAIN ---------------- #
@st.cache_resource
def create_qa(_vectordb):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.1,
        convert_system_message_to_human=True
    )

    retriever = _vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain

# ---------------- MAIN APP ---------------- #
if uploaded_files:

    with st.spinner("📄 Processing PDFs..."):
        texts = process_pdfs(uploaded_files)
        st.success(f"✅ Created {len(texts)} chunks")

    with st.spinner("🧠 Building vector database..."):
        vectordb = create_db(texts)

    qa_chain = create_qa(vectordb)

    query = st.text_input("💬 Ask a question from your PDFs:")

    if query:
        with st.spinner("🤖 Thinking..."):
            result = qa_chain.invoke({"query": query})

        st.subheader("📌 Answer")
        st.write(result["result"])

        st.subheader("📚 Source Documents")
        with st.expander("Show sources"):
            for doc in result["source_documents"]:
                st.write(doc.page_content[:500])
                st.write("---")

else:
    st.info("👆 Upload PDFs to start chatting")