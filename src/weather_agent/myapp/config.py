import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "zh")
