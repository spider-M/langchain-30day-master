# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain.pydantic_v1 import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()

class UserInfo(BaseModel):
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY")).with_structured_output(UserInfo)
result = llm.invoke("张三，今年 25 岁，程序员")
print(result)