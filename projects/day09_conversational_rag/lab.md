# Day 09 Lab – Conversational RAG with Session Memory

## Objective

Build a conversational AI assistant that:

- Maintains conversation history
- Supports multiple users using session IDs
- Retrieves relevant documents from ChromaDB
- Generates answers using Ollama Chat API
- Streams responses
- Limits conversation history with a memory window

---

# Learning Outcomes

After completing this lab, you will be able to:

- Build a session manager
- Store conversation history
- Create multi-turn conversations
- Add streaming responses
- Explain enterprise chatbot architecture

---

# Project Structure

```
day09_conversational_rag/

│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── session_manager.py
│   ├── prompt_builder.py
│   ├── vector_store.py
│   ├── embedding_service.py
│   ├── llm_service.py
│   └── document_loader.py
│
├── chromadb/
├── data/
└── requirements.txt
```

---

# Lab 1 – Create a Session Manager

## Goal

Store conversation history for each user.

### Tasks

Create a `SessionManager` class.

Required methods:

```python
create_session(session_id)

get_history(session_id)

add_message(session_id, role, content)

clear_session(session_id)
```

### Expected Behaviour

```
Session A

↓

User
Assistant
User
Assistant

-----------------------

Session B

↓

User
Assistant
```

Each session must maintain an independent history.

---

# Lab 2 – Maintain Conversation History

Every time a user asks a question:

1. Add the user message.
2. Send the complete conversation to Ollama.
3. Receive the answer.
4. Store the assistant response.

Expected flow:

```
User

↓

Store User Message

↓

Retrieve History

↓

Ollama Chat API

↓

Store Assistant Message

↓

Return Response
```

---

# Lab 3 – Build Prompt Builder V2

Create a reusable Prompt Builder.

The prompt should contain:

```
System Prompt

↓

Conversation History

↓

Retrieved Documents

↓

Current User Question
```

Example system prompt:

```
You are an Enterprise IT Assistant.

Answer only using the supplied context.

If the answer is unavailable, say:

"I don't know."
```

---

# Lab 4 – Add Memory Window

Don't send unlimited history.

Keep only the latest 10 messages.

Example:

```
Message 1

Message 2

...

Message 25
```

Only send:

```
Message 16

↓

Message 25
```

### Why?

- Faster responses
- Lower token usage
- Reduced prompt size

---

# Lab 5 – Enable Streaming

Modify your LLM service.

Instead of waiting for the entire response,

stream tokens as they arrive.

Expected behaviour:

```
T

Th

The

The password

The password reset...
```

---

# Lab 6 – Modify the Chat API

Create:

```
POST /chat
```

Request:

```json
{
    "session_id": "abc123",
    "question": "How do I reset my password?"
}
```

Response:

```json
{
    "answer": "...",
    "sources": [
        "Password Policy"
    ]
}
```

---

# Lab 7 – Continue the Conversation

Call the same endpoint again.

Request:

```json
{
    "session_id": "abc123",
    "question": "How long does it take?"
}
```

Expected result:

The assistant understands that **"it"** refers to the password reset because conversation history is included.

---

# Bonus Challenge

Add a new endpoint:

```
DELETE /session/{session_id}
```

This endpoint should:

- Remove conversation history
- Create a fresh conversation

---

# Advanced Challenge

Instead of keeping only the last 10 messages,

summarise older messages.

Example:

Old conversation:

```
User asked about password reset.

Assistant explained the process.

User confirmed completion.
```

Replace 20 old messages with a short summary.

---

# Expected Architecture

```
                User
                  │
                  ▼
              FastAPI
                  │
                  ▼
          Session Manager
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
Conversation History    ChromaDB
        │                   │
        └─────────┬─────────┘
                  ▼
           Prompt Builder
                  │
                  ▼
          Ollama Chat API
                  │
                  ▼
          Streaming Answer
```

---

# Deliverables

By the end of this lab, your project should support:

- ✅ Multi-user conversations
- ✅ Session IDs
- ✅ Conversation memory
- ✅ Prompt Builder V2
- ✅ Streaming responses
- ✅ Memory window
- ✅ Enterprise architecture

---

# Self-Assessment Checklist

- [ ] I created a Session Manager.
- [ ] I can retrieve conversation history.
- [ ] I store both user and assistant messages.
- [ ] I implemented a memory window.
- [ ] My chatbot supports follow-up questions.
- [ ] I added streaming responses.
- [ ] I created a `/chat` endpoint.
- [ ] I can clear a session.
- [ ] I understand why session IDs are important.
- [ ] I can explain the architecture in an interview.

---

# Interview Questions

### Q1. Why do we need session IDs?

**Answer:** Session IDs uniquely identify each user's conversation, ensuring histories remain isolated in multi-user applications.

---

### Q2. Why store assistant messages?

**Answer:** Previous assistant responses provide context for follow-up questions, enabling coherent multi-turn conversations.

---

### Q3. Why use a memory window?

**Answer:** It limits the amount of conversation history sent to the model, reducing token usage, latency, and the risk of exceeding the model's context window.

---

### Q4. Why stream responses?

**Answer:** Streaming improves responsiveness by displaying generated text incrementally, creating a better user experience.

---

### Q5. Why separate the Prompt Builder from the LLM service?

**Answer:** Separating responsibilities makes the application easier to maintain, test, and extend. The Prompt Builder focuses on assembling context, while the LLM service only communicates with the model.

---

# Success Criteria

Congratulations! You have completed the lab successfully if:

- Your chatbot remembers previous questions.
- Different session IDs have separate conversation histories.
- The assistant answers follow-up questions correctly.
- Responses are streamed to the client.
- The application follows a clean, modular architecture suitable for enterprise development.