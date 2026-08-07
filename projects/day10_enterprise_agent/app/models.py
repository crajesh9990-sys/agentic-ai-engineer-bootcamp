from dataclasses import dataclass

@dataclass
class Plan:
    question: str
    tool: str
    status: str = "READY"


