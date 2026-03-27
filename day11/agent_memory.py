# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
import os

load_dotenv()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

@tool
def weather(city: str) -> str:
    return f"{city}：晴，25℃"

tools = [weather]

def main():
    llm = ChatOpenAI(temperature=0)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "结合历史对话使用工具"),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}")
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    exe = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
    exe.invoke({"input": "我现在在上海"})
    res = exe.invoke({"input": "今天天气怎么样"})
    print(res["output"])

if __name__ == "__main__":
    main()