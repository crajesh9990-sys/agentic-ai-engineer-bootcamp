# AI Engineer Interview Preparation – Embeddings & Vector Search

# 1. What are Embeddings?

Embeddings are **numerical vector representations of data** (text, images, audio, etc.) that capture semantic meaning.

Example:

- "I love dogs"
- "Dogs are amazing pets"

These sentences have different words but similar meaning. An embedding model converts both into vectors that are close together in vector space.

Think of embeddings as GPS coordinates for meaning.

## Why are embeddings needed?

LLMs understand text, but computers compare numbers efficiently. Embeddings convert meaning into numbers so we can:

- Semantic search
- RAG
- Recommendation systems
- Duplicate detection
- Clustering
- Classification

---

# 2. Embeddings vs LLMs

| Embeddings | LLM |
|------------|-----|
| Convert text into vectors | Generate text |
| Output numbers | Output language |
| Used for search & retrieval | Used for answering |
| Small & fast | Large & slower |

Typical RAG flow:

User Question -> Embedding Model -> Vector DB search -> Relevant documents -> LLM -> Final answer

Interview answer:
> Embeddings retrieve relevant information; LLMs reason over and generate language from that information.

---

# 3. What are Vectors?

A vector is an ordered list of numbers.

Example:
```
[0.23, -0.71, 0.15, 0.94]
```

Each number represents one learned feature.

## Vector dimensions

Dimension = number of values.

Examples:

- 384 dimensions
- 768 dimensions
- 1024 dimensions
- 1536 dimensions

Higher dimensions can encode richer semantic information but use more storage and computation.

---

# 4. Cosine Similarity (Concept)

Cosine similarity measures the angle between vectors.

Formula:

cos(A,B) = (A·B) / (|A||B|)

You don't need to calculate it manually in interviews.

Interpretation:

- 1.0 = identical direction
- ~0.8 = very similar
- ~0 = unrelated
- -1 = opposite direction

Example:

Query:
"I want to learn AI"

Documents:
- "Artificial Intelligence roadmap" ✅ High similarity
- "Best pizza recipe" ❌ Low similarity

Interview answer:
> Cosine similarity compares vector direction rather than magnitude, making it effective for semantic similarity.

---

# 5. Generate Embeddings using Ollama

Install a model such as:
```
ollama pull nomic-embed-text
```

Python example:

```python
import ollama

response = ollama.embeddings(
    model="nomic-embed-text",
    prompt="What is Artificial Intelligence?"
)

embedding = response["embedding"]
print(len(embedding))
```

Equivalent (newer client API):

```python
from ollama import Client

client = Client()

response = client.embed(
    model="nomic-embed-text",
    input="What is Artificial Intelligence?"
)

print(len(response["embeddings"][0]))
```

---

# 6. Build a Semantic Search Engine

Steps:

1. Collect documents
2. Generate embeddings
3. Store vectors
4. Embed user query
5. Compare using cosine similarity
6. Return nearest documents
7. Send retrieved context to the LLM (optional)

Pipeline:

```
Documents
    ↓
Embedding Model
    ↓
Vector Database
    ↑
User Query
    ↓
Embedding Model
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
LLM
```

Difference from keyword search:

Keyword search:
- Matches exact words

Semantic search:
- Matches meaning

---

# 7. Where Vector Databases Fit

Architecture:

```
User
 ↓
Application
 ↓
Embedding Model
 ↓
Vector Database
 ↓
Relevant Documents
 ↓
LLM
 ↓
Response
```

Vector databases store embeddings and efficiently perform nearest-neighbour search.

Popular databases:

- Chroma
- Pinecone
- Weaviate
- Qdrant
- Milvus
- pgvector (PostgreSQL)

Why not use SQL alone?

Traditional SQL excels at exact matching.

Vector databases are optimised for similarity search over millions of vectors.

---

# Interview Questions

1. What are embeddings?
2. Why do we need embeddings?
3. Difference between embeddings and LLMs?
4. What is a vector?
5. What is vector dimension?
6. Explain cosine similarity.
7. Why cosine similarity instead of Euclidean distance?
8. How does semantic search work?
9. What is a vector database?
10. Explain a RAG architecture.

# Quick Revision

- Embeddings = numerical meaning
- LLM = text generation
- Vectors = list of numbers
- Dimensions = vector length
- Cosine similarity = semantic closeness
- Semantic search = meaning-based retrieval
- Vector DB = stores/searches embeddings
- RAG = Embeddings + Vector DB + LLM
