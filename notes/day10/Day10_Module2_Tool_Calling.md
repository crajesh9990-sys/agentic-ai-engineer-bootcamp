# Day 10 – Module 2
# Tool Calling (Function Calling)

**Agentic AI Engineer Bootcamp**

---

# Learning Objectives

After completing this module, you will be able to:

- Understand Tool Calling
- Explain why LLMs need tools
- Understand Function Calling
- Build a Tool Registry
- Design Tool Schemas
- Understand Tool Execution Flow
- Build simple AI Agents
- Answer interview questions confidently

---

# Introduction

Large Language Models (LLMs) are excellent at reasoning and generating text.

However, they have one major limitation.

They **cannot perform actions by themselves.**

For example, if you ask:

```
What is 245 × 89?
```

The model may calculate it correctly.

But if you ask:

```
What is the weather in Chennai right now?
```

The LLM does **not** know.

Why?

Because the weather changes continuously.

The LLM has no access to real-time information.

This is where **Tool Calling** becomes essential.

---

# What is Tool Calling?

## Definition

Tool Calling is the process where an AI model decides that it requires external information or an external capability, invokes the appropriate tool, receives the result, and then uses that result to generate its final response.

Think of the LLM as a manager.

The manager doesn't perform every task personally.

Instead, the manager delegates work to specialists.

---

# Real World Analogy

Imagine a CEO.

The CEO receives a request.

```
Prepare this month's sales report.
```

The CEO doesn't calculate everything manually.

Instead:

```
CEO

↓

Finance Team

↓

Sales Database

↓

Report

↓

CEO

↓

Customer
```

The CEO coordinates.

Similarly,

An AI Agent coordinates tools.

---

# Why Do LLMs Need Tools?

LLMs cannot:

- Read your local files
- Access SQL databases
- Read SharePoint
- Query SAP
- Send emails
- Call REST APIs
- Check live weather
- Execute Python
- Book meetings

They need external tools.

---

# Examples of AI Tools

Examples include:

- Calculator
- Weather API
- Search Engine
- SQL Database
- Email Sender
- Calendar
- PDF Reader
- File System
- Stock Market API
- CRM
- ERP
- HR System

Each tool extends the capabilities of the LLM.

---

# Basic Tool Calling Flow

```
User

↓

LLM

↓

Need Tool?

↓

YES

↓

Execute Tool

↓

Tool Result

↓

LLM

↓

Final Answer
```

---

# Example 1 – Calculator

User

```
What is 85 × 12?
```

Agent

↓

Calculator Tool

↓

1020

↓

LLM

↓

```
The answer is 1020.
```

---

# Example 2 – Weather

User

```
What's the weather in Chennai?
```

LLM

↓

Weather API

↓

```
31°C

Sunny
```

↓

LLM

↓

```
The weather in Chennai is 31°C and sunny.
```

---

# Example 3 – SQL Database

User

```
How many employees joined last month?
```

Agent

↓

Database Tool

↓

SQL Query

↓

42 Employees

↓

LLM

↓

```
42 employees joined last month.
```

---

# Tool Calling vs RAG

Many beginners confuse these concepts.

## RAG

Purpose:

Retrieve documents.

```
Question

↓

Vector Database

↓

Documents

↓

LLM
```

---

## Tool Calling

Purpose:

Execute actions.

```
Question

↓

Weather API

↓

Temperature

↓

LLM
```

---

# Tool Calling + RAG

Enterprise AI combines both.

```
Question

↓

Need Knowledge?

↓

ChromaDB

↓

Need Live Data?

↓

Weather Tool

↓

LLM

↓

Answer
```

---

# Components of Tool Calling

A complete tool calling system contains:

- Tool Registry
- Tool Schema
- Tool Selector
- Tool Executor
- Tool Result
- Final Response

---

# Tool Registry

A Tool Registry stores all available tools.

Example:

```python
TOOLS = {

    "calculator": calculator_tool,

    "weather": weather_tool,

    "search": search_tool

}
```

Instead of hardcoding tool selection,

the agent searches the registry.

---

# Tool Schema

Every tool has a schema.

Example

Calculator

```json
{
  "name":"calculator",

  "description":"Performs arithmetic calculations.",

  "parameters":{

      "operation":"multiply",

      "a":5,

      "b":8

  }
}
```

The schema tells the model:

- Tool name
- Purpose
- Inputs
- Output

---

# Tool Executor

