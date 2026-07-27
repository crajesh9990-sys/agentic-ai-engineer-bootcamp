# Day 05 – Multi-LLM Architecture using Provider Factory

**Duration:** 2 Hours

**Goal:** Learn how enterprise AI applications support multiple LLM providers (Ollama, OpenAI, Gemini, Claude) using the Factory Design Pattern.

---

# Learning Objectives

By the end of Day 5, you should be able to:

- Understand OpenAI-Compatible APIs
- Understand Provider Pattern
- Implement Factory Design Pattern
- Build a Multi-LLM architecture
- Use Environment Variables
- Implement clean architecture
- Understand Dependency Inversion Principle
- Prepare for AI Architect interviews

---

# Today's Schedule

| Time | Activity |
|-------|----------|
| 30 min | Udemy Course |
| 20 min | Documentation |
| 60 min | Hands-on Coding |
| 10 min | Interview Preparation |

---

# Udemy Course

Continue your selected Agentic AI / LLM course.

Focus on:

- OpenAI API
- API Clients
- REST APIs
- AI Providers
- Environment Variables
- Clean Architecture

---

# Documentation

Read

- OpenAI API Overview
- Ollama REST API
- FastAPI Dependency Injection
- python-dotenv
- Factory Design Pattern
- SOLID Principles

---

# Practical Lab

Project Folder

```
day05_multi_llm_api/
```

---

## Folder Structure

```
day05_multi_llm_api/

app/

    main.py

    routes.py

    models.py

    ai_service.py

    config.py

    provider_factory.py

    providers/

        base.py

        ollama_provider.py

        openai_provider.py

        gemini_provider.py

prompts/

.env

README.md

requirements.txt
```

---

# Lab 1

## Create Config

Create

```
config.py
```

```python
from dotenv import load_dotenv
import os

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
MODEL = os.getenv("MODEL", "llama3.2")
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)
```

---

# Lab 2

## Base Provider

```
providers/base.py
```

```python
from abc import ABC, abstractmethod

class BaseProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str):
        pass
```

---

# Lab 3

## Ollama Provider

Move all Ollama code into

```
providers/ollama_provider.py
```

The provider should expose

```python
generate(prompt)
```

---

# Lab 4

## Create OpenAI Provider

```
providers/openai_provider.py
```

```python
class OpenAIProvider:

    def generate(self, prompt):

        raise NotImplementedError
```

---

# Lab 5

## Create Gemini Provider

```
providers/gemini_provider.py
```

```python
class GeminiProvider:

    def generate(self, prompt):

        raise NotImplementedError
```

---

# Lab 6

## Provider Factory

Create

```
provider_factory.py
```

Example

```python
from app.providers.ollama_provider import OllamaProvider
from app.providers.openai_provider import OpenAIProvider
from app.providers.gemini_provider import GeminiProvider

from app.config import LLM_PROVIDER

_PROVIDER_REGISTRY = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
    "gemini": GeminiProvider,
}


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider_cls = _PROVIDER_REGISTRY.get(
            LLM_PROVIDER.lower()
        )

        if provider_cls is None:
            raise ValueError("Unsupported Provider")

        return provider_cls()
```

---

# Lab 7

## Update AI Service

Replace

```python
provider = OllamaProvider()
```

with

```python
provider = ProviderFactory.get_provider()
```

---

# Lab 8

## Add Environment Variables

Create

```
.env
```

```
LLM_PROVIDER=ollama

MODEL=llama3.2

OLLAMA_URL=http://localhost:11434/api/generate
```

---

# Lab 9

## Add Provider Endpoint

```
GET /provider
```

Expected Output

```json
{
    "provider":"ollama",
    "model":"llama3.2"
}
```

---

# Lab 10

## Logging

Install

```
pip install loguru
```

Use

```python
logger.info("Calling AI Provider")
```

inside

```
ai_service.py
```

---

# Mini Project

