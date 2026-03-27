# -*- coding: utf-8 -*-
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain import hub
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    return a + b

tools = [add]
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

executor.invoke({"input": "1+2+3 等于多少"})