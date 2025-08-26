from util.openai_util import completion_with_chatgpt
from util.gemini_util import completion_with_gemini

import json
import pathlib
import loguru

# load config file from root path
config_file_path = pathlib.Path("./config.json")

# read config file
config = json.load(open(config_file_path))

logger = loguru.logger

def completion_with_llm(text: str) -> str:
  chosen_llm = config["llm"]

  if chosen_llm == "chatgpt":
    return completion_with_chatgpt(text)
  elif chosen_llm == "gemini":
    return completion_with_gemini(text)
  else:
    logger.error(f"Unknown LLM: {chosen_llm}")
    return ""
