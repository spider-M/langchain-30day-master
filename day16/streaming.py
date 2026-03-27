# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), streaming=True)

for chunk in llm.stream("用 100 字介绍 LangChain"):
    print(chunk.content, end="", flush=True)

print()