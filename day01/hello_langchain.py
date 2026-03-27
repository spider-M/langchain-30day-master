
from langchain_openai import ChatOpenAI
import os



def main():
    llm = ChatOpenAI(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    response = llm.invoke("你好，我正在学习 LangChain")
    print("AI 回复：", response.content)

if __name__ == "__main__":
    main()