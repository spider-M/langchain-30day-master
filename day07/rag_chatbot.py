# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader

load_dotenv()

def main():
    loader = TextLoader("knowledge.txt", encoding="utf-8")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    db = FAISS.from_documents(splits, embeddings)
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever()
    )
    q = input("请输入问题：")
    print(qa.invoke({"query": q})["result"])

if __name__ == "__main__":
    main()