from models import Plan

class Planner:
    def create_plan(self, question: str, tool_name: str) -> Plan:
        return Plan(
            question=question,
            tool=tool_name,
            status="READY"
        )

planner = Planner()
