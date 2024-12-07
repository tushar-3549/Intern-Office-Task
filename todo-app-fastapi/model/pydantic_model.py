from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    root: str
    synonyms: List[str]