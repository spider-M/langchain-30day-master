# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import StructuredTool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate

load_dotenv()

def add(a: int, b: int):
    return a + b

def mul(a: int, b: int):
    return a * b

tools = [
    StructuredTool.from_function(add),
    StructuredTool.from_function(mul)
]

def main():
    llm = ChatOpenAI(temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是工具助手"),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}")
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    exe = AgentExecutor(agent=agent, tools=tools, verbose=True)
    print(exe.invoke({"input": "3+5*2 等于多少"}))

if __name__ == "__main__":
    main()