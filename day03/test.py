import os
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable, RunnableConfig
from typing import Dict


def main():
    llm: ChatOpenAI = ChatOpenAI(
        model="qwen3-max",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )

    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
        ("system", "你是一个友好的AI助手，会记住之前的对话内容。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    runnable: Runnable = prompt | llm
    store: Dict[str, InMemoryChatMessageHistory] = {}

    def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    with_menory: RunnableWithMessageHistory = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="input",
        history_messages_key='history',
    )

    config: RunnableConfig = {"configurable": {"session_id": "user_123"}}

    res1 = with_menory.invoke(
        {"input": "你好，我是张三，是程序员"},
        config=config
    )
    print("AI 回复 1：", res1.content)
    res2 = with_menory.invoke(
        {"input": "我叫什么？做什么工作"},
        config=config
    )
    print("AI 回复 2：", res2.content)


if __name__ == '__main__':
    main()
