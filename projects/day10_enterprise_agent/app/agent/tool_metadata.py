"""
Tool Metadata

Defines all tools available to the agent.
"""


TOOLS = [

    {
        "name": "calculator",
        "description": "Perform arithmetic calculations.",
        "parameters": [
            "operation",
            "a",
            "b"
        ]
    },

    {
        "name": "weather",
        "description": "Get current weather information for a city.",
        "parameters": [
            "city"
        ]
    },

    {
        "name": "datetime",
        "description": "Return today's date, current time and day.",
        "parameters": []
    },

    {
        "name": "rag",
        "description": "Retrieve information and answer questions from the company's knowledge base, policies, and how-to guides.",
        "parameters": [
            "question"
        ]
    }

]