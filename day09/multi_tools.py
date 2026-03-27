# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
import os

load_dotenv()

@tool
def user_info(user_id: str) -> str:
    return f"用户{user_id}：张三，25岁"

@tool
def order_info(order_id: str) -> str:
    return f"订单{order_id}：已发货"

tools = [user_info, order_info]

def main():
    llm = ChatOpenAI(temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "使用工具回答，不许编造"),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}")
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    exe = AgentExecutor(agent=agent, tools=tools, verbose=True)
    print(exe.invoke({"input": "查一下订单 6688"}))

if __name__ == "__main__":
    main()