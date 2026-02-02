from .base import WeatherResponse

def is_cold(weather: WeatherResponse) -> bool:
    return weather.temperature < 15