Convert yesterday's Prompt Engineering API into a Multi-Provider AI API.

The application should support

- Ollama
- OpenAI (placeholder)
- Gemini (placeholder)

without changing any route code.

---

# Git Tasks

```
git add .

git commit -m "Day 05 - Multi Provider Architecture"

git push
```

---

# Interview Preparation

---

# Question 1

## What is an OpenAI-Compatible API?

### Answer

An OpenAI-Compatible API is an API that follows the same request and response format as the OpenAI API. This allows developers to switch between different LLM providers with minimal or no code changes.

For example, Ollama exposes endpoints that mimic the OpenAI API, allowing existing OpenAI SDKs to work with local models.

Examples of OpenAI-compatible providers:

- Ollama
- Groq
- LM Studio
- vLLM
- Together AI
- OpenRouter

### Why is it useful?

- Vendor independence
- Easy migration between providers
- Reuse existing SDKs
- Reduced development effort
- Lower maintenance cost

### Follow-up Questions

- Why is OpenAI compatibility important?
- Which providers support it?
- Can Ollama work with the OpenAI SDK?

### AI Architect Note

Enterprise applications should avoid vendor lock-in. Designing around OpenAI-compatible interfaces makes future migrations significantly easier.

---

# Question 2

## Explain the Provider Pattern.

### Answer

The Provider Pattern separates business logic from external service implementations.

Instead of calling a specific provider directly, the application communicates through a common interface.

```
Application

↓

AI Service

↓

Provider Interface

↓

Ollama
OpenAI
Gemini
Claude
```

### Advantages

- Easy to extend
- Easy to test
- Supports multiple providers
- Clean architecture

### Follow-up Questions

- How does this differ from Strategy Pattern?
- Why not call Ollama directly?

### AI Architect Note

Every external dependency (AI model, database, payment gateway, email service) should be abstracted behind an interface.

---

# Question 3

## Why use the Factory Design Pattern?

### Answer

The Factory Pattern centralizes object creation.

Instead of creating objects throughout the application, one factory decides which implementation to instantiate.

Without Factory:

```python
provider = OllamaProvider()
```

With Factory:

```python
provider = ProviderFactory.get_provider()
```

### Benefits

- Loose coupling
- Easier maintenance
- Supports runtime configuration
- Simplifies testing

### Follow-up Questions

- Difference between Factory and Singleton?
- Where is Factory used in Spring Boot?

### AI Architect Note

Factories reduce coupling and make applications easier to evolve as new providers are introduced.

---

# Question 4

## Explain the Dependency Inversion Principle (DIP).

### Answer

The Dependency Inversion Principle states:

> High-level modules should not depend on low-level modules. Both should depend on abstractions.

Instead of:

```
AIService

↓

OllamaProvider
```

Use:

```
AIService

↓

BaseProvider

↓

Ollama
OpenAI
Gemini
```

### Benefits

- Better testing
- Loose coupling
- Easier extension

### Follow-up Questions

- How does Spring implement DIP?
- How does dependency injection help?

### AI Architect Note

Most enterprise frameworks (Spring, ASP.NET Core) rely heavily on DIP to keep systems modular and testable.

---

# Question 5

## Why shouldn't AIService depend directly on Ollama?

### Answer

If AIService directly depends on Ollama:

- Replacing Ollama requires code changes.
- Unit testing becomes difficult.
- The application becomes tightly coupled.

Using an abstraction allows switching providers through configuration without modifying business logic.

### Follow-up Questions

- What happens if Ollama is unavailable?
- How would you add Claude?

### AI Architect Note

Business logic should never be tied to a specific vendor implementation.

---

# Question 6

## Difference between Factory Pattern and Strategy Pattern.

### Factory Pattern

Responsible for creating objects.

Example:

```
ProviderFactory.get_provider()
```

### Strategy Pattern

Responsible for selecting behavior at runtime.

Example:

