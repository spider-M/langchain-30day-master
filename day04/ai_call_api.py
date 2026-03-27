# -*- coding: utf-8 -*-
import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import StructuredTool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate

load_dotenv()

def get_city_weather(city_name: str) -> str:
    """查询城市天气"""
    try:
        url = f"https://api.pearktrue.cn/api/weather/?city={city_name}"
        resp = requests.get(url, timeout=10)
        return str(resp.json())
    except Exception as e:
        return f"失败：{str(e)}"

weather_tool = StructuredTool.from_function(get_city_weather)
tools = [weather_tool]

def main():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是智能助手"),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}")
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    res = executor.invoke({"input": "北京天气如何？"})
    print("\n最终回答：", res["output"])

if __name__ == "__main__":
    main()