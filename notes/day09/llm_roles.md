# Understanding Roles in LLM Chat APIs
## System • User • Assistant

**Module:** Day 09 – Conversational AI

---

# Introduction

One of the most important concepts in modern AI applications is understanding **Roles**.

Every enterprise chatbot—whether it is ChatGPT, Claude, Gemini, Microsoft Copilot, or an internal company chatbot—uses the concept of **roles** to maintain structured conversations.

Understanding roles is essential because **they determine how the LLM interprets a conversation**.

---

# What is a Role?

A role defines **who is speaking** in a conversation.

Instead of sending plain text to the LLM, we send a list of messages.

Example:

```python
messages = [

    {
        "role": "system",
        "content": "You are an Enterprise IT Assistant."
    },

    {
        "role": "user",
        "content": "How do I reset my password?"
    }

]
```

Notice that every message has two fields:

- role
- content

The LLM reads **all the messages together** before generating a response.

---

# Types of Roles

There are three primary roles.

```
                LLM

        ▲      ▲      ▲

    System   User   Assistant
```

Each role has a different responsibility.

---

# 1. System Role

The **System** role defines **how the AI should behave**.

Think of it as giving instructions before the conversation starts.

Example:

```python
{
    "role": "system",
    "content": "You are an Enterprise IT Support Assistant."
}
```

The user never sees this message.

It is only used by the model.

---

## What can the System Role define?

Examples:

```
You are a Java Expert.
```

```
You are an HR Assistant.
```

```
You are an AI Architect.
```

```
Always answer in Markdown.
```

```
Keep answers short.
```

```
Never answer outside company policies.
```

```
Always ask clarifying questions if information is missing.
```

---

## Why is it Useful?

Instead of changing application code,

you simply change the system prompt.

Example:

Today's chatbot

```
You are an IT Support Assistant.
```

Tomorrow

```
You are a Banking Assistant.
```

No code changes are required.

Only the System Prompt changes.

---

# Java Analogy

Think of the System Prompt as configuring an implementation.

```java
interface Assistant {

    void answer();

}
```

Implementation today

```java
Assistant assistant =
        new ITSupportAssistant();
```

Tomorrow

```java
Assistant assistant =
        new BankingAssistant();
```

Same application.

Different behaviour.

---

# Enterprise Example

Suppose you build an HR chatbot.

System Prompt

```
You are the HR assistant of ABC Company.

Only answer using HR policies.

If the answer is unavailable,

say

"I don't know."
```

Now every answer follows HR policies.

---

# 2. User Role

The **User** role contains the user's question.

Example

```python
{
    "role":"user",
    "content":"How do I reset my password?"
}
```

Every message from the user is stored using this role.

---

# Examples

```
Explain RAG
```

```
What is ChromaDB?
```

```
Reset my password
```

```
Write Python code
```

These are all User messages.

---

# 3. Assistant Role

The Assistant role stores previous AI responses.

Example

```python
{
    "role":"assistant",
    "content":"Visit password.company.com."
}
```

Many beginners ask

> Why send the AI's own response back to the AI?

The answer is:

Because LLM APIs are **stateless**.

---

# Stateless APIs

Every API request is independent.

Imagine the following:

Request 1

```
User

↓

Reset Password
```

Response

```
Visit password.company.com
```

Now another request arrives.

```
How long does it take?
```

The model has forgotten the previous request.

Why?

Because the previous conversation was never sent.

---

# Without Assistant Messages

```python
messages = [

    {

        "role":"user",

        "content":"How long does it take?"

    }

]
```

The model doesn't know what "it" refers to.

---

# With Assistant Messages

```python
messages = [

    {

        "role":"system",

        "content":"You are an IT Assistant."

    },

    {

        "role":"user",

        "content":"How do I reset my password?"

    },

    {

        "role":"assistant",

        "content":"Visit password.company.com."

    },

    {

        "role":"user",

        "content":"How long does it take?"

    }

]
```

Now the model understands:

"It"

means

```
Password Reset
```

---

# Conversation Timeline

```
System

↓

You are IT Assistant

↓

User

↓

How do I reset my password?

↓

Assistant

↓

Visit password.company.com

↓

User

↓

How long does it take?

↓

LLM

↓

Password reset usually takes a few minutes.
```

The assistant message provides conversation context.

---

# Why Doesn't the LLM Remember Automatically?

This is a very common interview question.

LLMs are stateless.

Each request contains:

```
Messages

↓

LLM

↓

Answer
```

Once the response is generated,

the LLM forgets everything.

Your application is responsible for maintaining history.

---

# Example

Python

```python
history = []

history.append(

    {

        "role":"user",

        "content":"Hello"

    }

)

history.append(

    {

        "role":"assistant",

        "content":"Hi!"

    }

)
```

