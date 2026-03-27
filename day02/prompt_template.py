# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
import os

load_dotenv()

def main():
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="请把以下内容翻译成英文：\n{user_input}"
    )
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    parser = StrOutputParser()
    chain = prompt | llm | parser
    result = chain.invoke({"user_input": "LangChain是大模型应用开发框架"})
    print("翻译结果：", result)

if __name__ == "__main__":
    main()