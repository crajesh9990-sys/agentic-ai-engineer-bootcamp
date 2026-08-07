# Day 10 – Module 4
# Tool Registry

**Agentic AI Engineer Bootcamp**

---

# Learning Objectives

After completing this module, you will be able to:

- Understand what a Tool Registry is
- Explain why AI Agents need a Tool Registry
- Build a Tool Registry in Python
- Register tools dynamically
- Execute tools by name
- Understand Tool Metadata
- Understand Tool Discovery
- Explain Tool Registry architecture in interviews

---

# Introduction

Imagine building an AI Agent with multiple tools:

- Calculator
- Weather
- Calendar
- Email
- Database
- Search
- RAG

How does the AI know which tools exist?

How does it execute a tool?

The answer is:

**Tool Registry**

---

# What is a Tool Registry?

## Definition

A Tool Registry is a centralized component that stores information about all available tools and provides a mechanism for discovering and executing them.

Think of it as a **directory of capabilities** available to an AI Agent.

---

# Real-World Analogy

Imagine a hotel reception.

A guest asks:

```
I need a taxi.
```

The receptionist doesn't drive the taxi.

Instead,

the receptionist knows:

- Taxi service
- Restaurant
- Laundry
- Doctor
- Room Service

The receptionist simply connects the guest with the correct service.

The Tool Registry works the same way.

---

# Why Do We Need a Tool Registry?

Without a registry:

```python
if "weather" in question:
    ...

elif "calculator" in question:
    ...

elif "database" in question:
    ...
```

Problems:

- Hard to maintain
- Difficult to add tools
- Not scalable
- Violates the Open/Closed Principle

---

With a Tool Registry:

```python
registry.register(weather_tool)

registry.register(calculator_tool)

registry.execute(...)
```

No changes are required when adding new tools.

---

# Tool Registry Architecture

```
              User

                │

                ▼

            AI Agent

                │

                ▼

          Tool Registry

      ┌─────────┼─────────┐

      ▼         ▼         ▼

 Calculator   Weather    Search

      ▼         ▼         ▼

   Result    Result    Result
```

The Tool Registry acts as the central directory.

---

# Components of a Tool Registry

A Tool Registry generally contains:

- Tool Name
- Description
- Parameters
- Function Reference
- Metadata

Example:

```
Tool Name

↓

Calculator

↓

Description

↓

Performs arithmetic calculations.

↓

Function

↓

calculator_tool()

↓

Parameters

↓

operation

a

b
```

---

# Simple Python Example

```python
TOOLS = {

    "calculator": calculator_tool,

    "weather": weather_tool,

    "search": search_tool

}
```

Now the AI Agent simply asks:

```
Do we have a calculator?
```

Instead of:

```
Where is the calculator code?
```

---

# Dynamic Registration

Instead of hardcoding tools,

register them dynamically.

```python
registry.register(

    name="calculator",

    tool=calculator_tool

)
```

Later

```python
registry.register(

    name="email",

    tool=email_tool

)
```

No other code changes.

---

# Tool Metadata

Every tool should describe itself.

Example

```python
{

"name":"weather",

"description":

"Returns current weather.",

"parameters":[

"city"

]

}
```

Metadata helps the AI choose the correct tool.

---

# Tool Discovery

Suppose your agent has 100 tools.

Instead of searching source code,

it asks the Tool Registry:

```
Available Tools

↓

Weather

Calculator

Search

Email

Calendar

Database
```

The LLM can reason about which tool to use.

---

# Tool Execution

After selecting a tool,

the registry executes it.

Example

```
Weather

↓

weather_tool("Chennai")

↓

31°C

Sunny
```

The registry returns the result to the AI Agent.

---

# Example Registry Class

```python
class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(

        self,

        name,

        tool

    ):

        self.tools[name] = tool

    def get(

        self,

        name

    ):

        return self.tools.get(name)

    def execute(

        self,

        name,

        *args,

        **kwargs

    ):

        tool = self.get(name)

        if tool is None:

            raise Exception(

                "Tool not found."

            )

        return tool(

            *args,

            **kwargs

        )
```

