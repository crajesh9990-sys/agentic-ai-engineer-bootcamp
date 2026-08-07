import sys
import os

# Add the project root to the Python path to allow importing modules from 'app'
# This assumes the project root is one level up from the current file (test/ -> day10_enterprise_agent/)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, project_root)

from app.tools.weather import weather_tool

print(
    weather_tool.execute(
        "Chennai"
    )
)