# Day 09 – Conversational RAG & Memory
## Agentic AI Engineer Bootcamp

**Duration:** 2 Hours

**Difficulty:** ⭐⭐⭐⭐☆

**Project:** Enterprise AI Assistant with Conversation Memory

---

# Learning Objectives

After completing today's study material, you will be able to:

- Understand Conversational AI
- Explain Stateless vs Stateful AI
- Implement Conversation Memory
- Build Session Management
- Design Enterprise Chatbots
- Understand Prompt Templates
- Implement Streaming Responses
- Explain Multi-turn Conversations
- Answer Day 9 Interview Questions

---

# Introduction

On Day 8, you built a Retrieval-Augmented Generation (RAG) application.

However, there was one limitation.

Every request was independent.

Example:

User:

```
How do I reset my password?
```

AI:

```
Visit password.company.com
```

Then the user asks

```
What if I forgot my username?
```

The AI has forgotten the previous question.

This is because the application is **stateless**.

Today's objective is to make it conversational.

---

# What is Conversational AI?

Conversational AI refers to systems that can maintain context across multiple interactions.

Instead of treating every request independently, the system remembers previous messages.

Examples include:

- ChatGPT
- Claude
- Microsoft Copilot
- Gemini
- Enterprise Helpdesk Bots

---

# Single-turn vs Multi-turn Conversations

## Single-turn

```
Question

↓

Answer
```

Each request is independent.

---

## Multi-turn

```
User

↓

Assistant

↓

User

↓

Assistant

↓

User

↓

Assistant
```

The AI understands the entire conversation.

---

# Why Conversation Memory?

Without memory

User

```
I forgot my password.
```

AI

```
Visit password.company.com
```

User

```
How long does it take?
```

The AI doesn't know what "it" refers to.

---

With memory

The AI remembers the previous conversation.

It understands that "it" means **password reset**.

---

# Stateless vs Stateful AI

## Stateless

Every request is independent.

```
Request 1

↓

AI

↓

Response
```

```
Request 2

↓

AI

↓

Response
```

No history.

---

### Advantages

- Easy to scale
- Simple architecture
- Less memory usage

---

### Disadvantages

- No conversation history
- Poor user experience

---

## Stateful

```
Conversation History

↓

Current Question

↓

LLM

↓

Response
```

The AI remembers previous messages.

---

### Advantages

- Better conversations
- Follow-up questions
- Natural interaction

---

### Disadvantages

- Requires memory
- Session management
- More storage

---

# Conversation Memory

Conversation memory stores previous interactions.

Example

```
User

↓

Hello

↓

Assistant

↓

Hi!

↓

User

↓

Explain RAG

↓

Assistant

↓

...
```

Every message becomes part of the conversation.

---

# Types of Memory

## 1. Short-term Memory

Stores only recent messages.

Example

Last 10 messages.

---

## 2. Long-term Memory

Stores conversations permanently.

Example

Customer history

Past support tickets

Preferences

---

## 3. Semantic Memory

Stores facts.

Example

```
Preferred Language

Java Developer

Location
```

---

# Memory Window

Instead of sending the complete history

```
500 messages
```

Send only

```
Last 10 messages
```

Benefits

- Faster
- Lower cost
- Smaller prompts

---

# Session Management

A session identifies one conversation.

Example

```
Session ID

abc123
```

All messages belong to that session.

---

## Why Session IDs?

Imagine two users.

User A

```
Reset password
```

User B

```
Leave policy
```

Their conversations must remain separate.

Session IDs isolate conversations.

---

# Session Store

Simple Python implementation

```python
sessions = {

    "abc123":[

        {

            "role":"user",

            "content":"Reset password"

        }

    ]

}
```

Production systems use

- Redis
- PostgreSQL
- MongoDB

---

# Conversation Lifecycle

```
Create Session

↓

Receive Question

↓

Retrieve History

↓

Retrieve Documents

↓

Prompt Builder

↓

LLM

↓

Store Response

↓

Return Answer
```

---

# Prompt Templates

Instead of sending

```
Question
```

Send

```
System Prompt

Conversation History

Retrieved Documents

Current Question
```

Example

```
You are an Enterprise IT Assistant.

Conversation

User:
I forgot my password.

Assistant:
Visit password.company.com.

Context

Password Reset Guide

Question

What if I forgot my username?
```

---

# Streaming Responses

Without Streaming

```
Wait

↓

Entire Response
```

---

With Streaming

```
H

He

Hel

Hello...
```

Streaming improves user experience.

---

# Enterprise Chatbot Architecture

```
                User

                  │

                  ▼

             API Gateway

                  │

                  ▼

          Authentication

                  │

                  ▼

             FastAPI

                  │

                  ▼

          Session Manager

                  │

                  ▼

         Conversation Memory

                  │

                  ▼

         Embedding Service

                  │

                  ▼

             ChromaDB

                  │

                  ▼

       Retrieve Top Documents

                  │

                  ▼

         Prompt Builder

                  │

                  ▼

            Ollama Chat

                  │

                  ▼

          Streaming Answer
```

