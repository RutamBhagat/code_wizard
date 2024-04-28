import os
from typing import Any, List, Tuple
from dotenv import load_dotenv
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from code_wizard.consts import INDEX_NAME

load_dotenv()
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key, environment="northamerica-northeast1-gcp")


def run_llm(query: str, chat_history: List[Tuple[str, str]] = []) -> str:
    print("Query: ", query)
    print("Chat History: ", chat_history)
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(
        openai_api_key=openai_api_key, disallowed_special=set()
    )

    docsearch = PineconeVectorStore.from_existing_index(
        index_name=INDEX_NAME, embedding=embeddings
    )

    chat = ChatOpenAI(
        openai_api_key=openai_api_key,
        verbose=True,
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat,
        chain_type="refine",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )

    return qa.invoke({"question": query, "chat_history": chat_history})


if __name__ == "__main__":
    query = "What is Retrieval QA chain?"
    response = run_llm(query)
    print(response)
