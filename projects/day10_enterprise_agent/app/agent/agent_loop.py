from .agent import agent


class AgentLoop:
    MAX_ITERATIONS = 5

    def run(self, question: str):
        observation = question

        iteration = 1

        while iteration <= self.MAX_ITERATIONS:
            result = agent.process(
                observation
            )

            return {
                "iterations": iteration,
                "observation": observation,
                "result": result
            
            }


        return {
            "completed": False,
            "reason": "Max iterations reached."
        }

agent_loop = AgentLoop()