---

# Using the Registry

Register tools

```python
registry.register(

    "calculator",

    calculator_tool

)

registry.register(

    "weather",

    weather_tool
)
```

Execute

```python
registry.execute(

    "calculator",

    5,

    8
)
```

Output

```
13
```

---

# Enterprise Registry

Enterprise systems store much more information.

```
Tool

↓

Description

↓

Parameters

↓

Permissions

↓

Version

↓

Owner

↓

Timeout

↓

Authentication

↓

Logging
```

Example

```json
{
  "name":"weather",

  "description":

  "Returns weather information.",

  "version":"1.2",

  "owner":"Platform Team",

  "timeout":"10 seconds"
}
```

---

# Why Metadata Matters

Suppose there are two tools.

```
Weather

↓

Current Weather
```

```
Forecast

↓

7-Day Forecast
```

The descriptions help the AI select the correct tool.

---

# Tool Registry in Enterprise AI

Typical tools:

- Calculator
- Weather
- SQL
- SAP
- Salesforce
- Jira
- GitHub
- Outlook
- Teams
- Slack
- ServiceNow
- ChromaDB
- PostgreSQL

The registry provides one place to manage them all.

---

# AI Agent Flow

```
User Request

↓

Planner

↓

Need Tool?

↓

Tool Registry

↓

Execute Tool

↓

Receive Result

↓

Final Answer
```

---

# Benefits

- Centralized management
- Easy to extend
- Dynamic discovery
- Cleaner architecture
- Better maintainability
- Easier testing
- Enterprise scalability

---

# Best Practices

- Register tools during application startup.
- Use descriptive names.
- Include metadata.
- Validate parameters.
- Handle execution failures.
- Log every invocation.
- Restrict sensitive tools.

---

# Common Mistakes

❌ Hardcoding tool selection

❌ Duplicate tool names

❌ Missing metadata

❌ No error handling

❌ No authentication

❌ Exposing dangerous tools

---

# Interview Questions

## Q1. What is a Tool Registry?

### Answer

A Tool Registry is a centralized component that stores available tools, their metadata, and provides a mechanism for discovering and executing them.

---

## Q2. Why is a Tool Registry important?

### Answer

It decouples the AI Agent from individual tool implementations, making the system easier to extend, maintain, and scale.

---

## Q3. What information should a Tool Registry store?

### Answer

A Tool Registry should store:

- Tool name
- Description
- Parameters
- Function reference
- Metadata
- Permissions
- Version (optional)

---

## Q4. How does a Tool Registry improve scalability?

### Answer

New tools can be registered without changing the agent's core logic. This follows the Open/Closed Principle and simplifies maintenance.

---

## Q5. What happens if a tool isn't found?

### Answer

The registry should return a controlled error, allowing the agent to recover gracefully or ask the user for clarification.

---

# AI Architect Notes

In enterprise systems, Tool Registries often include:

- Role-based access control (RBAC)
- Tool versioning
- Usage analytics
- Audit logs
- Execution timeouts
- Retry policies
- Health checks
- Dynamic loading of tools

This allows organizations to manage hundreds of tools safely and consistently.

---

# Revision Cheat Sheet

| Concept | Description |
|----------|-------------|
| Tool Registry | Central directory of tools |
| Tool Metadata | Information describing a tool |
| Tool Discovery | Finding available tools |
| Tool Execution | Running the selected tool |
| Dynamic Registration | Adding tools without changing agent logic |
| Registry Pattern | Design pattern for centralized management |

---

# Key Takeaways

- A Tool Registry is the central hub that manages all tools available to an AI Agent.
- It enables dynamic discovery, execution, and extension of tools.
- Metadata helps the LLM understand when and how to use a tool.
- Tool Registries improve scalability, maintainability, and testability.
- Most enterprise AI frameworks use some form of Tool Registry internally.

---

# Next Module

## Day 10 – Module 5: Agent Loop

You will learn:

- What an Agent Loop is
- Planning and execution cycles
- Tool invocation loops
- Stopping conditions
- Error recovery
- Building your first autonomous AI Agent