Later

```python
ollama.chat(

    model="llama3.2",

    messages=history

)
```

The complete conversation is sent every time.

---

# Real Enterprise Flow

```
Browser

↓

React

↓

FastAPI

↓

Redis

↓

Conversation History

↓

Ollama Chat API

↓

LLM

↓

Answer

↓

Save Assistant Reply
```

The LLM itself never remembers.

Redis (or another store) remembers.

---

# Why All Three Roles Are Required

Imagine a movie.

The **Director**

tells actors how to behave.

↓

System

---

The **Audience**

asks questions.

↓

User

---

The **Actor**

responds.

↓

Assistant

Without the Director,

the actor has no guidance.

Without the Audience,

there is nothing to answer.

Without previous dialogue,

the story is lost.

---

# Enterprise HR Example

Request

```python
messages = [

{

"role":"system",

"content":"You are an HR Assistant."

},

{

"role":"user",

"content":"How many leave days do employees receive?"

}

]
```

Assistant

```
Employees receive 20 annual leave days.
```

Next request

```
Can I carry them forward?
```

Now the messages become

```python
messages = [

system,

user,

assistant,

user

]
```

The AI understands that

"them"

means

```
Annual Leave Days
```

---

# Why System Prompt is So Powerful

Suppose you have one application.

Changing only the System Prompt creates completely different assistants.

```
You are a Java Instructor.
```

↓

Programming Assistant

---

```
You are a Doctor.
```

↓

Medical Assistant

---

```
You are an HR Manager.
```

↓

HR Assistant

---

```
You are an AI Architect.
```

↓

Architecture Assistant

No code changes.

Only the prompt changes.

---

# Best Practices

✅ Always include a System Prompt.

✅ Keep System Prompts clear.

✅ Store conversation history.

✅ Use Assistant messages.

✅ Trim long conversations.

✅ Keep User messages concise.

---

# Common Mistakes

❌ Forgetting the System Prompt.

❌ Using Generate API for conversations.

❌ Not storing Assistant responses.

❌ Mixing conversations between users.

❌ Sending unlimited history.

---

# Interview Questions

## Q1. What is the purpose of the System role?

### Answer

The System role defines the behaviour, personality, constraints, and responsibilities of the AI. It provides instructions that influence how the model responds throughout the conversation.

---

## Q2. What does the User role represent?

### Answer

The User role contains the input or question provided by the human user. Every new question is added as a User message.

---

## Q3. Why do we store Assistant messages?

### Answer

Assistant messages preserve previous AI responses. Since LLM APIs are stateless, including previous assistant messages allows the model to understand follow-up questions and maintain conversation context.

---

## Q4. Why doesn't the LLM remember previous requests?

### Answer

LLM APIs are stateless. Every request is processed independently. The application is responsible for storing conversation history and sending it back with each request.

---

## Q5. Can we build different AI assistants using the same model?

### Answer

Yes.

By changing the System Prompt, the same LLM can behave as an IT Assistant, HR Assistant, Banking Assistant, Coding Assistant, or AI Architect without changing the application code.

---

# AI Architect Discussion

A production conversational AI system stores messages outside the model.

Typical architecture

```
User

↓

React UI

↓

FastAPI

↓

Session Manager

↓

Redis

↓

Conversation History

↓

Prompt Builder

↓

Ollama Chat API

↓

LLM

↓

Assistant Response

↓

Redis
```

This design enables:

- Multi-user support
- Session isolation
- Scalability
- Fault tolerance
- Conversation persistence
- Prompt versioning

---

# Revision Cheat Sheet

| Role | Purpose | Example |
|------|----------|----------|
| System | Defines AI behaviour | "You are an IT Assistant." |
| User | Contains the user's question | "How do I reset my password?" |
| Assistant | Stores previous AI responses | "Visit password.company.com." |

---

# Key Takeaways

- **System Role** defines the AI's behaviour, constraints, and personality.
- **User Role** represents the current human input.
- **Assistant Role** stores previous AI responses to maintain context.
- The LLM processes all messages together on every request.
- Conversation memory is managed by your application, not by the LLM itself.
- Enterprise AI systems use roles to build reliable, scalable, multi-turn conversational experiences.

---

# Summary

Understanding roles is the foundation of building conversational AI.

Every modern chatbot—including ChatGPT, Claude, Gemini, and enterprise assistants—uses the same three-role conversation structure.

Once you understand these roles, you can build:

- AI Chatbots
- RAG Applications
- AI Agents
- Customer Support Bots
- Enterprise Knowledge Assistants
- Multi-Agent Systems
- AI Copilots

Mastering roles is one of the first major steps toward becoming a professional AI Engineer.