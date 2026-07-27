# Day 06 – Embeddings & Semantic Search

**Duration:** 2 Hours

**Difficulty:** ⭐⭐⭐☆☆

**Project:** Employee Knowledge Search API

---

# Goal

Today's goal is to understand how AI understands the **meaning** of text rather than simply matching keywords.

By the end of today, you will build your first **Semantic Search API**, which is the foundation of modern Retrieval-Augmented Generation (RAG) systems.

---

# Learning Objectives

After completing Day 6, you should be able to:

- Explain what embeddings are
- Differentiate embeddings from LLMs
- Understand vectors and vector dimensions
- Explain cosine similarity
- Generate embeddings using Ollama
- Build a semantic search engine
- Cache document embeddings in memory
- Design a basic enterprise document search architecture

---

# Study Plan (2 Hours)

| Time | Activity |
|-------|----------|
| 20 min | Learn Embeddings Concepts |
| 15 min | Read Ollama Embeddings Documentation |
| 70 min | Hands-on Labs |
| 15 min | Interview Preparation |

---

# Study Material

## Mandatory Reading

### 1. Ollama Embeddings Documentation

Learn:

- Embeddings API
- Pull embedding models
- Generate embeddings
- Embedding response

---

### 2. ChromaDB Documentation (Overview Only)

Read:

- What is ChromaDB?
- What is a Collection?
- What is a Vector Database?

(No installation today.)

---

### 3. NumPy Basics

Understand:

- Arrays
- Dot Product
- Norm
- Vector Operations

---

# Theory

---

## What is an Embedding?

An embedding is a numerical representation of text that captures its semantic meaning.

Example

```
Reset my password

↓

[0.31, -0.18, 0.62, ...]
```

Computers compare vectors instead of comparing words.

---

## LLM vs Embeddings

| LLM | Embedding Model |
|------|-----------------|
| Generates text | Generates vectors |
| Chatbot | Search |
| Answers questions | Finds similar information |
| Produces natural language | Produces numbers |

---

## What is a Vector?

A vector is simply a list of numbers.

Example

```python
[
 0.42,
-0.91,
 0.17,
...
]
```

Most embedding models generate vectors with hundreds of dimensions.

---

## Cosine Similarity

Cosine similarity measures how similar two vectors are.

```
1.0

↓

Exactly Same Meaning

0.8

↓

Very Similar

0.5

↓

Somewhat Similar

0

↓

Completely Different
```

---

# Practical Labs

---

# Lab 1 – Generate Embeddings

## Install Packages

```bash
pip install ollama numpy
```

---

## Pull Model

```bash
ollama pull nomic-embed-text
```

---

## Verify

```bash
ollama list
```

Expected

```
llama3.2

nomic-embed-text
```

---

## Create

```
compare_embeddings.py
```

Generate embeddings for

- Reset my password
- I forgot my password
- What's the weather today?

Print

- Vector Length
- First 10 values

---

# Lab 2 – Compare Similarity

Implement

```python
cosine_similarity()
```

Compare

```
Reset my password

↓

Forgot my password

↓

Weather today
```

Observe that the first two sentences have the highest similarity.

---

# Lab 3 – Build Document Store

Create

```
document.py
```

```python
from dataclasses import dataclass

@dataclass
class Document:

    title: str
    content: str
    embedding: list[float]
```

---

Create

```
document_store.py
```

Implement

- load_documents()
- get_documents()
- reload()
- size()
- is_empty()

Generate document embeddings **once** during application startup.

---

# Lab 4 – Build Semantic Search API

Create

```
documents.json
```

Example

```json
[
  {
    "title":"Password Reset",
    "content":"Reset your password..."
  },
  {
    "title":"VPN Access",
    "content":"Connect using VPN..."
  },
  {
    "title":"Leave Policy",
    "content":"Annual leave..."
  }
]
```

---

Implement

```
POST /search
```

Input

```json
{
    "query":"Forgot password"
}
```

Output

