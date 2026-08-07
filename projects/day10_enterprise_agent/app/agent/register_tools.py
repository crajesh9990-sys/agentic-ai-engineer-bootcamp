import logging

from .tool_registry import tool_registry
from ..tools.calculator import calculator_tool
from ..tools.datetime_tool import datetime_tool
from ..tools.rag_tool import rag_tool
from ..tools.weather import weather_tool

logger = logging.getLogger(__name__)

logger.info("Registering tools...")
tool_registry.register(tool=calculator_tool)
tool_registry.register(tool=datetime_tool)
tool_registry.register(tool=rag_tool)
tool_registry.register(tool=weather_tool)


