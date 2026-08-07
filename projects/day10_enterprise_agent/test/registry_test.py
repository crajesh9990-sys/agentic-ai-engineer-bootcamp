import sys
import os

# Add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, project_root)

# Import the registry and register the tools
from app.agent.tool_registry import tool_registry
import app.agent.register_tools

def test_list_tools():
    """Tests that the tool registry can list the registered tools."""
    tools = tool_registry.list_tools()
    print(tools)
    assert len(tools) > 0
    assert any(tool['name'] == 'calculator' for tool in tools)