---

# Redis in Enterprise AI

Redis is commonly used because it is

- Fast
- In-memory
- Distributed
- Supports expiration

Example

Conversation expires after

```
30 minutes
```

---

# PostgreSQL

Used when conversations must be stored permanently.

Useful for

- Auditing
- Analytics
- Compliance

---

# Best Practices

✔ Store only recent messages

✔ Use session IDs

✔ Return document sources

✔ Cache embeddings

✔ Stream responses

✔ Use metadata filters

✔ Store prompts separately

✔ Log conversations

---

# Common Mistakes

❌ Sending complete history

❌ No session IDs

❌ No memory limit

❌ No source attribution

❌ Very large prompts

❌ No conversation cleanup

---

# Interview Questions

---

## Q1. What is Conversational AI?

### Answer

Conversational AI is an AI system capable of maintaining context across multiple interactions, allowing users to have natural, multi-turn conversations instead of isolated question-and-answer exchanges.

---

## Q2. What is the difference between Stateless and Stateful AI?

### Answer

A stateless AI application treats every request independently and stores no conversation history.

A stateful AI application stores previous interactions and uses them when generating future responses.

---

## Q3. Why is conversation memory important?

### Answer

Conversation memory enables the AI to understand follow-up questions, maintain context, reduce repeated user input, and provide a more natural conversational experience.

---

## Q4. What is a Session ID?

### Answer

A Session ID uniquely identifies a user's conversation and ensures that conversation history is isolated from other users.

---

## Q5. Why shouldn't we send the complete conversation every time?

### Answer

Sending the complete history increases token usage, latency, and cost. It may also exceed the model's context window. Most systems keep only recent messages or summarise older ones.

---

## Q6. Why is Redis commonly used?

### Answer

Redis provides extremely fast in-memory storage with support for expiration, making it ideal for storing temporary conversation history.

---

## Q7. What is Prompt Engineering in conversational AI?

### Answer

Prompt Engineering is the process of structuring system instructions, conversation history, retrieved documents, and the user's current question into an effective prompt for the LLM.

---

## Q8. What is Streaming?

### Answer

Streaming returns generated tokens incrementally, allowing users to see responses as they are generated rather than waiting for the complete response.

---

## Q9. What is a Memory Window?

### Answer

A memory window limits the amount of conversation history sent to the model, typically keeping only the most recent messages to reduce token usage and improve efficiency.

---

## Q10. What are the advantages of multi-turn conversations?

### Answer

- Better user experience
- Natural conversations
- Less repeated information
- Improved context awareness
- Better enterprise support systems

---

# AI Architect Notes

A production conversational AI system includes:

- API Gateway
- Authentication
- Session Manager
- Redis Cache
- Vector Database
- Prompt Builder
- LLM
- Monitoring
- Logging
- Analytics
- Guardrails
- Rate Limiting
- Role-based Access Control

Enterprise systems also include:

- Prompt versioning
- Conversation summarisation
- Token budgeting
- Response evaluation
- Human feedback collection

---

# Daily Assignment

Build a Session Manager with the following methods:

```python
create_session()

get_history(session_id)

add_message(session_id, role, content)

clear_session(session_id)
```

Enhance the Prompt Builder to include:

- System Prompt
- Conversation History
- Retrieved Documents
- Current User Question

Modify the `/chat` endpoint to:

- Accept a session ID
- Retrieve previous messages
- Store the latest interaction
- Return source documents

---

# Revision Notes

Remember these interview points:

- Conversational AI supports multi-turn conversations.
- Stateless APIs do not remember previous requests.
- Stateful APIs maintain conversation history.
- Session IDs isolate user conversations.
- Memory windows improve efficiency.
- Redis is commonly used for temporary conversation storage.
- Prompt templates combine instructions, history, context, and user input.
- Streaming improves the user experience.

---

# End-of-Day Checklist

- [ ] Explain Conversational AI.
- [ ] Explain Stateless vs Stateful applications.
- [ ] Implement Session Management.
- [ ] Understand Conversation Memory.
- [ ] Explain Memory Windows.
- [ ] Build Prompt Templates.
- [ ] Implement Streaming Responses.
- [ ] Explain Enterprise Chatbot Architecture.
- [ ] Answer all interview questions confidently.
- [ ] Complete the coding assignment.

---

# Key Takeaways

- Memory transforms a simple RAG system into a conversational assistant.
- Session management is essential for supporting multiple users.
- Prompt engineering becomes more important as conversation history grows.
- Enterprise AI systems balance context quality with token limits by using memory windows and summarisation.
- Redis is commonly used for fast, temporary conversation storage, while relational or document databases are used for long-term persistence and auditing.

---

# What's Next?

## Day 10 – Agentic AI Fundamentals

Topics include:

- What is an AI Agent?
- Tool Calling
- Function Calling
- Planning
- ReAct Pattern
- Multi-step Reasoning
- Agent Memory
- Agent Architecture
- Enterprise Agent Design

You will begin transforming your conversational assistant into an **AI Agent** capable of selecting and using tools to complete tasks.