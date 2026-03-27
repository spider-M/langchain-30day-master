# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader

load_dotenv()

def create_knowledge_bot(file_path):
    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    splits = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    db = FAISS.from_documents(splits, embeddings)

    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        return_source_documents=False
    )
    return qa_chain

if __name__ == "__main__":
    bot = create_knowledge_bot("knowledge.txt")
    print("企业知识库助手已启动（输入 exit 退出）")
    while True:
        q = input("Q：")
        if q.lower() == "exit":
            break
        ans = bot.invoke({"query": q})
        print("A：", ans["result"])