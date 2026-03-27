from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    response = llm.invoke("你好，我正在学习 LangChain")
    print("AI 回复：", response.content)

if __name__ == "__main__":
    main()