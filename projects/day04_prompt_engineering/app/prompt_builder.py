from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str, **kwargs) -> str:
    prompt_file = PROMPTS_DIR / filename

    with open(prompt_file, "r", encoding="utf-8") as f:
        template = f.read()

    return template.format(**kwargs)

def explain_prompt(topic: str) -> str:
    return load_prompt("explain.txt", topic=topic) 

def summarize_prompt(topic: str) -> str:
    return load_prompt("summarize.txt", topic=topic)

def interview_prompt(topic: str) -> str:
    return load_prompt("interview.txt", topic=topic)

def code_prompt(task: str) -> str:
    return load_prompt("code.txt", task=task)

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

def architect_prompt(requirement: str) -> str:
    return load_prompt("architect.txt", requirement=requirement)

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