The Tool Executor actually runs the tool.

Example

```
Calculator

↓

5 × 8

↓

40
```

The LLM never performs the action itself.

It only decides **which tool** should be executed.

---

# Enterprise Tool Calling Flow

```
User Request

↓

Planner

↓

Need Tool?

↓

Select Tool

↓

Execute Tool

↓

Receive Result

↓

Generate Final Response
```

---

# Building Your Own Tool

Example

```python
def weather(city):

    return {

        "city": city,

        "temperature": "31°C",

        "condition": "Sunny"

    }
```

The LLM can now call this function.

---

# Multiple Tools

One request may require multiple tools.

Example

```
Email today's weather to my manager.
```

Execution

```
Weather Tool

↓

Email Tool

↓

Success
```

The agent chains multiple tools together.

---

# Multi-Step Tool Calling

Example

```
Book my vacation.
```

Step 1

Calendar Tool

↓

Available dates

↓

Step 2

Flight Search

↓

Flights

↓

Step 3

Hotel Search

↓

Hotels

↓

Step 4

Booking Tool

↓

Reservation

↓

Final Response

```
Your vacation has been booked.
```

---

# Benefits of Tool Calling

- Real-time information
- Automation
- External system integration
- Better decision-making
- Enterprise workflow support
- Reduced hallucinations
- Increased reliability

---

# Common Mistakes

❌ Trying to make the LLM do everything

❌ Not validating tool inputs

❌ Exposing unsafe tools

❌ No error handling

❌ Hardcoding tool selection everywhere

---

# Tool Calling in Enterprise Applications

Typical tools include:

- SAP
- Salesforce
- ServiceNow
- Jira
- GitHub
- Azure DevOps
- Outlook
- Microsoft Teams
- Slack
- PostgreSQL
- MongoDB
- ChromaDB

---

# AI Architect View

```
                  User

                    │

                    ▼

                AI Agent

                    │

          ┌─────────┼───────────┐

          ▼         ▼           ▼

      Calculator  Weather    ChromaDB

          │         │           │

          ▼         ▼           ▼

       Result    Result     Documents

                │

                ▼

           Final Answer
```

---

# Interview Questions

## Q1. What is Tool Calling?

### Answer

Tool Calling is the mechanism by which an AI model identifies the need for external information or functionality, invokes the appropriate tool, receives its output, and incorporates that output into the final response.

---

## Q2. Why do LLMs need tools?

### Answer

LLMs cannot access live data or interact with external systems by themselves. Tools allow them to retrieve current information and perform actions such as querying databases, calling APIs, or sending emails.

---

## Q3. What is the difference between Tool Calling and RAG?

### Answer

RAG retrieves documents to improve answers, while Tool Calling executes external functions or services to perform actions or obtain live information.

---

## Q4. What is a Tool Registry?

### Answer

A Tool Registry is a centralized collection of available tools that the AI Agent can discover and invoke.

---

## Q5. Can an AI Agent use multiple tools?

### Answer

Yes.

Enterprise AI Agents frequently chain multiple tools together to complete complex tasks.

Example:

Weather API → Email Service → Calendar

---

# Best Practices

- Keep tools focused on a single responsibility.
- Validate all tool inputs.
- Handle failures gracefully.
- Log every tool invocation.
- Restrict access to sensitive tools.
- Use structured schemas.
- Separate planning from execution.

---

# Revision Cheat Sheet

| Concept | Description |
|----------|-------------|
| Tool Calling | AI invokes external functionality |
| Tool Registry | Stores available tools |
| Tool Schema | Defines tool interface |
| Tool Executor | Runs the selected tool |
| Tool Result | Output returned by the tool |
| Function Calling | A common implementation of Tool Calling |
| RAG | Retrieves documents |
| AI Agent | Reasons, selects tools, and executes actions |

---

# Key Takeaways

- LLMs are excellent at reasoning but require tools to interact with the outside world.
- Tool Calling allows AI systems to execute actions and retrieve live information.
- Enterprise AI applications combine Tool Calling with RAG, memory, and planning.
- Tool Registries and Tool Schemas make AI systems extensible and maintainable.
- Tool Calling is one of the core capabilities that transforms a chatbot into an AI Agent.

---

# Next Module

## Day 10 – Module 3

You will learn:

- ReAct Pattern
- Reasoning Loop
- Planning
- Acting
- Observing
- Building your first AI Agent loop