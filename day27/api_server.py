# -*- coding: utf-8 -*-
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/ask")
def ask_ai(q: str):
    ans = llm.invoke(q).content
    return {"question": q, "answer": ans}

# 启动命令：
# uvicorn day27.api_server:app --reload