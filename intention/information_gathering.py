import dataclasses

from .base_intention import Intention


@dataclasses.dataclass
class InformationGathering:
    name = "Information Gathering"
    question_prompt = "Print out current date."
