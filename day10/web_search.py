# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv()

def main():
    search = TavilySearchResults(max_results=3)
    tools = [search]
    llm = ChatOpenAI(temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "使用搜索工具回答最新信息"),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}")
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    exe = AgentExecutor(agent=agent, tools=tools, verbose=True)
    res = exe.invoke({"input": "2026 人工智能发展趋势"})
    print(res["output"])

if __name__ == "__main__":
    main()