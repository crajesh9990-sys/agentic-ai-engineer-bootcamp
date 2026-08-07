from pathlib import Path

class PromptLoader:

    @staticmethod
    def load_prompt(prompt_name: str) -> str:
        prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / f"{prompt_name}"
        )
        with open(prompt_path, "r") as f:
            return f.read()

