# -*- coding: utf-8 -*-
# 文件编码声明，确保中文可以正常显示

# 读取 .env 环境变量文件（用于安全加载 API Key）
from dotenv import load_dotenv

# 对接大模型（通义千问 / GPT 都用这个类）
from langchain_openai import ChatOpenAI

# 内存版聊天历史记录存储（用于保存对话上下文）
from langchain_core.chat_history import InMemoryChatMessageHistory

# 给链添加记忆能力的核心类
from langchain_core.runnables.history import RunnableWithMessageHistory

# 聊天提示词模板 + 历史消息占位符
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 导入类型定义，用于消除 PyCharm 黄色警告
from langchain_core.runnables import Runnable, RunnableConfig

# 类型注解工具（Dict 表示字典）
from typing import Dict

# 系统库，用于读取环境变量
import os

# ===================== 加载环境变量 =====================
# 从 .env 文件读取 DASHSCOPE_API_KEY 等配置
load_dotenv()

# ===================== 主函数 =====================
def main() -> None:
    """
    主函数：实现带记忆功能的 AI 对话
    功能：AI 能记住你之前说过的话
    """

    # 1. 初始化大模型（通义千问 qwen3-max）
    llm: ChatOpenAI = ChatOpenAI(
        model="qwen3-max",                                  # 使用的模型名称
        api_key=os.getenv("DASHSCOPE_API_KEY"),            # 从环境变量获取通义千问密钥
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 通义千问接口地址
        temperature=0.7,                                   # 回答风格：0 严谨 / 1 创意
    )

    # 2. 定义提示词模板
    # MessagesPlaceholder 用于自动插入历史聊天记录
    prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
        ("system", "你是一个友好的AI助手，会记住之前的对话内容。"),  # 系统提示词
        MessagesPlaceholder(variable_name="history"),       # 历史消息占位符（必须有）
        ("human", "{input}")                                # 用户输入的位置
    ])

    # 3. 构建基础链：提示词 → 大模型
    runnable: Runnable = prompt | llm

    # 4. 内存会话存储：用字典保存每个用户的聊天历史
    store: Dict[str, InMemoryChatMessageHistory] = {}

    def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        """
        根据 session_id 获取对应用户的聊天历史
        如果没有则自动创建一个新的
        """
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    # 5. 给基础链添加记忆能力
    with_memory: RunnableWithMessageHistory = RunnableWithMessageHistory(
        runnable,                                          # 基础链
        get_session_history,                               # 历史记录获取函数
        input_messages_key="input",                       # 用户输入的键名
        history_messages_key="history"                     # 历史消息的键名
    )

    # ===================== 开始对话 =====================

    # 配置：指定用户会话 ID（同一个 ID 会共享记忆）
    config: RunnableConfig = {"configurable": {"session_id": "user_123"}}

    # 6. 第一次对话：告诉 AI 名字和职业
    res1 = with_memory.invoke(
        {"input": "你好，我叫张三，是程序员"},
        config=config
    )
    print("AI 回复 1：", res1.content)

    # 7. 第二次对话：测试 AI 是否记得之前的信息
    res2 = with_memory.invoke(
        {"input": "我叫什么？做什么工作？"},
        config=config
    )
    print("AI 回复 2：", res2.content)

# ===================== 程序入口 =====================
if __name__ == "__main__":
    main()