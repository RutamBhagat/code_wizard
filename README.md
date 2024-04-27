# Code Wizard: LangChain Documentation AI Chatbot

Code Wizard is a super cool AI chatbot that helps you learn and use the LangChain Documentation in an interactive way. Just ask it anything about LangChain concepts or code, and it'll break it down for you in an easy-to-understand way. Built with Next.js, FastAPI, LangChain, and a local LLaMA model.

**Link to project:** https://code-wizard-frontend.vercel.app/

![Code Wizard Screenshot](https://i.imgur.com/abcdefg.png)

## How It's Made

**Tech used:** LangChain, LLaMA, Next.js, Typescript, FastAPI

Code Wizard is a full-stack app that combines some cutting edge tech. The front-end is built with Next.js and React, which makes it fast and snappy. The back-end uses FastAPI to host the LangChain pipelines and APIs.

The core is powered by LangChain, which lets us build cool applications with large language models like LLaMA. Code Wizard takes the LangChain documentation, chunks it up, and stores it in a vector database using embeddings.

When you ask Code Wizard a question, it uses LangChain agents to search the vector database for relevant doc chunks. It then generates a response by combining those chunks with the LLaMA 3.

The front-end has a slick chat interface built with React, so you can have natural conversations with the AI. It also renders Markdown and code snippets nicely.

## Optimizations

To make Code Wizard performant and scalable, it uses some cool optimizations:

1. **Caching**: Frequently asked questions and their responses are cached to improve latency.
2. **Async Processing**: The LangChain pipelines run asynchronously to handle multiple requests concurrently.
3. **Model Optimization**: The LLaMA model is optimized for efficient CPU inference, allowing Code Wizard to run on modest hardware.

## Lessons Learned

Building Code Wizard was an incredible learning experience that taught me so much about LangChain, large language models, and modern web development. Some key lessons:

- How to effectively integrate LangChain components like agents, memory, and vector stores.
- Optimizing LLM performance through techniques like quantization and CPU offloading.
- Designing intuitive conversational UIs that feel natural and engaging.
- Leveraging the latest web frameworks like Next.js and FastAPI for building scalable apps.

## Examples

Check out these example conversations with Code Wizard:

**Understanding Retrieval Augmented Generation (RAG):**
[https://code-wizard.app/chat/rag-overview](https://code-wizard.app/chat/rag-overview)

**Building a Question-Answering Chatbot:**
[https://code-wizard.app/chat/qa-chatbot](https://code-wizard.app/chat/qa-chatbot)

**Explaining LangChain's Memory Concepts:**
[https://code-wizard.app/chat/memory-in-langchain](https://code-wizard.app/chat/memory-in-langchain)
