# Day 10 – Module 1
# Introduction to AI Agents

**Agentic AI Engineer Bootcamp**

---

# Learning Objectives

After completing this module, you will be able to:

- Define an AI Agent
- Understand the components of an AI Agent
- Explain the Observation → Reasoning → Action cycle
- Describe the lifecycle of an AI Agent
- Compare AI Agents with Chatbots and RAG systems
- Discuss real-world AI Agent use cases
- Answer common AI Agent interview questions

---

# Introduction

Large Language Models (LLMs) such as Llama, GPT, Claude, and Gemini are excellent at understanding and generating text.

However, on their own they have important limitations.

They cannot:

- Access real-time information
- Execute external actions
- Use business applications
- Interact with databases
- Send emails
- Book meetings
- Make decisions based on changing environments

To overcome these limitations, we build **AI Agents**.

An AI Agent combines an LLM with memory, reasoning, planning, and external tools to perform tasks autonomously.

---

# What is an AI Agent?

## Definition

An **AI Agent** is an intelligent software system that can:

- Observe its environment
- Understand a goal
- Reason about the best approach
- Select and use tools
- Execute actions
- Evaluate results
- Continue until the goal is achieved

Unlike a traditional chatbot, an AI Agent does more than answer questions—it can **perform work**.

---

# Simple Analogy

Imagine you ask three different systems the same question.

### Chatbot

```
User:
What's the weather today?

↓

Bot:

"I don't know."
```

The chatbot has no access to live information.

---

### RAG Application

```
User

↓

Vector Database

↓

Documents

↓

Answer
```

The RAG system can answer questions only if the required information exists in its knowledge base.

---

### AI Agent

```
User

↓

Agent

↓

Weather API

↓

Current Temperature

↓

Answer
```

The AI Agent retrieves live information before responding.

---

# AI Agent Architecture

```
                  User

                    │

                    ▼

                 AI Agent

        ┌───────────┼───────────┐

        ▼           ▼           ▼

     Memory      Reasoning     Tools

        │           │           │

        └───────────┼───────────┘

                    ▼

             Final Response
```

An AI Agent is composed of multiple cooperating components.

---

# Components of an AI Agent

## 1. Large Language Model (Brain)

The LLM provides:

- Natural language understanding
- Reasoning
- Planning
- Response generation

Examples:

- GPT
- Claude
- Gemini
- Llama
- Mistral

Without an LLM, the agent cannot understand user requests.

---

## 2. Memory

Memory allows the agent to remember previous interactions.

Example

```
User

↓

I work in Chennai.

↓

Later...

↓

What's the weather today?

↓

Agent

↓

Weather in Chennai
```

Without memory, the user would need to repeat the location.

---

## 3. Tools

Tools extend the capabilities of the LLM.

Examples:

- Calculator
- Weather API
- Database Search
- Email Sender
- Calendar
- File System
- SQL Database
- Web Search

The LLM decides when a tool should be used.

---

## 4. Planner

The planner breaks complex problems into smaller tasks.

Example

```
Book my vacation.

↓

Find dates

↓

Check calendar

↓

Search flights

↓

Compare prices

↓

Book hotel

↓

Create itinerary
```

Planning enables multi-step task execution.

---

## 5. Executor

The executor runs the selected tools.

Example

```
Weather Tool

↓

Temperature

↓

Return Result
```

---

## 6. Knowledge Source

The agent may retrieve information from:

- ChromaDB
- Pinecone
- PostgreSQL
- SharePoint
- Confluence
- PDF files
- Company documentation

This enables Retrieval-Augmented Generation (RAG).

---

# Observation → Reasoning → Action

This is the core operating cycle of an AI Agent.

```
Observe

↓

Reason

↓

Act

↓

Observe Again

↓

Reason

↓

Act
```

Let's examine each stage.

---

# Step 1 – Observation

The agent gathers information.

Examples:

- User request
- Conversation history
- Retrieved documents
- API responses
- Tool outputs

Example

```
User

↓

What's the weather in Chennai?
```

Observation:

- User wants weather information.
- The current temperature is unknown.

---

# Step 2 – Reasoning

The agent decides what to do.

Reasoning:

```
Weather requires live information.

↓

Use Weather Tool.
```

The agent determines the next action before acting.

---

# Step 3 – Action

The selected tool is executed.

```
Weather Tool

↓

31°C

↓

Sunny
```

The result is returned to the agent.

---

# Final Response

```
The current weather in Chennai is 31°C and sunny.
```

---

# Agent Lifecycle

A complete AI Agent follows this lifecycle.

```
Receive Request

↓

Understand Goal

↓

Retrieve Memory

↓

Retrieve Knowledge (Optional)

↓

Reason

↓

Select Tool

↓

Execute Tool

↓

Observe Result

↓

Need More Actions?

↓

Yes → Repeat

↓

No

↓

Generate Final Answer

↓

Store Memory
```

This loop continues until the task is complete.

---

# Chatbot vs RAG vs AI Agent

