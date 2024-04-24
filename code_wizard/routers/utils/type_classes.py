from pydantic import BaseModel, Field
from typing import Any, List, Tuple


class Query_Request(BaseModel):
    query: str = Field(..., min_length=3, example="What is the Langchain?")
    chat_history: List[Any]

    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is the Langchain?",
                "chat_history": [("System", "Hello, how can I help you?")],
            }
        }
