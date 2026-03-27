import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()


def main():
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="请说出你的作用：\n{user_input}"
    )

    llm = ChatOpenAI(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature = 0.7,
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    result = chain.invoke(
        {"user_input":"你能为我做什么"}
    )
    print("AI回复", result)

if __name__ == '__main__':
    main()









