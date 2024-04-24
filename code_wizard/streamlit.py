from typing import Set
import streamlit as st
from streamlit_chat import message
from code_wizard.core import run_llm


def create_sources_string(sources: Set[str]) -> str:
    if not sources:
        return ""

    sources_list = sorted(sources)
    return "Sources: \n" + "\n".join(
        f"{i+1}. {source}" for i, source in enumerate(sources_list)
    )


st.header("Code Wizard: Langchain Documentation Helper 🤖")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here...")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if prompt:
    with st.spinner("Generating Response..."):
        # print("Query: ", prompt)
        # print("Chat History: ", st.session_state["chat_history"])
        response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
        sources = set(
            doc.metadata.get("source") for doc in response.get("source_documents", [])
        )
        formatted_response = (
            f"{response.get('answer', '')} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, response.get("answer", "")))


if st.session_state["chat_answers_history"]:
    st.subheader("Chat History")
    for user_prompt, chat_answer in zip(
        st.session_state["user_prompt_history"],
        st.session_state["chat_answers_history"],
    ):
        message(user_prompt, is_user=True)
        message(chat_answer)
