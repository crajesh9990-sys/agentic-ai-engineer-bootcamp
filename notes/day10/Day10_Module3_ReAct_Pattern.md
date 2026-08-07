# Day 10 – Module 3
# ReAct Pattern (Reason + Act)

**Agentic AI Engineer Bootcamp**

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the ReAct Pattern
- Explain why reasoning is important
- Differentiate reasoning from execution
- Understand the ReAct loop
- Build AI Agents that reason before acting
- Explain ReAct in interviews
- Understand how modern AI frameworks implement ReAct

---

# Introduction

Traditional chatbots answer questions.

AI Agents solve problems.

To solve problems, an AI Agent must:

- Think
- Decide
- Act
- Observe
- Think again

This iterative process is known as the **ReAct Pattern**.

---

# What is ReAct?

## Definition

**ReAct** stands for:

```
Reason

+

Act
```

It is an AI Agent framework where the model alternates between:

- Reasoning about the current situation
- Performing an action
- Observing the result
- Continuing until the objective is achieved

---

# Why Do We Need ReAct?

Suppose the user asks:

```
What's the weather in Chennai and email it to my manager?
```

A chatbot responds:

```
I can't send emails.
```

A ReAct Agent thinks differently.

```
Need weather information.

↓

Call Weather Tool.

↓

Receive weather.

↓

Need email tool.

↓

Send email.

↓

Task completed.
```

The agent reasons before every action.

---

# ReAct Workflow

```
User Request

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

Yes

↓

Reason Again

↓

Execute Next Tool

↓

Final Answer
```

---

# Observation → Reasoning → Action

Every ReAct Agent follows this cycle.

```
Observation

↓

Reasoning

↓

Action

↓

Observation

↓

Reasoning

↓

Action
```

This continues until the task is complete.

---

# Understanding Each Stage

## 1. Observation

The agent gathers information.

Examples:

- User request
- Conversation history
- Retrieved documents
- Tool results
- Current state

Example:

```
User:

Calculate the tax for ₹50,000.
```

Observation:

- Amount = ₹50,000
- Tax calculation required

---

## 2. Reasoning

The agent decides what to do.

Example:

```
Need calculator.

↓

Need tax formula.

↓

Perform calculation.
```

The agent has not acted yet.

It is only planning.

---

## 3. Action

The selected tool is executed.

```
Calculator

↓

Tax = ₹9,000
```

---

## 4. Observation Again

The agent receives the tool output.

```
Tax

↓

₹9,000
```

Now the agent decides whether another action is required.

---

# Simple ReAct Example

Question:

```
What is 245 × 89?
```

Reason:

```
Use calculator.
```

Action:

```
245 × 89

↓

21805
```

Final Answer:

```
245 × 89 = 21,805.
```

---

# Multi-Step ReAct Example

Question:

```
What's the weather in Chennai tomorrow?
```

Reason:

```
Need weather data.
```

Action:

```
Weather API
```

Observation:

```
31°C
Sunny
```

Reason:

```
Need final response.
```

Answer:

```
Tomorrow's forecast for Chennai is 31°C and sunny.
```

---

# Complex ReAct Example

User:

```
Plan my business trip to Bengaluru.
```

Reason:

```
Need calendar.

↓

Need flights.

↓

Need hotels.

↓

Need itinerary.
```

Action 1

```
Calendar API
```

Action 2

```
Flight Search
```

Action 3

```
Hotel Search
```

Action 4

```
Create itinerary
```

Final Response:

```
Your trip has been planned successfully.
```

---

# ReAct Loop

```
             User

               │

               ▼

           Observation

               │

               ▼

            Reasoning

               │

               ▼

          Need Tool?

        ┌─────┴─────┐

        │           │

       Yes          No

        │           │

        ▼           ▼

 Execute Tool   Final Answer

        │

        ▼

 Observe Result

        │

        ▼

 Reason Again
```

---

# Why Is Reasoning Important?

Without reasoning:

```
User

↓

Calculator

↓

Weather

↓

Database

↓

Everything
```

The agent wastes time and resources.

With reasoning:

```
Need calculator only.

↓

Calculator

↓

Answer
```

Reasoning improves:

- Accuracy
- Speed
- Cost
- Reliability

---

# ReAct vs Simple Tool Calling

## Simple Tool Calling

