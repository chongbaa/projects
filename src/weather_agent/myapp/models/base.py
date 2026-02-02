from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temperature: float
    description: str
