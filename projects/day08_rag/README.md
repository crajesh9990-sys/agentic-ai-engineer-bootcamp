# Day 08 – Enterprise RAG Application using Ollama, ChromaDB & FastAPI

> **Agentic AI Engineer Bootcamp – Day 8**

## 📌 Project Overview

This project demonstrates a complete **Retrieval-Augmented Generation (RAG)** pipeline using:

- FastAPI
- Ollama
- ChromaDB
- nomic-embed-text
- Llama 3.2

Instead of relying only on the LLM's training data, the application retrieves relevant documents from a vector database and injects them into the prompt before generating an answer.

This is the foundation of most enterprise AI assistants used in IT support, HR, Legal, Banking, Healthcare, and Customer Support.

---

# Learning Objectives

After completing this project you will understand:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Embeddings
- ChromaDB
- Prompt Engineering
- Context Injection
- Enterprise AI Architecture
- FastAPI API Development
- Ollama Integration

---

# Architecture

```
                User
                  │
                  ▼
          FastAPI Endpoint
                  │
                  ▼
      Generate Query Embedding
                  │
                  ▼
             ChromaDB
                  │
                  ▼
       Retrieve Top-K Documents
                  │
                  ▼
          Prompt Builder
                  │
                  ▼
          Ollama (Llama 3.2)
                  │
                  ▼
          Grounded Response
                  │
                  ▼
               Client
```

---

# Project Structure

```
day08_rag/

│── app/
│   │── main.py
│   │── routes.py
│   │── models.py
│   │── embedding_service.py
│   │── vector_store.py
│   │── llm_service.py
│   │── prompt_builder.py
│   │── document_loader.py
│   │── config.py
│
│── chromadb/
│
│── data/
│   │── documents.json
│
│── requirements.txt
│── README.md
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| Ollama | Local LLM Runtime |
| Llama 3.2 | Large Language Model |
| nomic-embed-text | Embedding Model |
| ChromaDB | Vector Database |
| Pydantic | Request Validation |
| Uvicorn | ASGI Server |

---

# RAG Pipeline

```
User Question

↓

Embedding Model

↓

Vector Database

↓

Top-K Retrieval

↓

Prompt Builder

↓

LLM

↓

Grounded Answer
```

---

# Prerequisites

- Python 3.11+
- Ollama Installed
- Git
- VS Code (Recommended)

---

# Install Required Models

## Pull Llama 3.2

```bash
ollama pull llama3.2
```

## Pull Embedding Model

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

Expected output:

```
llama3.2
nomic-embed-text
```

---

# Installation

Clone repository

```bash
git clone <repository-url>
```

Move into project

```bash
cd day08_rag
```

Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Run Ollama

Start Ollama (if it is not already running):

```bash
ollama serve
```

---

# Run the Application

```bash
uvicorn app.main:app --reload
```

Application URL

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# API

## POST /ask

### Request

```json
{
    "question": "How do I reset my password?"
}
```

---

### Response

```json
{
    "question": "How do I reset my password?",
    "answer": "Visit password.company.com to reset your password.",
    "sources": [
        "Password Reset",
        "VPN Access"
    ],
    "retrieval": [
        {
            "title": "Password Reset",
            "distance": 0.08,
            "preview": "To reset your password visit password.company.com..."
        },
        {
            "title": "VPN Access",
            "distance": 0.62,
            "preview": "Install Global Protect VPN..."
        }
    ]
}
```

---

# Example Workflow

1. User asks a question.
2. Generate query embedding.
3. Search ChromaDB.
4. Retrieve Top-K documents.
5. Build a prompt using the retrieved context.
6. Send the prompt to Llama 3.2.
7. Return the generated answer with document sources.

---

# Key Components

## Embedding Service

Converts text into vector embeddings using **nomic-embed-text**.

---

## Vector Store

Stores and retrieves embeddings using ChromaDB.

---

## Prompt Builder

Builds a structured prompt containing:

- Instructions
- Retrieved documents
- User question

---

## LLM Service

Sends the prompt to **Llama 3.2** via Ollama and returns the generated response.

---

## Document Loader

Loads sample documents into ChromaDB during application startup.

---

# Enterprise Best Practices

- Use low temperature (0–0.2) for factual responses.
- Return source documents with every answer.
- Store embeddings in a persistent vector database.
- Keep prompts concise and focused.
- Retrieve only the Top-K relevant documents.
- Use metadata for filtering.
- Cache embeddings where appropriate.
- Avoid exposing sensitive document content.

---

# Common Interview Questions

### What is RAG?

Retrieval-Augmented Generation combines semantic retrieval with LLM-based text generation to produce grounded responses using external knowledge.

---

### Why use ChromaDB?

ChromaDB stores vector embeddings and enables semantic similarity search for efficient document retrieval.

---

### Why use embeddings?

Embeddings convert text into numerical vectors that capture semantic meaning, enabling similarity search.

---

### What is Context Injection?

Context Injection is the process of inserting retrieved documents into the LLM prompt before generating a response.

---

### Why return sources?

Returning sources improves transparency, allows users to verify answers, and increases trust in AI-generated responses.

---

# Future Improvements

- Multi-turn conversations
- Conversation memory
- Session management
- Streaming responses
- PDF ingestion
- DOCX support
- Metadata filtering
- Hybrid search
- Re-ranking
- Authentication
- Role-based access control
- React frontend
- Source highlighting
- Response caching

---

# Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- FastAPI Development
- Ollama Integration
- Prompt Engineering
- Semantic Search
- ChromaDB
- Embedding Models
- Vector Databases
- Enterprise AI Design
- REST API Development

---

# Git Commands

```bash
git checkout -b day08-rag

git add .

git commit -m "Day 08 - Enterprise RAG Application"

git push origin day08-rag
```

---

# Next Steps

In **Day 09**, this project will be enhanced with:

- Conversational Memory
- Multi-turn Chat
- Session Management
- Streaming Responses
- React Chat UI
- AI Agent Fundamentals

The application will evolve into a **ChatGPT-style Enterprise AI Assistant**.

---

# Author

**Rajesh Choudary**

Agentic AI Engineer Bootcamp – 140 Day Roadmap

Building enterprise-grade AI applications with FastAPI, Ollama, ChromaDB, React, and modern AI architectures.

---

# License

This project is intended for learning, portfolio development, and interview preparation.