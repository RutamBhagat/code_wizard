from time import perf_counter
from fastapi import APIRouter, status

from code_wizard.core import run_llm
from code_wizard.routers.utils.type_classes import Query_Request

router = APIRouter()


@router.post("/process", status_code=status.HTTP_201_CREATED)
def create_new_query(query_request: Query_Request):
    start_time = perf_counter()
    chat_history = query_request.chat_history
    formatted_chat_history = []

    for i in range(0, len(chat_history), 2):
        if i + 1 >= len(chat_history):
            formatted_chat_history.append((chat_history[i], ""))
        else:
            formatted_chat_history.append((chat_history[i], chat_history[i + 1]))

    response = run_llm(query=query_request.query, chat_history=formatted_chat_history)

    end_time = perf_counter()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time:.4f} seconds")
    return response.get('answer', '')
