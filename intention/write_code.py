import dataclasses

from .base_intention import Intention


@dataclasses.dataclass
class WriteCode:
    name = "Write Code (quick sort)"
    question_prompt = "Please write a quick sort algorithm in python"
