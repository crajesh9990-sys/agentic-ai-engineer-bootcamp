# Day 08 – Study Material
## Retrieval-Augmented Generation (RAG)
### Agentic AI Engineer Bootcamp (2026)

**Duration:** 2 Hours

**Difficulty:** ⭐⭐⭐⭐☆

**Project:** Enterprise Knowledge Assistant using Ollama + ChromaDB + FastAPI

---

# Learning Objectives

After today's session you will be able to:

- Understand Ollama Chat API
- Understand Ollama Generate API
- Configure model parameters
- Implement streaming responses
- Use ChromaDB Query API
- Understand Collections and Metadata
- Master Context Injection
- Explain RAG architecture in interviews

---

# Study Material 1 – Official Ollama Documentation

## Topic 1 – Chat API

### What is the Chat API?

The Chat API allows an LLM to maintain a conversation by processing multiple messages instead of a single prompt.

Unlike the Generate API, it understands conversation history using different message roles.

The Chat API is used in:

- AI Chatbots
- Enterprise Assistants
- RAG Applications
- Customer Support Bots
- Coding Assistants

---

## Conversation Flow

```
User

↓

Hello

↓

Assistant

↓

Hi! How can I help?

↓

User

↓

Explain RAG
```

Each new message becomes part of the conversation history.

---

## Message Roles

Every message contains a **role**.

### System

Defines the AI's behaviour.

Example

```python
{
    "role":"system",
    "content":"You are an Enterprise IT Assistant."
}
```

---

### User

Represents the user's question.

```python
{
    "role":"user",
    "content":"How do I reset my password?"
}
```

---

### Assistant

Stores previous AI responses.

```python
{
    "role":"assistant",
    "content":"Visit password.company.com."
}
```

---

## Python Example

```python
import ollama

response = ollama.chat(

    model="llama3.2",

    messages=[

        {
            "role":"system",
            "content":"You are an Enterprise IT Assistant."
        },

        {
            "role":"user",
            "content":"Explain RAG."
        }

    ]

)

print(response["message"]["content"])
```

---

## Why Use Chat API?

Because it supports:

- Conversation history
- System prompts
- Context injection
- Multi-turn conversations
- Memory

It is the preferred API for enterprise AI assistants.

---

## Interview Question

### What is the Chat API?

### Answer

The Chat API enables conversational interactions with an LLM by accepting multiple messages with different roles such as system, user, and assistant. It is ideal for chatbots, AI assistants, and Retrieval-Augmented Generation systems because it maintains conversational context.

---

## Follow-up Questions

- What are message roles?
- Why is a system prompt important?
- Can Chat API support memory?
- Why is Chat API preferred over Generate API?

---

# Topic 2 – Generate API

## What is Generate API?

Generate API performs text generation from a single prompt.

It does not maintain conversation history.

---

## Example

```python
import ollama

response = ollama.generate(

    model="llama3.2",

    prompt="Explain Vector Databases."

)

print(response["response"])
```

---

## Use Cases

- Summarisation
- Translation
- Single Question Answering
- Blog Writing
- Code Generation

---

## Generate API vs Chat API

| Generate API | Chat API |
|--------------|----------|
| Single Prompt | Multiple Messages |
| No Memory | Supports Memory |
| Simple | Conversational |
| Good for utilities | Best for assistants |

---

## Interview Question

### When should you use Generate API?

### Answer

Generate API is suitable for single prompt-response tasks such as summarisation, translation, or text generation. For conversational applications and RAG systems, Chat API is usually the better choice.

---

# Topic 3 – Model Parameters

LLMs expose configurable parameters that influence the generated output.

---

## Temperature

Controls creativity.

```
0
```

Very deterministic.

Suitable for:

- Banking
- Healthcare
- HR
- Enterprise Documentation

---

```
1
```

Creative.

Suitable for:

- Story writing
- Marketing
- Brainstorming

---

Example

```python
options={

    "temperature":0

}
```

---

## Top_p

Controls the range of token selection.

Typical value

```
0.9
```

---

## Num Predict

Maximum tokens generated.

Example

```python
options={

    "num_predict":300

}
```

---

## Seed

Produces repeatable results.

```python
options={

    "seed":42

}
```

Useful during testing.

---

## Interview Question

### Which temperature should an enterprise chatbot use?

### Answer

A low temperature (0–0.2) because enterprise assistants should provide consistent, reliable, and factual responses instead of creative variations.

---

# Topic 4 – Streaming Responses

Without Streaming

```
User

↓

Wait...

↓

Entire Answer
```

---

With Streaming

```
User

↓

H

↓

He

↓

Hel

↓

Hello...
```

The user starts seeing the response immediately.

---

## Python Example

```python
stream = ollama.chat(

    model="llama3.2",

    messages=[

        {
            "role":"user",
            "content":"Explain RAG"
        }

    ],

    stream=True

)

for chunk in stream:

    print(

        chunk["message"]["content"],

        end=""

    )
```

---

## Advantages

- Better user experience
- Faster perceived performance
- Ideal for chat interfaces
- Lower perceived latency

---

## Interview Question

### Why do ChatGPT and Claude stream responses?

### Answer

Streaming improves perceived responsiveness. Users can start reading the generated text while the model is still generating the remaining content.

---

# Study Material 2 – ChromaDB Documentation

---

# Topic 5 – Query API

After storing document embeddings, ChromaDB retrieves similar documents.

Example

```python
results = collection.query(

    query_embeddings=[embedding],

    n_results=3

)
```

---

## Internal Workflow

```
Question

↓

Embedding

↓

Vector Search

↓

Top 3 Results
```

---

## Example Response

