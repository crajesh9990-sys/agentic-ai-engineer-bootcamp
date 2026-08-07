# datetime_tool.py

from datetime import datetime, timedelta
import pytz

class DateTimeTool:
    name = "datetime"
    description = "Returns current date and time."

    def execute(self):
        now = datetime.now()

        return {
            "tool": self.name,
            "date": now.strftime(
                "%Y-%m-%d"
            ),
            "time": now.strftime(
                "%H:%M:%S"
            ),
            "day": now.strftime(
                "%A"
            )
        }
    
    def get_current_time(timezone: str = "UTC") -> str:
        """
        Returns the current date and time in a specified timezone.

        Args:
            timezone: The target timezone (e.g., "America/Los_Angeles"). Defaults to UTC.

        Returns:
            A formatted string representing the current time.
        """
        try:
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            return now.strftime("%Y-%m-%d %H:%M:%S %Z")
        except pytz.UnknownTimeZoneError:
            return f"Error: Unknown timezone '{timezone}'"

    def add_time(start_dt_str: str, days: int = 0, hours: int = 0) -> str:
        """
        Calculates a future date by adding relative time components to a starting datetime string.

        Args:
            start_dt_str: The starting date/time in YYYY-MM-DD format.
            days: Number of days to add. Defaults to 0.
            hours: Number of hours to add. Defaults to 0.

        Returns:
            The resulting date/time string, or an error message.
        """
        # Placeholder: Requires robust parsing logic for start_dt_str in a real system.
        print(f"Calculating new date from {start_dt_str}...")
        return "Calculated future date string"

datetime_tool = DateTimeTool()