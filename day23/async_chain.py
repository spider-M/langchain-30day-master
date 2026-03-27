# -*- coding: utf-8 -*-
import asyncio
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def main():
    task1 = llm.ainvoke("写一句早安问候")
    task2 = llm.ainvoke("写一句晚安问候")
    r1, r2 = await asyncio.gather(task1, task2)
    print(r1.content)
    print(r2.content)

asyncio.run(main())