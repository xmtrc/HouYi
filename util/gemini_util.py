from google import genai
from google.genai import types

import json
import pathlib
import time

# load config file from root path
config_file_path = pathlib.Path("./config.json")

# read config file
config = json.load(open(config_file_path))

# init gemini api key
client = genai.Client(api_key=config["gemini_key"])

def completion_with_gemini(text: str, model: str = "gemini-2.5-flash-lite") -> str:
  time.sleep(60)
  response = client.models.generate_content(
    model=model,
    contents=text,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
  )
  return response.text
