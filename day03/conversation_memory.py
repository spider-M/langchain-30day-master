# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

load_dotenv()

def main():
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory, verbose=False)

    print(chain.run("你好，我叫张三，是程序员"))
    print(chain.run("我叫什么？做什么工作？"))

if __name__ == "__main__":
    main()