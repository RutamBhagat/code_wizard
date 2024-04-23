import os

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
