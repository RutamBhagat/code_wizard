import os

from langchain_community.document_loaders import ReadTheDocsLoader

if __name__ == "__main__":
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
    print(docs_path)
    # loader = ReadTheDocsLoader(docs_path)
