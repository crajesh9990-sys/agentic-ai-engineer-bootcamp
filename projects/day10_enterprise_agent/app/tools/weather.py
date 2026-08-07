class WeatherTool:

    name = "weather"
    description = "Returns current weather."

    DATA = {

        "chennai": {
            "temperature": "31°C",
            "condition": "Sunny"
        },

        "bangalore": {
            "temperature": "25°C",
            "condition": "Cloudy"
        },

        "hyderabad": {
            "temperature": "29°C",
            "condition": "Clear"
        }

    }

    def execute(
        self,
        city: str
    ):

        city = city.lower()

        weather = self.DATA.get(
            city,
            {
                "temperature": "Unknown",
                "condition": "Unknown"
            }
        )

        return {
            "tool": self.name,
            "city": city.title(),
            **weather
        }


weather_tool = WeatherTool()