```python
{

 "documents":[

     [

      "Password Reset",

      "VPN Guide"

     ]

 ],

 "metadatas":[

     [

      {

        "title":"Password Reset"

      },

      {

        "title":"VPN"

      }

     ]

 ]

}
```

---

## Interview Question

### What is Query API?

### Answer

The Query API performs semantic similarity search using vector embeddings and returns the nearest matching documents from a collection.

---

# Topic 6 – Metadata

Metadata is additional information stored alongside documents.

Example

```python
collection.add(

documents=[

"Reset Password"

],

metadatas=[

{

"department":"IT",

"category":"Support",

"author":"Admin"

}

]

)
```

---

## Why Metadata?

Allows filtering such as:

```
Only HR documents
```

```
Only IT documents
```

```
Only Finance documents
```

---

## Enterprise Examples

Metadata fields may include:

- Department
- Author
- Category
- Version
- Security Level
- Language
- Created Date

---

## Interview Question

### Why is metadata important?

### Answer

Metadata enables filtering, organisation, governance, and access control. Enterprise AI applications use metadata to ensure users retrieve only relevant and authorised documents.

---

# Topic 7 – Collections

Collections are logical containers for documents.

Think of them like SQL tables.

SQL

```
Employee
```

```
Orders
```

```
Departments
```

ChromaDB

```
employee_docs
```

```
policies
```

```
contracts
```

---

Each collection stores:

- IDs
- Documents
- Embeddings
- Metadata

---

Example

```python
collection = client.get_or_create_collection(

name="employee_docs"

)
```

---

## Interview Question

### What is a Collection?

### Answer

A Collection is a logical container in ChromaDB that stores documents, embeddings, metadata, and IDs. It is conceptually similar to a table in a relational database.

---

# Study Material 3 – Context Injection (Most Important)

---

# What is Context Injection?

Context Injection is the process of adding retrieved documents into the prompt before sending it to the LLM.

Without Context Injection

```
Question

↓

LLM

↓

Guess
```

---

With Context Injection

```
Question

↓

Retriever

↓

Relevant Documents

↓

Prompt Builder

↓

LLM

↓

Grounded Answer
```

---

# Step-by-Step Example

## User Question

```
How do I reset my password?
```

---

## Retriever Searches

Returns

```
Password Reset Guide

VPN Guide

Email Setup
```

---

## Prompt Builder Creates

```
You are an Enterprise IT Assistant.

Use ONLY the information below.

Context

------------------------------------

Password Reset Guide

Visit

password.company.com

to reset your password.

------------------------------------

Question

How do I reset my password?

Answer:
```

---

## LLM Response

```
Visit password.company.com and follow the password reset instructions.
```

Notice that the LLM answers using the retrieved documentation instead of making assumptions.

---

# Why Context Injection Works

Instead of asking the LLM to remember everything,

we provide the required knowledge.

The LLM focuses on:

- Reading
- Understanding
- Explaining

rather than remembering company policies.

---

# Benefits

- Reduces hallucinations
- More accurate responses
- Uses company documents
- Easy to update
- No model retraining required

---

# Enterprise RAG Architecture

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

            Ollama LLM

                  │

                  ▼

         Grounded AI Response
```

---

# Real Enterprise Example

Company documents:

- Leave Policy
- VPN Guide
- Password Reset
- Travel Policy

Employee asks:

```
How many leave days do I get?
```

Retriever finds:

```
Leave Policy
```

Prompt Builder injects the policy.

LLM responds:

```
Employees receive 20 annual leave days each year according to the company leave policy.
```

---

# Interview Question

### What is Context Injection?

### Answer

Context Injection is the process of inserting externally retrieved information into an LLM prompt before generating a response. In RAG systems, retrieved documents from a vector database are added to the prompt so the model can produce answers grounded in trusted information rather than relying solely on its pre-trained knowledge.

---

## Follow-up Questions

- Why does Context Injection reduce hallucinations?
- What happens if irrelevant documents are injected?
- Should all retrieved documents be included?
- Why is Top-K retrieval used?

---

# Common Mistakes

❌ Sending all documents to the LLM

❌ Ignoring metadata

❌ Using very large document chunks

❌ Not returning document sources

❌ Using high temperature for enterprise assistants

❌ Forgetting to instruct the model to use only the provided context

---

# AI Architect Notes

Enterprise RAG systems include additional capabilities:

- Authentication
- Role-based access control
- Metadata filtering
- Prompt versioning
- Logging
- Monitoring
- Caching
- Guardrails
- Source citations
- Conversation memory
- Evaluation metrics

A production RAG application is much more than an LLM connected to a vector database.

---

# Revision Cheat Sheet

| Topic | Summary |
|---------|----------|
| Chat API | Multi-message conversations |
| Generate API | Single prompt generation |
| Temperature | Controls creativity |
| Streaming | Token-by-token responses |
| Query API | Semantic search |
| Metadata | Document filtering |
| Collections | Containers for embeddings |
| Context Injection | Adds retrieved documents into prompts |
| RAG | Retrieval + Generation |

---

# End-of-Day Checklist

- [ ] Understand Chat API
- [ ] Understand Generate API
- [ ] Configure model parameters
- [ ] Explain streaming responses
- [ ] Use ChromaDB Query API
- [ ] Understand Metadata
- [ ] Understand Collections
- [ ] Explain Context Injection
- [ ] Explain complete RAG architecture
- [ ] Review interview questions and answers

---

# Tomorrow (Day 09)

**Conversational RAG**

Topics include:

- Conversation Memory
- Session Management
- Multi-turn Chat
- Streaming Responses
- React Chat UI
- AI Agent Fundamentals
- Enterprise Chatbot Architecture

By the end of Day 9, you will build a ChatGPT-style enterprise assistant with memory and document retrieval.