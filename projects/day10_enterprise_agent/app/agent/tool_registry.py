from typing import Dict
import logging

logger = logging.getLogger(__name__)

class ToolRegistry:
    def __init__(self):
        self.tools: Dict = {}

    def register(self, tool):
        logger.info(f"Registering tool: {tool.name}")
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def execute(self, name, **kwargs):
        tool = self.tools.get(name)
        if tool is None:
            raise Exception(f"Tool '{name}' not found.")
        
        return tool.execute(**kwargs)

    def list_tools(self):
        return [
            {
                "name": tool.name,
                "description": tool.description
            }
            for tool in self.tools.values()
        ]

tool_registry = ToolRegistry()