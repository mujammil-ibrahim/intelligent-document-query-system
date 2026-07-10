# 📄 Intelligent Document Query System

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions. The system retrieves the most relevant document sections using vector similarity search (pgvector) and generates accurate answers using a Large Language Model (LLM).

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic document chunking
- 🧠 Generate embeddings using Sentence Transformers
- 🔍 Semantic search with PostgreSQL + pgvector
- 🤖 AI-powered question answering using OpenRouter LLM
- 💬 Chat-style Streamlit interface
- 📑 Displays retrieved document chunks with similarity scores
- 🔄 Automatically replaces duplicate uploads of the same file

---

## 🏗️ System Architecture

```
                PDF Upload
                     │
                     ▼
            Text Extraction (PyMuPDF)
                     │
                     ▼
              Text Chunking
                     │
                     ▼
      Sentence Transformer Embeddings
                     │
                     ▼
      PostgreSQL + pgvector Database
                     │
         Semantic Similarity Search
                     │
                     ▼
          Relevant Document Chunks
                     │
                     ▼
        OpenRouter Large Language Model
                     │
                     ▼
             AI Generated Answer
                     │
                     ▼
            Streamlit User Interface
```

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- pgvector

### AI & NLP

- Sentence Transformers
- Hugging Face
- OpenRouter API
- GPT-OSS-20B (Free)

### Frontend

- Streamlit

### PDF Processing

- PyMuPDF (fitz)

---

## 📂 Project Structure

```
intelligent-document-query-system/

│
├── app/
│   ├── routers/
│   ├── models.py
│   ├── crud.py
│   ├── database.py
│   ├── embedding_utils.py
│   ├── pdf_utils.py
│   ├── search.py
│   ├── llm.py
│   ├── schemas.py
│   └── main.py
│
├── frontend.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/intelligent-document-query-system.git

cd intelligent-document-query-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=your_database_url
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=openai/gpt-oss-20b:free
```

---

### 5. Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

### 6. Start Streamlit Frontend

```bash
streamlit run frontend.py
```

Frontend URL

```
http://localhost:8501
```

---

## 📋 How It Works

1. Upload a PDF document.
2. The document text is extracted.
3. Text is split into semantic chunks.
4. Each chunk is converted into a vector embedding.
5. Embeddings are stored in PostgreSQL using pgvector.
6. User asks a question.
7. The question is embedded.
8. Similar chunks are retrieved using vector similarity search.
9. Retrieved context is sent to the LLM.
10. The LLM generates a context-aware answer.

---

## 📸 Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/

home.png

chat.png

retrieval.png
```

---

## 🔮 Future Improvements

- Multiple document support
- Document management dashboard
- Conversation history
- Hybrid search (Keyword + Semantic)
- User authentication
- Citation highlighting
- OCR support for scanned PDFs
- Cloud deployment with Docker

---

## 📦 Deployment

Backend: Render

Database: Supabase PostgreSQL + pgvector

Frontend: Streamlit

---

## 👨‍💻 Author

**Mujammil Ibrahim**

GitHub:
https://github.com/mujammil-ibrahim

LinkedIn:
https://linkedin.com/in/mujammil-ib

Email:
mujammilibrahim007@gmail.com

---

## 📄 License

This project is developed for educational and portfolio purposes.