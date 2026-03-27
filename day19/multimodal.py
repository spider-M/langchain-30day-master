# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

msg = HumanMessage(content=[
    {"type": "text", "text": "图片里有什么内容？"},
    {"type": "image_url", "image_url": {"url": "https://picsum.photos/300/200"}}
])

resp = llm.invoke([msg])
print(resp.content)