```
Question

↓

Tool

↓

Answer
```

One action.

---

## ReAct

```
Question

↓

Reason

↓

Tool

↓

Observe

↓

Reason

↓

Tool

↓

Final Answer
```

Multiple decisions.

---

# Enterprise Example

Question:

```
Reset my password.
```

Reason:

```
Need identity verification.
```

Action:

```
Authentication Service
```

Observation:

```
Verified
```

Reason:

```
Reset password.
```

Action:

```
Password Service
```

Observation:

```
Success
```

Final Response:

```
Your password has been reset successfully.
```

---

# Benefits of ReAct

- Better reasoning
- Multi-step execution
- Reduced hallucinations
- Dynamic decision-making
- More reliable AI Agents
- Supports complex workflows

---

# Limitations

- More API calls
- Higher latency
- Increased token usage
- More implementation complexity

These trade-offs are usually worthwhile for tasks requiring reasoning and external actions.

---

# ReAct in Modern Frameworks

Many AI frameworks implement ReAct concepts.

Examples:

- LangGraph
- CrewAI
- AutoGen
- OpenAI Agents SDK
- Semantic Kernel
- Haystack Agents

Although implementations differ, the reasoning-action cycle remains similar.

---

# Enterprise AI Architecture

```
                 User

                   │

                   ▼

              AI Agent

                   │

                   ▼

               Planner

                   │

         ┌─────────┼─────────┐

         ▼         ▼         ▼

 Calculator    Weather     RAG

         │         │         │

         ▼         ▼         ▼

     Tool Results

           │

           ▼

      Observe Result

           │

           ▼

      Need Another Tool?

           │

           ▼

      Final Response
```

---

# Best Practices

- Keep reasoning separate from execution.
- Execute only the required tools.
- Validate tool results.
- Log every reasoning step.
- Handle tool failures gracefully.
- Avoid infinite reasoning loops.
- Set a maximum number of iterations.

---

# Common Mistakes

❌ Calling every tool

❌ Ignoring previous observations

❌ No planning

❌ No stopping condition

❌ Mixing reasoning and execution logic

---

# Interview Questions

## Q1. What is the ReAct Pattern?

### Answer

ReAct (Reason + Act) is an AI Agent framework where the model alternates between reasoning about a task and executing actions until the objective is achieved.

---

## Q2. Why is reasoning important?

### Answer

Reasoning enables the agent to choose the correct action, avoid unnecessary tool calls, and solve multi-step problems efficiently.

---

## Q3. How is ReAct different from simple tool calling?

### Answer

Simple tool calling usually performs a single action. ReAct repeatedly reasons, acts, observes, and decides whether additional actions are required.

---

## Q4. Why is ReAct useful for enterprise AI?

### Answer

Enterprise workflows often involve multiple systems and dependencies. ReAct enables AI Agents to coordinate these steps intelligently while adapting to intermediate results.

---

## Q5. What should happen if a tool fails?

### Answer

The agent should observe the failure, reason about alternative actions (such as retrying, selecting another tool, or asking the user for clarification), and avoid crashing or producing misleading information.

---

# AI Architect Notes

Production AI Agents typically add safeguards around the ReAct loop:

- Maximum reasoning iterations
- Tool execution timeouts
- Permission checks
- Audit logging
- Human approval for sensitive actions
- Retry and fallback strategies
- Cost and token monitoring

These controls make autonomous agents safer and more reliable.

---

# Revision Cheat Sheet

| Concept | Description |
|----------|-------------|
| Observation | Gather information |
| Reasoning | Decide what to do |
| Action | Execute a tool |
| Observation | Evaluate the result |
| ReAct Loop | Repeat until goal is achieved |
| Planner | Break tasks into steps |
| Tool | External capability used by the agent |

---

# Key Takeaways

- ReAct stands for **Reason + Act**.
- AI Agents solve problems by alternating between reasoning and action.
- Observation, reasoning, and action form a continuous decision-making loop.
- ReAct enables multi-step workflows, adaptive behavior, and tool orchestration.
- Most modern Agentic AI frameworks build on ReAct-style reasoning.

---

# Next Module

## Day 10 – Module 4: Tool Registry

You will learn:

- What a Tool Registry is
- Dynamic tool discovery
- Tool metadata
- Tool schemas
- Tool execution
- Building your first production-ready Tool Registry