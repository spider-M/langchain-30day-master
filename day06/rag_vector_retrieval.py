# -*- coding: utf-8 -*-
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    docs = [
        Document(page_content="LangChain是大模型应用框架"),
        Document(page_content="RAG让AI读取私有文档"),
        Document(page_content="向量库存储文本特征"),
        Document(page_content="检索找到最相关内容")
    ]
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    db = FAISS.from_documents(splits, embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 2})
    res = retriever.invoke("什么是RAG？")
    for doc in res:
        print(doc.page_content)

if __name__ == "__main__":
    main()