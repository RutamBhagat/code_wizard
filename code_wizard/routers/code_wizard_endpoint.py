from typing import Set
from fastapi import APIRouter, status

from code_wizard.core import run_llm

from code_wizard.routers.utils.type_classes import Query_Request


router = APIRouter()


def create_sources_string(sources: Set[str]) -> str:
    if not sources:
        return ""

    sources_list = sorted(sources)
    return "Sources: \n" + "\n".join(
        f"{i+1}. {source}" for i, source in enumerate(sources_list)
    )


@router.post("/process", status_code=status.HTTP_201_CREATED)
def create_new_query(query_request: Query_Request):
    chat_history = query_request.chat_history
    formatted_chat_history = []

    for i in range(0, len(chat_history), 2):
        if i + 1 >= len(chat_history):
            formatted_chat_history.append((chat_history[i], ""))
        else:
            formatted_chat_history.append((chat_history[i], chat_history[i + 1]))

    response = run_llm(query=query_request.query, chat_history=formatted_chat_history)

    sources = set(
        doc.metadata.get("source") for doc in response.get("source_documents", [])
    )

    formatted_response = (
        f"{response.get('answer', '')} \\n\\n {create_sources_string(sources)}"
    )

    return formatted_response
