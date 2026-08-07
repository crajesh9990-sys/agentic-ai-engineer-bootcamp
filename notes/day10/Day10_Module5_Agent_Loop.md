# Day 10 – Module 5
# Agent Loop

**Agentic AI Engineer Bootcamp**

---

# Learning Objectives

After completing this module, you will be able to:

- Understand what an Agent Loop is
- Explain why AI Agents require loops
- Understand the Observe → Reason → Act cycle
- Build a simple Agent Loop in Python
- Understand stopping conditions
- Handle tool failures
- Explain Agent Loops in interviews
- Understand how enterprise AI Agents work internally

---

# Introduction

A chatbot usually answers a question once.

```
Question

↓

LLM

↓

Answer
```

An AI Agent is different.

It repeatedly thinks, acts, observes, and decides whether additional work is required.

This repeated execution is called the **Agent Loop**.

---

# What is an Agent Loop?

## Definition

An **Agent Loop** is a continuous execution cycle in which an AI Agent:

- Observes the current state
- Reasons about the next action
- Executes a tool if required
- Observes the result
- Decides whether to continue or stop

The loop continues until the task is complete.

---

# Why Do We Need an Agent Loop?

Consider this request:

```
Plan my business trip.
```

Can the AI answer immediately?

No.

It must:

- Check your calendar
- Search for flights
- Find hotels
- Calculate costs
- Build an itinerary

One response is not enough.

The AI must perform multiple steps.

---

# High-Level Workflow

```
User Request

↓

Observe

↓

Reason

↓

Need Tool?

↓

Execute Tool

↓

Observe Result

↓

Need Another Action?

↓

Yes

↓

Repeat

↓

No

↓

Final Answer
```

---

# Observation

Observation means gathering information.

Sources include:

- User request
- Conversation history
- Memory
- Tool results
- RAG documents
- Current environment

Example:

```
User

↓

Book a meeting tomorrow.
```

Observation:

- Meeting requested
- Date mentioned
- Calendar required

---

# Reasoning

The AI decides what should happen next.

Example:

```
Need Calendar Tool

↓

Need available time slots

↓

Book meeting
```

Reasoning does not execute anything.

It only plans.

---

# Action

The selected tool is executed.

Example:

```
Calendar Tool

↓

Available at 2 PM
```

---

# Observation Again

The AI receives the result.

```
Calendar says:

2 PM available
```

The AI now asks:

```
Need another action?
```

If yes,

the loop continues.

---

# Example 1 – Calculator

User

```
Calculate 45 × 12
```

Loop

```
Observe

↓

Need Calculator

↓

Execute

↓

540

↓

Stop
```

Final Answer

```
540
```

---

# Example 2 – Weather

User

```
What's the weather in Chennai?
```

Loop

```
Observe

↓

Need Weather Tool

↓

Execute

↓

31°C

↓

Stop
```

---

# Example 3 – Business Trip

User

```
Plan my trip to Bengaluru.
```

Loop

```
Observe

↓

Calendar

↓

Observe

↓

Flights

↓

Observe

↓

Hotels

↓

Observe

↓

Create Itinerary

↓

Stop
```

---

# Visual Flow

```
                User

                  │

                  ▼

             AI Agent

                  │

          Observe Request

                  │

                  ▼

             Reasoning

                  │

          Need Tool?

      ┌───────────┴───────────┐

      │                       │

     Yes                      No

      │                       │

      ▼                       ▼

 Execute Tool          Final Response

      │

      ▼

Observe Result

      │

      ▼

Need Another Tool?

      │

      ▼

Repeat Loop
```

---

# Simple Python Agent Loop

```python
while True:

    observation = observe()

    action = reason(observation)

    if action is None:

        break

    result = execute(action)

    update_memory(result)
```

This is the foundation of every AI Agent.

---

# Agent Loop Components

A production Agent Loop usually contains:

- User Input
- Memory
- Planner
- Tool Selector
- Tool Executor
- Observation
- Reasoning
- Final Response

---

# Agent Loop with RAG

```
Question

↓

Observe

↓

Need Knowledge?

↓

Retrieve Documents

↓

Reason

↓

Need Tool?

↓

Execute Tool

↓

Observe

↓

Answer
```

The AI combines retrieval and tool execution.

---

# Stopping Conditions

Every Agent Loop must know when to stop.

Examples:

