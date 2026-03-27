# -*- coding: utf-8 -*-
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
db = FAISS.from_texts([
    "RAG 是检索增强生成",
    "rerank 用于优化检索结果",
    "向量库存储文本向量"
], embeddings)

base_retriever = db.as_retriever()
compressor = LLMChainExtractor.from_llm(ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY")))
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

docs = retriever.invoke("什么是 RAG？")
for d in docs:
    print(d.page_content)