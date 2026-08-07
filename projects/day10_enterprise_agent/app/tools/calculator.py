from typing import Dict

class CalculatorTool:
    name = "calculator"
    description = "Performs mathematical calculations."

    def execute(self, operation: str, a: float, b: float) -> Dict:
        if operation == "addition":
            result = a + b

        elif operation == "subtraction":
            result = a - b

        elif operation == "multiplication":
            result = a * b

        elif operation == "division":

            if b == 0:
                raise ValueError("Division by zero.")

            result = a / b

        else:
            raise ValueError(
                f"Unsupported operation: {operation}"
            )

        return {
            "tool": self.name,
            "operation": operation,
            "result": result
        }

calculator_tool = CalculatorTool() 
