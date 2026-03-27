# -*- coding: utf-8 -*-
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

agent_analyst = ChatPromptTemplate.from_messages([
    ("system", "你是行业分析师，简短分析"),
    ("user", "{input}")
]) | llm

agent_summarizer = ChatPromptTemplate.from_messages([
    ("system", "你是总结专家，提炼 3 句话"),
    ("user", "{input}")
]) | llm

if __name__ == "__main__":
    res = agent_analyst.invoke({"input": "AI 大模型未来发展"})
    final = agent_summarizer.invoke({"input": res.content})
    print(final.content)