```
provider.generate(prompt)
```

### Simple Comparison

| Factory | Strategy |
|----------|----------|
| Creates objects | Chooses algorithms |
| Used during initialization | Used during execution |
| Focuses on instantiation | Focuses on behavior |

### Follow-up Questions

- Can both patterns be used together?

### AI Architect Note

Many enterprise applications combine Factory and Strategy to achieve flexibility and maintainability.

---

# Question 7

## What are Environment Variables?

### Answer

Environment variables store configuration outside the source code.

Examples:

```
LLM_PROVIDER=ollama
MODEL=llama3.2
API_KEY=xxxxxxxx
```

### Benefits

- Keeps secrets out of code
- Supports multiple environments
- Simplifies deployment
- Improves security

### Follow-up Questions

- Why not hardcode API keys?
- What is `.env`?

### AI Architect Note

Never commit secrets such as API keys or passwords to version control. Use secret management solutions in production environments.

---

# Question 8

## How would you support OpenAI, Claude, Gemini, and Ollama without changing application code?

### Answer

1. Define a common interface (`BaseProvider`).
2. Create one provider implementation per LLM.
3. Register providers in `ProviderFactory`.
4. Read the provider name from configuration.
5. Instantiate the provider through the factory.
6. Keep business logic independent of provider-specific APIs.

Architecture:

```
FastAPI

↓

AIService

↓

ProviderFactory

↓

BaseProvider

↓

Ollama
OpenAI
Gemini
Claude
```

Changing the provider only requires updating:

```
LLM_PROVIDER=openai
```

No code changes are required.

### Follow-up Questions

- How would you add a new provider?
- How would you unit test the service?

### AI Architect Note

This design demonstrates the Open/Closed Principle: the system is open for extension but closed for modification.

---

# Senior AI Architect Interview Question

## Design an enterprise AI platform supporting multiple LLM providers.

### Sample Answer

I would design the platform with:

- API Layer (FastAPI)
- Business Layer
- AI Service Layer
- Provider Factory
- Provider Interface
- Individual Provider Implementations
- Prompt Management
- Logging & Monitoring
- Configuration Management
- Caching
- Rate Limiting
- Retry Mechanisms
- Observability

This architecture allows new providers to be added without affecting business logic, improves maintainability, and supports enterprise scalability.

```
Client

↓

FastAPI

↓

Business Service

↓

AI Service

↓

Provider Factory

↓

BaseProvider

↓

OpenAI
Gemini
Claude
Ollama
```

---

# AI Architect Notes

Enterprise AI applications never directly call

```
requests.post(...)
```

inside business logic.

Instead they use

```
Business Layer

↓

AI Service

↓

Provider Factory

↓

Provider

↓

LLM
```

This makes the application

- Maintainable
- Testable
- Extensible
- Vendor Independent

---

# Deliverables

By the end of today you should have

- Multi Provider Architecture
- Provider Factory
- Base Provider
- Ollama Provider
- OpenAI Placeholder
- Gemini Placeholder
- Environment Variables
- Logging
- Provider Endpoint
- GitHub Commit

---

# End of Day Checklist

- [ ] Completed Udemy lesson
- [ ] Read documentation
- [ ] Created BaseProvider
- [ ] Implemented OllamaProvider
- [ ] Created OpenAIProvider
- [ ] Created GeminiProvider
- [ ] Implemented ProviderFactory
- [ ] Updated AI Service
- [ ] Added .env
- [ ] Added logging
- [ ] Tested all APIs
- [ ] Verified `/provider` endpoint
- [ ] Git commit completed
- [ ] GitHub push completed
- [ ] Reviewed interview questions

---

# Tomorrow (Day 06)

Topic:

**Embeddings & Semantic Search**

You will learn:

- What are Embeddings?
- Vector Similarity
- Cosine Similarity
- Sentence Transformers
- Building your first Embedding Search Engine
- Introduction to Vector Databases