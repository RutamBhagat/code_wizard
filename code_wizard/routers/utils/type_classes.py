from pydantic import BaseModel, Field
from typing import List, Tuple


class Query_Request(BaseModel):
    query: str = Field(..., min_length=3, example="What is the weather?")
    chat_history: List[Tuple[str, str]]

    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is the weather?",
                "chat_history": [("System", "Hello, how can I help you?")],
            }
        }