- Goal completed
- No additional tools required
- Maximum iterations reached
- Tool failure
- User cancellation

Without stopping conditions, an agent could loop indefinitely.

---

# Maximum Iterations

Production agents often limit execution.

Example:

```python
MAX_ITERATIONS = 5
```

If the limit is reached,

the AI stops safely and returns the best available response.

---

# Error Handling

Suppose the Weather API fails.

```
Weather Tool

↓

Error
```

The AI can:

- Retry
- Use cached information
- Ask the user to try later
- Choose another tool

The loop should recover gracefully.

---

# Agent Memory

After every action,

the result is stored.

```
User

↓

Tool

↓

Result

↓

Memory
```

The next reasoning step uses the updated memory.

---

# Enterprise Agent Loop

```
               User

                 │

                 ▼

             AI Agent

                 │

         Conversation Memory

                 │

                 ▼

             Planner

                 │

         Need Tool?

      ┌──────────┼───────────┐

      ▼          ▼           ▼

 Calculator   Weather      RAG

      │          │           │

      ▼          ▼           ▼

  Tool Results

      │

      ▼

 Update Memory

      │

      ▼

 Continue?

      │

      ▼

 Final Response
```

---

# Benefits

- Supports multi-step reasoning
- Handles complex workflows
- Enables tool orchestration
- Supports autonomous execution
- Makes AI more reliable

---

# Common Mistakes

❌ No stopping condition

❌ Infinite loops

❌ Ignoring tool failures

❌ Not updating memory

❌ Executing unnecessary tools

❌ Mixing reasoning with execution logic

---

# Best Practices

- Keep reasoning separate from execution.
- Define clear stopping conditions.
- Set a maximum iteration limit.
- Log each reasoning step.
- Store observations in memory.
- Handle failures gracefully.
- Validate tool outputs.

---

# Interview Questions

## Q1. What is an Agent Loop?

### Answer

An Agent Loop is the continuous cycle in which an AI Agent observes the current state, reasons about the next action, executes tools, evaluates the results, and repeats until the objective is achieved.

---

## Q2. Why do AI Agents use loops?

### Answer

Many real-world tasks require multiple steps and intermediate decisions. A loop allows the agent to adapt based on new information rather than assuming a single action is sufficient.

---

## Q3. What are stopping conditions?

### Answer

Stopping conditions determine when an AI Agent should terminate its execution. Examples include task completion, reaching the maximum number of iterations, or encountering an unrecoverable error.

---

## Q4. What happens if a tool fails?

### Answer

A robust agent observes the failure, logs it, decides whether to retry, switch to another tool, or ask the user for clarification, and avoids crashing unexpectedly.

---

## Q5. Why separate reasoning from execution?

### Answer

Separating reasoning from execution improves maintainability, testability, and flexibility. The reasoning component decides *what* should happen, while the executor is responsible for *how* it happens.

---

# AI Architect Notes

Enterprise AI Agents typically enhance the Agent Loop with:

- Retry policies
- Timeout management
- Human approval workflows
- Audit logging
- Token usage tracking
- Cost monitoring
- Guardrails
- Parallel tool execution
- Checkpointing and recovery

These capabilities make autonomous systems safer and more scalable.

---

# Agent Loop vs Traditional Program

| Traditional Program | AI Agent |
|---------------------|----------|
| Fixed sequence of instructions | Dynamic decision-making |
| Predefined workflow | Adapts at runtime |
| Minimal reasoning | Continuous reasoning |
| Executes known steps | Selects actions dynamically |

---

# Revision Cheat Sheet

| Concept | Description |
|----------|-------------|
| Observation | Gather information |
| Reasoning | Decide the next action |
| Action | Execute a tool |
| Memory | Store results for future decisions |
| Loop | Repeat until goal is reached |
| Stop Condition | Safely terminate execution |

---

# Key Takeaways

- The Agent Loop is the execution engine of an AI Agent.
- It repeatedly observes, reasons, acts, and evaluates results.
- Multi-step tasks require iterative decision-making.
- Stopping conditions and error handling are essential for safe execution.
- Every major enterprise AI framework implements some form of an Agent Loop.

---

# Next Module

## Day 10 – Module 6: Enterprise Agent Architecture

You will learn:

- Planner
- Tool Registry
- Tool Executor
- Memory
- RAG Integration
- Guardrails
- Logging
- Observability
- Production AI Agent Design