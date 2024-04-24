from pydantic import BaseModel, Field
from typing import Any, List, Tuple


class Query_Request(BaseModel):
    query: str = Field(..., min_length=3, example="What is LCEL")
    chat_history: List[str] = Field(
        ...,
        example=[
            "What is the Langchain?",
            "Langchain is a conversational AI platform.",
        ],
    )

    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is LCEL",
                "chat_history": [
                    "What is the Langchain?",
                    "Langchain is a conversational AI platform.",
                ],
            }
        }