```json
{
    "query":"Forgot password",
    "best_match":"Password Reset",
    "score":0.91
}
```

---

# Lab 5 – Cache Embeddings

Instead of generating embeddings every request

```
Request

↓

Generate Document Embeddings

↓

Search
```

Cache them

```
Application Starts

↓

Generate Embeddings

↓

Store in Memory

↓

Ready
```

Each request only generates

```
Query Embedding
```

making the application significantly faster.

---

# Mini Project

## Employee Knowledge Search

Build a semantic search application that searches company documents.

Suggested Documents

- Password Reset
- VPN Access
- Leave Policy
- Expense Claims
- Laptop Request
- Email Setup
- HR Policies
- Travel Policy

The API should return the most relevant document based on meaning, not keywords.

---

# Project Structure

```
day06_embeddings/

app/

    main.py

    routes.py

    models.py

    embedding_service.py

    similarity.py

    document.py

    document_store.py

data/

    documents.json

README.md

requirements.txt
```

---

# Git Tasks

```bash
git checkout -b day06-embeddings

git add .

git commit -m "Day06 - Semantic Search"

git push
```

---

# Interview Preparation

---

## Question 1

### What is an embedding?

**Answer**

An embedding is a dense numerical vector representing the semantic meaning of text.

---

## Question 2

### Difference between embeddings and LLMs?

**Answer**

LLMs generate text.

Embedding models generate vectors.

Embeddings are used for search and retrieval.

LLMs are used for reasoning and response generation.

---

## Question 3

### What is semantic search?

**Answer**

Semantic search retrieves information based on meaning rather than exact keyword matches.

---

## Question 4

### What is cosine similarity?

**Answer**

Cosine similarity measures the angle between two vectors to determine semantic similarity.

---

## Question 5

### Why are embeddings required for RAG?

**Answer**

Embeddings allow documents to be searched based on meaning.

The retrieved documents become context for the LLM.

Without embeddings, retrieval quality would be much lower.

---

## Question 6

### Why cache embeddings?

**Answer**

Document embeddings rarely change.

Generating them for every request wastes time and compute.

Caching improves application performance and reduces latency.

---

## Question 7

### Can embeddings replace an LLM?

**Answer**

No.

Embeddings help retrieve relevant information.

LLMs interpret that information and generate human-readable responses.

---

## Question 8

### How would you design an enterprise document search system?

**Answer**

Architecture

```
Documents

↓

Embedding Model

↓

Vector Database

↓

Retriever

↓

LLM

↓

User
```

The retriever finds the most relevant documents, and the LLM uses those documents to answer the user's question.

---

# AI Architect Notes

Enterprise systems never regenerate document embeddings on every request.

Instead

```
Startup

↓

Load Documents

↓

Generate Embeddings

↓

Store in ChromaDB

↓

Search

↓

LLM
```

Tomorrow you will replace the in-memory cache with **ChromaDB**, which supports efficient vector storage and similarity search.

---

# Deliverables

By the end of Day 6, you should have:

- [ ] Generated embeddings using Ollama
- [ ] Compared sentence similarity
- [ ] Built cosine similarity function
- [ ] Created Document model
- [ ] Implemented DocumentStore
- [ ] Cached document embeddings
- [ ] Built `/search` endpoint
- [ ] Tested using Swagger
- [ ] Updated README
- [ ] Committed code to GitHub

---

# Bonus Challenge

Return the **Top 3** matching documents instead of only the best match.

Example

```json
{
  "results": [
    {
      "title":"Password Reset",
      "score":0.94
    },
    {
      "title":"VPN Access",
      "score":0.63
    },
    {
      "title":"Email Setup",
      "score":0.51
    }
  ]
}
```

---

# Tomorrow (Day 07)

## Vector Databases with ChromaDB

You will learn:

- Why Vector Databases exist
- ChromaDB
- Collections
- Indexing
- Top-K Search
- Building your first RAG pipeline
- Replacing in-memory search with ChromaDB
- Enterprise RAG architecture