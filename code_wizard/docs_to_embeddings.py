import os
import pinecone
from langchain_pinecone import Pinecone as PineconeLangChain
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI, OpenAIEmbeddings

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pc = pinecone.Pinecone(
    api_key=pinecone_api_key, environment="northamerica-northeast1-gcp"
)


def docs_to_embeddings() -> None:
    current_dir = os.path.dirname(__file__)
    docs_path = os.path.join(
        current_dir,
        "..",
        "langchain_docs",
        "langchain-docs",
        "api.python.langchain.com",
        "en",
        "latest",
    )

    loader = ReadTheDocsLoader(path=docs_path)
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs/", "https://")
        doc.metadata.update({"source": new_url})
    print(f"Going to insert {len(documents)} to Pinecone")

    openai_api_key = os.environ.get("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    docsearch = PineconeLangChain.from_documents(
        documents=documents,
        embedding=embeddings,
        index_name="langchain-doc-index",
    )
    print("****** Added to Pinecone Vectorstore ******")


if __name__ == "__main__":
    docs_to_embeddings()