| Feature | Chatbot | RAG | AI Agent |
|---------|---------|-----|----------|
| Answers questions | ✅ | ✅ | ✅ |
| Uses company documents | ❌ | ✅ | ✅ |
| Conversation memory | Limited | ✅ | ✅ |
| Calls external tools | ❌ | ❌ | ✅ |
| Multi-step planning | ❌ | ❌ | ✅ |
| Executes actions | ❌ | ❌ | ✅ |
| Works autonomously | ❌ | ❌ | ✅ |

---

# Real-World Examples

## Example 1 – IT Support Agent

User:

```
Reset my password.
```

Agent:

- Retrieves password policy
- Verifies identity
- Initiates password reset
- Sends confirmation email

---

## Example 2 – HR Agent

User:

```
How many leave days do I have?
```

Agent:

- Queries HR database
- Retrieves leave balance
- Responds with current balance

---

## Example 3 – Finance Agent

User:

```
Generate last month's expense report.
```

Agent:

- Retrieves expense records
- Calculates totals
- Generates PDF
- Emails the report

---

## Example 4 – Healthcare Agent

User:

```
Schedule my next appointment.
```

Agent:

- Checks doctor availability
- Finds free slots
- Books appointment
- Sends confirmation

---

## Example 5 – DevOps Agent

User:

```
Why did deployment fail?
```

Agent:

- Reads CI/CD logs
- Identifies the error
- Suggests a fix
- Creates an incident report

---

# Enterprise AI Agent Architecture

```
                  User

                    │

                    ▼

                 FastAPI

                    │

                    ▼

              AI Agent Core

        ┌───────────┼───────────┐

        ▼           ▼           ▼

     Memory      Tool Registry     RAG

        │           │              │

        ▼           ▼              ▼

      Redis      Calculator     ChromaDB

                    │

                    ▼

                Weather API

                    │

                    ▼

             Final Response
```

---

# Benefits of AI Agents

- Perform tasks instead of only answering questions
- Integrate with enterprise systems
- Automate repetitive work
- Reduce manual effort
- Improve decision-making
- Support multi-step workflows
- Use multiple information sources
- Maintain conversational context

---

# Common Misconceptions

### "AI Agents are just chatbots."

❌ Incorrect

AI Agents can reason, plan, call tools, and perform actions.

---

### "Agents always know everything."

❌ Incorrect

Agents depend on available tools and knowledge sources.

---

### "RAG is the same as an AI Agent."

❌ Incorrect

RAG retrieves knowledge.

AI Agents retrieve knowledge **and** execute actions.

---

# Interview Questions

## Q1. What is an AI Agent?

### Answer

An AI Agent is an intelligent software system that can observe its environment, reason about a goal, use external tools, perform actions, and iteratively work toward completing a task.

---

## Q2. How is an AI Agent different from a chatbot?

### Answer

A chatbot primarily generates conversational responses. An AI Agent can also plan tasks, invoke external tools, access live information, and execute actions.

---

## Q3. What are the main components of an AI Agent?

### Answer

Typical components include:

- Large Language Model
- Memory
- Planner
- Tool Registry
- Tool Executor
- Knowledge Source
- Reasoning Engine

---

## Q4. What is the Observation → Reasoning → Action cycle?

### Answer

It is the fundamental decision-making loop of an AI Agent:

- Observe the current situation.
- Reason about the best next step.
- Execute an action.
- Observe the outcome.
- Repeat until the objective is achieved.

---

## Q5. Can an AI Agent use RAG?

### Answer

Yes.

Modern enterprise AI Agents commonly use RAG as one of several tools. They retrieve relevant documents and combine them with reasoning and tool execution to complete tasks.

---

# AI Architect Notes

A production AI Agent usually includes:

- Authentication
- Authorization
- Memory (Redis)
- Long-term storage (PostgreSQL)
- Vector Database (ChromaDB)
- Tool Registry
- Planner
- Monitoring
- Audit Logging
- Guardrails
- Human Approval for sensitive actions

These components ensure the agent is scalable, secure, and suitable for enterprise environments.

---

# Revision Cheat Sheet

| Concept | Summary |
|----------|---------|
| AI Agent | Software that can reason and act |
| Observation | Gather information |
| Reasoning | Decide what to do |
| Action | Execute tools or workflows |
| Memory | Store previous interactions |
| Planner | Break complex tasks into steps |
| Tools | Extend LLM capabilities |
| RAG | Retrieve external knowledge |

---

# Key Takeaways

- An AI Agent goes beyond answering questions by making decisions and performing actions.
- The Observation → Reasoning → Action cycle is the foundation of agent behavior.
- Memory, planning, and tools make agents significantly more capable than traditional chatbots.
- RAG is an important capability, but it is only one part of a complete AI Agent.
- Enterprise AI systems combine LLMs, memory, tools, and knowledge sources to automate real business workflows.

---

# Next Module

**Day 10 – Module 2: Tool Calling**

You will learn:

- Why LLMs need tools
- Tool schemas
- Function calling
- Tool registry
- Tool execution
- Building your first enterprise AI Agent