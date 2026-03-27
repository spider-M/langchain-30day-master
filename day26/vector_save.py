# -*- coding: utf-8 -*-
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

# 保存
db = FAISS.from_texts(["LangChain 实战课程"], embeddings)
db.save_local("faiss_index")

# 加载
db2 = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

print(db2.similarity_search("课程")[0].page_content)