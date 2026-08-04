# Day 09 Project
# Enterprise Conversational RAG Assistant

## Project Overview

In this project, you will build an Enterprise Conversational AI Assistant.

Unlike the Day 8 project, this assistant remembers previous conversations, allowing users to ask follow-up questions naturally.

Example:

User:

```
How do I reset my password?
```

Assistant:

```
Visit password.company.com.
```

User:

```
How long does it take?
```

The assistant understands that **"it"** refers to the password reset.

---

# Project Objectives

Build a chatbot that can:

- Maintain conversation history
- Support multiple sessions
- Retrieve relevant company documents
- Generate context-aware responses
- Stream responses
- Return document sources

---

# Technologies Used

- Python
- FastAPI
- Ollama
- ChromaDB
- Pydantic
- Uvicorn

---

# Project Structure

```
day09_conversational_rag/

│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── session_manager.py
│   ├── prompt_builder.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   ├── llm_service.py
│   ├── document_loader.py
│   └── utils.py
│
├── data/
│   └── company_documents.json
│
├── chromadb/
│
├── requirements.txt
│
└── README.md
```

---

# Architecture

```
                    User

                      │

                      ▼

                  FastAPI

                      │

                      ▼

               Session Manager

          ┌───────────┴────────────┐

          ▼                        ▼

 Conversation History          Embedding Service

          │                        │

          ▼                        ▼

      Prompt Builder         ChromaDB Search

               │                  │

               └──────────┬───────┘

                          ▼

                    Ollama Chat API

                          │

                          ▼

                   Streaming Answer

                          │

                          ▼

                     Store Response
```

---

# Functional Requirements

The application must support:

### 1. Session Management

Every user receives a unique Session ID.

Example

```
abc123
```

Conversation history is stored separately for each session.

---

### 2. Document Retrieval

Before generating an answer,

retrieve the most relevant documents from ChromaDB.

Return Top 3 results.

---

### 3. Prompt Building

The prompt should include:

- System Prompt
- Conversation History
- Retrieved Context
- Current Question

---

### 4. LLM Integration

Use

```
ollama.chat()
```

instead of

```
ollama.generate()
```

---

### 5. Conversation Memory

Store

- User messages
- Assistant messages

for every session.

---

### 6. Memory Window

Keep only

```
Last 10 Messages
```

Older messages are ignored.

---

### 7. Streaming

Responses should stream back to the client.

---

### 8. Source Attribution

Return

```json
{
    "answer": "...",
    "sources": [
        "Password Policy",
        "Leave Policy"
    ]
}
```

---

# API Endpoints

## POST /chat

Request

```json
{
    "session_id": "abc123",
    "question": "How do I reset my password?"
}
```

Response

```json
{
    "answer": "...",
    "sources": [
        "Password Policy"
    ]
}
```

---

## DELETE /session/{session_id}

Deletes conversation history.

Response

```json
{
    "message": "Session cleared successfully."
}
```

---

## GET /session/{session_id}

Returns stored conversation.

Example

```json
[
    {
        "role":"user",
        "content":"Reset password"
    },
    {
        "role":"assistant",
        "content":"Visit password.company.com."
    }
]
```

---

# Workflow

```
Receive Request

↓

Validate Session

↓

Retrieve Conversation

↓

Generate Embedding

↓

Search ChromaDB

↓

Build Prompt

↓

Call Ollama

↓

Store Assistant Response

↓

Return Response
```

---

# Sample Conversation

Request

```
Reset my password
```

Assistant

```
Visit password.company.com.
```

Second request

```
How long does it take?
```

Assistant

```
The password reset usually completes within five minutes.
```

The chatbot correctly understands the context.

---

# Testing Scenarios

## Scenario 1

Ask

```
What is the leave policy?
```

Expected

Relevant HR policy.

---

## Scenario 2

Ask

```
Can I carry it forward?
```

Expected

The assistant understands that "it" means annual leave.

---

## Scenario 3

Create another Session ID.

Ask

```
How do I connect to VPN?
```

Expected

The second user should not see the first user's history.

---

## Scenario 4

Delete Session.

Ask

```
What did I ask before?
```

Expected

No conversation history exists.

---

# Enterprise Improvements

Future versions can include:

- Redis for session storage
- PostgreSQL for persistent conversations
- JWT Authentication
- Role-based Access Control (RBAC)
- Conversation summarisation
- Token usage monitoring
- Prompt versioning
- Audit logging
- Rate limiting

---

# Coding Standards

Follow these principles:

- Single Responsibility Principle (SRP)
- Dependency Injection
- Modular architecture
- Type hints
- Pydantic validation
- Logging
- Exception handling

---

# Interview Questions

## Q1. Why use Chat API instead of Generate API?

**Answer**

The Chat API supports structured messages with system, user, and assistant roles, enabling multi-turn conversations and conversation memory.

---

## Q2. Why do we need a Session Manager?

**Answer**

A Session Manager isolates conversation history for each user, ensuring context is maintained without mixing conversations.

---

## Q3. Why use a Prompt Builder?

**Answer**

It centralises prompt creation, making it easier to maintain and ensuring all required context is consistently included.

---

## Q4. Why limit the memory window?

**Answer**

Limiting conversation history reduces token usage, improves response time, and avoids exceeding the model's context limit.

---

## Q5. How would you scale this application?

**Answer**

Replace the in-memory session manager with Redis, store long-term history in PostgreSQL, deploy multiple FastAPI instances behind a load balancer, and use a shared vector database.

---

# Project Deliverables

By the end of this project, you should have:

- ✅ Multi-turn conversational chatbot
- ✅ Session management
- ✅ Conversation memory
- ✅ ChromaDB integration
- ✅ Prompt Builder
- ✅ Streaming responses
- ✅ Source attribution
- ✅ Clean, modular architecture

---

# AI Architect Notes

This project demonstrates several enterprise AI engineering concepts:

- Retrieval-Augmented Generation (RAG)
- Conversation state management
- Prompt engineering
- Service-layer architecture
- API design
- Context management
- Scalable application structure

These are common topics in Senior AI Engineer and AI Architect interviews.

---

# Project Summary

Congratulations!

You have evolved your application through the roadmap:

- **Day 6:** Semantic Search
- **Day 7:** ChromaDB Vector Database
- **Day 8:** Enterprise RAG
- **Day 9:** Enterprise Conversational RAG

You now have a strong foundation for **Day 10**, where you'll transform this conversational assistant into an **AI Agent** by introducing tool calling, planning, and autonomous decision-making.