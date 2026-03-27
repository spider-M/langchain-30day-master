# -*- coding: utf-8 -*-
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是专业技术顾问"),
    ("user", "{question}")
])

chain = prompt | ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY")) | StrOutputParser()

if __name__ == "__main__":
    print(chain.invoke({"question": "什么是 LCEL？"}))