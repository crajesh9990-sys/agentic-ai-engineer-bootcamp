from fastapi import APIRouter
import logging

from .agent.agent_loop import agent_loop
from .agent import register_tools
from .agent.tool_registry import tool_registry

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/tools")
def list_tools():
    logger.info("Available tools: %s", tool_registry.list_tools())
    return tool_registry.list_tools()

@router.post("/agent")
def agent(request: dict):
    question = request["question"]
    return agent_loop.run(question)
