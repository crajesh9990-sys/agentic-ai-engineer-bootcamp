from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str, **kwargs) -> str:
    prompt_file = PROMPTS_DIR / filename

    with open(prompt_file, "r", encoding="utf-8") as f:
        template = f.read()

    return template.format(**kwargs)

def explain_prompt(topic: str) -> str:
    return load_prompt("explain.txt", topic=topic) 

# print("Explain Prompt: ", explain_prompt("LangGraph"))

def summarize_prompt(topic: str) -> str:
    return load_prompt("summarize.txt", topic=topic)

# print("Summarize Prompt: ", summarize_prompt("Traditional relational databases store data in neat rows and columns, making them ideal for structured text or exact keyword searches. In contrast, vector databases are specialized systems designed to handle unstructured data—such as text, images, audio, and video—by converting it into high-dimensional numerical arrays called vector embeddings. Using advanced indexing algorithms like Hierarchical Navigable Small World (HNSW), these databases can execute vector searches to find item similarity rather than exact matches. This ability to instantly measure semantic context makes vector databases a critical foundation for modern AI applications, enabling fast retrieval-augmented generation (RAG) for large language models, accurate recommendation engines, and complex image recognition systems."))

def interview_prompt(topic: str) -> str:
    return load_prompt("interview.txt", topic=topic)

# print("Interview Prompt: ", interview_prompt("FastAPI"))


def code_prompt(task: str) -> str:
    return load_prompt("code.txt", task=task)

# print("Code Prompt: ", code_prompt("Fast API post for reading products from database"))

def rewrite_prompt(text: str) -> str:
    return f"""
    You are an expert technical writer.

    Rewrite the following text professionally.

    Text:
    {text}

    Requirements:

    - Improve grammar.
    - Improve clarity.
    - Keep the original meaning.
    - Make it concise.
    - Use a professional tone.

    Return only the rewritten text.
    """

# print("Rewrite Prompt: ", rewrite_prompt("Email is not good"))

def architect_prompt(requirement: str) -> str:
    return load_prompt("architect.txt", requirement=requirement)

# print("Architect Prompt: ", architect_prompt("Simple mobile app to track investments"))

def review_code_prompt(code: str) -> str:
    return f"""
    You are a Senior Software Engineer conducting a code review.

    Review the following code.

    Code:
    {code}

    Return:

    1. Strengths
    2. Issues
    3. Security Concerns
    4. Performance Improvements
    5. Refactored Version
    """

sample_code = """
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()
"""
# print("Code review Prompt: ", review_code_prompt(sample_code))

def programming_language_prompt(language: str, task: str) -> str:
    return f"""
    You are a Senior Software Engineer.

    Generate production-quality {language} code.

    Task:
    {task}

    Requirements:

    - Follow best practices for {language}.
    - Include comments.
    - Use meaningful variable names.
    - Handle exceptions.
    - Use functions where appropriate.
    - Explain the code after generating it.

    Return the complete solution.
    """

# print("Programming Language Prompt: ", programming_language_prompt("Python", "recursive programm"))

def persona_prompt(role: str, question: str) -> str:
    return f"""
    You are a {role} with 20 years of enterprise experience.

    Answer the following question:

    Question:
    {question}

    Requirements:

    - Provide a detailed answer.
    - Include examples if applicable.
    - Use a professional tone.
    - Keep the answer concise and clear.

    Return only the answer.
    """

# print("Persona Prompt: ", persona_prompt("software architect", "Build an AI Agent for daily usage"))
