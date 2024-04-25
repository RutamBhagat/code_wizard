import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from unstructured.chunking.title import chunk_by_title
from unstructured.partition.md import partition_md
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
from unstructured.staging.base import dict_to_elements
from consts import INDEX_NAME


load_dotenv()
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key, environment="northamerica-northeast1-gcp")


def docs_to_embeddings() -> None:
    current_dir = os.getcwd()
    docs_path = os.path.join(
        current_dir,
        "..",
        "langchain_docs",
    )

    loader = ReadTheDocsLoader(path=docs_path)
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Going to insert {len(documents)} Documents to Pinecone")

    openai_api_key = os.environ.get("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(
        openai_api_key=openai_api_key, disallowed_special=set()
    )

    docsearch = PineconeVectorStore.from_documents(
        documents=documents,
        embedding=embeddings,
        index_name=INDEX_NAME,
    )
    print("****** Added to Pinecone Vectorstore ******")


if __name__ == "__main__":
    docs_to_embeddings()
