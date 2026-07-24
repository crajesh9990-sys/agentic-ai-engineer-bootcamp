from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

class PromptService:
    def load_prompt(self, filename: str, **kwargs) -> str:
        prompt_file = PROMPTS_DIR / filename

        with open(prompt_file, "r", encoding="utf-8") as f:
            template = f.read()

        return template.format(**kwargs)

    def explain_prompt(self, topic: str) -> str:
        return self.load_prompt("explain.txt", topic=topic) 

    def summarize_prompt(self, topic: str) -> str:
        return self.load_prompt("summarize.txt", topic=topic)

    def interview_prompt(self, topic: str) -> str:
        return self.load_prompt("interview.txt", topic=topic)

    def code_prompt(self, task: str) -> str:
        return self.load_prompt("code.txt", task=task)

    def rewrite_prompt(self, text: str) -> str:
        return self.load_prompt("rewrite.txt", text=text)

    def architect_prompt(self, requirement: str) -> str:
        return self.load_prompt("architect.txt", requirement=requirement)

    def review_code_prompt(self, code: str) -> str:
        return self.load_prompt("codereview.txt", code=code)

    def programming_language_prompt(self, language: str, task: str) -> str:
        return self.load_prompt("program.txt", language=language, task=task)

    def persona_prompt(self, role: str, question: str) -> str:
        return self.load_prompt("persona.txt", role=role, question=question)
