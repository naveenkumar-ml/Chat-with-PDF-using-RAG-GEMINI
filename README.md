# 📄 RAG PDF Chatbot (LangChain + Gemini + Streamlit)

## 🚀 Overview

This project is a **Retrieval-Augmented Generation (RAG) based PDF Chatbot** that allows users to upload multiple PDF files and ask questions based on their content.

The application uses:

* **LangChain** for orchestration
* **Google Gemini (LLM)** for answer generation
* **HuggingFace Embeddings** for vector representation
* **ChromaDB** as the vector database
* **Streamlit** for UI

---

## 🧠 RAG Architecture

The system follows a standard RAG pipeline:

```
User Query
    ↓
PDF Upload
    ↓
Document Loader (PyPDFLoader)
    ↓
Text Splitting (RecursiveCharacterTextSplitter)
    ↓
Embeddings (HuggingFace)
    ↓
Vector Database (ChromaDB)
    ↓
Retriever (MMR Search)
    ↓
LLM (Gemini)
    ↓
Final Answer + Source Documents
```

---

## ⚙️ Features

* 📄 Upload multiple PDF files
* 🔍 Semantic search using embeddings
* 🤖 Accurate answers using Gemini LLM
* 📚 Source document visibility
* ⚡ Fast processing with caching
* 🔄 Automatic vector DB reset on each run

---

## 🏗️ Tech Stack

| Component  | Technology Used                        |
| ---------- | -------------------------------------- |
| Frontend   | Streamlit                              |
| LLM        | Google Gemini (gemini-2.5-flash)       |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB  | ChromaDB                               |
| Framework  | LangChain                              |

---

## 📂 Project Structure

```
project/
│── app.py
│── .env
│── chroma_db/   (auto-generated)
```

---

## 🔑 Environment Setup

Create a `.env` file and add your API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Installation & Run

### 1. Install dependencies

```
pip install streamlit langchain langchain-community langchain-google-genai chromadb sentence-transformers python-dotenv
```

### 2. Run the app

```
streamlit run app.py
```

---

## 🔄 Workflow Explanation

### 1. PDF Processing

* PDFs are uploaded
* Stored temporarily
* Loaded using PyPDFLoader

### 2. Text Chunking

* Split into chunks (size=400, overlap=100)
* Helps better retrieval accuracy

### 3. Embeddings Creation

* Converts text chunks into vectors

### 4. Vector Database

* Stored in ChromaDB
* Old DB is deleted and recreated every run

### 5. Retrieval

* Uses MMR (Max Marginal Relevance)
* Fetches top 3 relevant chunks

### 6. Answer Generation

* Gemini LLM generates answer using retrieved context

---

## 📌 Key Highlights

* Prevents hallucination using context-based answers
* Uses lightweight embedding model for speed
* Efficient retrieval with MMR strategy
* Clean UI for better user experience

---

## ⚠️ Limitations

* Works only with text-based PDFs
* Large PDFs may take time to process
* Requires valid Google API key

---

## 🔮 Future Improvements

* Add chat history (memory)
* Support for other file types (DOCX, TXT)
* Deploy using Docker or cloud
* Add authentication

---

## 🤝 Contributing

Feel free to fork this repo and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
