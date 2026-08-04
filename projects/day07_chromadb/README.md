# Day 7 – Embeddings, ChromaDB & Semantic Search

> **Agentic AI Engineer Bootcamp**  
> **Module:** Embeddings, Vector Databases & Semantic Search  
> **Duration:** ~2 Hours  
> **Status:** ⬜ Not Started

---

# 📚 Day 7 Learning Objectives

By the end of Day 7, you will be able to:

- Understand what embeddings are.
- Explain the difference between LLMs and embeddings.
- Understand vectors and vector dimensions.
- Calculate cosine similarity conceptually.
- Generate embeddings using Ollama.
- Understand how vector databases work.
- Use ChromaDB to store and retrieve embeddings.
- Build a simple semantic search engine.
- Understand where vector databases fit in a RAG architecture.

---

# 🛠 Prerequisites

Make sure you have:

- Python 3.11+
- VS Code
- Git
- Ollama installed
- `nomic-embed-text` model downloaded
- ChromaDB installed

Install dependencies:

```bash
pip install chromadb ollama
```

Download the embedding model:

```bash
ollama pull nomic-embed-text
```

Verify the installation:

```bash
ollama list
```

Expected output:

```
nomic-embed-text
llama3
```

---

# 📖 Topics Covered

## Part 1 – Embeddings

- What are embeddings?
- Embeddings vs LLMs
- Vector representation
- Vector dimensions
- Cosine similarity
- Real-world examples

---

## Part 2 – Generate Embeddings

Generate embeddings using:

- Ollama
- Python

Concepts:

- Embedding API
- Float vectors
- Similarity search

---

## Part 3 – ChromaDB

Study:

- Introduction
- Collections
- Adding Documents
- Querying Documents
- Metadata
- Persistence

Learn:

- Create collections
- Store vectors
- Query vectors
- Filter using metadata
- Persistent storage

---

## Part 4 – Semantic Search

Build a mini search engine that:

- Accepts a question
- Converts it into an embedding
- Searches ChromaDB
- Returns the most relevant document

---

## Part 5 – Vector Search Concepts

Study:

- Vector Search
- AI Search
- Retrieval
- Top-K Retrieval
- Hybrid Search
- Semantic Ranking

---

# 💻 Hands-on Labs

## Lab 1

Generate embeddings using Ollama.

---

## Lab 2

Create a ChromaDB collection.

---

## Lab 3

Insert multiple documents.

---

## Lab 4

Query documents using semantic search.

---

## Lab 5

Use metadata filtering.

---

## Lab 6

Enable persistent storage.

---

## Lab 7 (Mini Project)

Build a Semantic Search Engine.

Features:

- Store documents
- Generate embeddings
- Search by meaning
- Display Top-K results

---

# 📂 Suggested Project Structure

```
day07/

│── data/
│   └── documents.txt
│
│── db/
│
│── embeddings.py
│── store.py
│── search.py
│── app.py
│── requirements.txt
│── README.md
```

---

# 📦 Required Packages

```text
chromadb
ollama
```

Install:

```bash
pip install chromadb ollama
```

---

# 🎯 Mini Project

## Semantic Search Engine

Workflow:

```
Documents

↓

Embeddings

↓

ChromaDB

↓

User Question

↓

Embedding

↓

Similarity Search

↓

Top-K Documents
```

---

# 🧠 Interview Preparation

Prepare answers for:

1. What is an embedding?
2. Difference between embeddings and LLMs.
3. What is a vector database?
4. Why not use MySQL for semantic search?
5. What is ChromaDB?
6. What is a collection?
7. What is metadata?
8. What is Top-K retrieval?
9. Why is Top-K important?
10. Where does ChromaDB fit in a RAG pipeline?

---

# 📝 Deliverables

By the end of Day 7, you should have:

- ✅ Generated embeddings using Ollama
- ✅ Understood vectors and cosine similarity
- ✅ Created a ChromaDB collection
- ✅ Stored documents and metadata
- ✅ Queried documents using semantic search
- ✅ Enabled persistence
- ✅ Built a simple semantic search application
- ✅ Completed interview preparation

---

# 🚀 What's Next? (Day 8)

On Day 8, you'll learn:

- Retrieval-Augmented Generation (RAG)
- Document loading
- Text chunking
- Prompt augmentation
- Building a complete RAG pipeline
- Integrating ChromaDB with an LLM
- End-to-end Question Answering system

---

# 📌 Resources

### Mandatory

- ChromaDB Documentation
- ChromaDB GitHub Repository

### Optional

- Microsoft Learn – Vector Search
- Microsoft Learn – AI Search Concepts
- Microsoft Learn – Retrieval Concepts

---

# ✅ Day 7 Checklist

- [ ] Read ChromaDB documentation
- [ ] Read ChromaDB GitHub Quick Start
- [ ] Study Microsoft Vector Search concepts
- [ ] Generate embeddings with Ollama
- [ ] Create a ChromaDB collection
- [ ] Add documents to the collection
- [ ] Perform semantic search queries
- [ ] Practice metadata filtering
- [ ] Enable persistence
- [ ] Build the semantic search mini project
- [ ] Review interview questions

---

**Congratulations! 🎉**

You have completed **Day 7** of your **Agentic AI Engineer Bootcamp**. You now understand how embeddings are stored, searched, and retrieved using a vector database—the foundation of modern RAG applications.