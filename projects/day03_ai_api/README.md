# 🤖 Day 03 – AI REST API using FastAPI & Ollama

This project demonstrates how to build a RESTful AI service using **FastAPI** and a **local Large Language Model (LLM)** powered by **Ollama**.

The API exposes endpoints that interact with an LLM through a clean service layer, making it easy to extend with additional AI capabilities.

---

## 📌 Features

- FastAPI REST API
- Interactive Swagger UI
- Local LLM integration using Ollama
- Pydantic request/response models
- Clean layered architecture
- Health check endpoint
- AI-powered prompt endpoint

---

## 🏗 Architecture

```text
Client
   │
   ▼
FastAPI REST API
   │
   ▼
Service Layer
   │
   ▼
Ollama
   │
   ▼
Llama 3.2
```

---

## 📂 Project Structure

```text
day03_ai_api/

├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   └── ai_service.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙ Prerequisites

- Python 3.12+
- Ollama
- Llama 3.2 model
- Git

---

## 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to project

```bash
cd day03_ai_api
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

```bash
ollama run llama3.2
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Swagger UI

Open

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET**

```
/health
```

Response

```json
{
  "status": "UP"
}
```

---

### Ask AI

**POST**

```
/ask
```

Request

```json
{
  "prompt": "Explain FastAPI."
}
```

Response

```json
{
  "response": "FastAPI is..."
}
```

---

## Technologies Used

- Python
- FastAPI
- Ollama
- Llama 3.2
- Requests
- Pydantic
- Uvicorn

---

## Skills Demonstrated

- REST API Development
- AI Integration
- Prompt Handling
- API Design
- Layered Architecture
- Local LLM Development
- Swagger/OpenAPI

---

## Future Enhancements

- Authentication
- Streaming responses
- Conversation history
- Prompt templates
- LangChain integration
- RAG support
- Vector Database
- Docker support

---

## Author

Rajesh

Agentic AI Engineer Bootcamp

Day 03