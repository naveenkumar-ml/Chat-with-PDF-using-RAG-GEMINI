📄 RAG PDF Chatbot (LangChain + Gemini + Streamlit)
🚀 Overview
This project is a Retrieval-Augmented Generation (RAG) based PDF Chatbot that allows users to upload multiple PDF files and ask questions based on their content.
The application uses:
•	LangChain for orchestration
•	Google Gemini (LLM) for answer generation
•	HuggingFace Embeddings for vector representation
•	ChromaDB as the vector database
•	Streamlit for UI
________________________________________
🧠 RAG Architecture
The system follows a standard RAG pipeline:
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
________________________________________
⚙️ Features
•	📄 Upload multiple PDF files
•	🔍 Semantic search using embeddings
•	🤖 Accurate answers using Gemini LLM
•	📚 Source document visibility
•	⚡ Fast processing with caching
•	🔄 Automatic vector DB reset on each run
________________________________________
🏗️ Tech Stack
Component	Technology Used
Frontend	Streamlit
LLM	Google Gemini (gemini-2.5-flash)
Embeddings	sentence-transformers/all-MiniLM-L6-v2
Vector DB	ChromaDB
Framework	LangChain
________________________________________
📂 Project Structure
project/
│── app.py
│── .env
│── chroma_db/   (auto-generated)
________________________________________
🔑 Environment Setup
Create a .env file and add your API key:
GOOGLE_API_KEY=your_api_key_here
________________________________________
▶️ Installation & Run
1. Install dependencies
pip install streamlit langchain langchain-community langchain-google-genai chromadb sentence-transformers python-dotenv
2. Run the app
streamlit run app.py
________________________________________
🔄 Workflow Explanation
1. PDF Processing
•	PDFs are uploaded
•	Stored temporarily
•	Loaded using PyPDFLoader
2. Text Chunking
•	Split into chunks (size=400, overlap=100)
•	Helps better retrieval accuracy
3. Embeddings Creation
•	Converts text chunks into vectors
4. Vector Database
•	Stored in ChromaDB
•	Old DB is deleted and recreated every run
5. Retrieval
•	Uses MMR (Max Marginal Relevance)
•	Fetches top 3 relevant chunks
6. Answer Generation
•	Gemini LLM generates answer using retrieved context
________________________________________
📌 Key Highlights
•	Prevents hallucination using context-based answers
•	Uses lightweight embedding model for speed
•	Efficient retrieval with MMR strategy
•	Clean UI for better user experience
________________________________________
⚠️ Limitations
•	Works only with text-based PDFs
•	Large PDFs may take time to process
•	Requires valid Google API key
________________________________________
🔮 Future Improvements
•	Add chat history (memory)
•	Support for other file types (DOCX, TXT)
•	Deploy using Docker or cloud
•	Add authentication
________________________________________
🤝 Contributing
Feel free to fork this repo and improve the project.

                                                                                                      Naveenkumar Adanapattu

