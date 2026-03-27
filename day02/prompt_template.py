# 读取.env文件，加载密钥等环境变量
from dotenv import load_dotenv
# 提示词模板：定义固定的提问格式
from langchain_core.prompts import PromptTemplate
# 大模型调用工具：对接通义千问/GPT
from langchain_openai import ChatOpenAI
# 输出解析器：把模型返回结果转成纯文本
from langchain_core.output_parsers import StrOutputParser
# 系统库：读取环境变量
import os

# 加载 .env 文件中的配置
load_dotenv()

def main():
    # ==========================
    # 1. 创建提示词模板
    # ==========================
    prompt = PromptTemplate(
        # 模板里用到的变量名列表，必须和模板中的 {xxx} 对应
        input_variables=["user_input"],
        # 提示词模板内容：{user_input} 会被动态替换成用户输入
        template="请把以下内容翻译成英文：\n{user_input}"
    )

    # ==========================
    # 2. 创建大模型实例（核心！）
    # ==========================
    llm = ChatOpenAI(
        # 模型名称：通义千问最强版本
        model="qwen3-max",
        # API密钥：从.env文件读取，不能写在代码里
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # 通义千问的API接口地址（必须加，否则默认调用GPT）
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        # 温度参数：0=严谨，1=创意，0.7=平衡（最常用）
        temperature=0.7,
        # 关闭SSL证书验证，解决国内网络报错
    )

    # ==========================
    # 3. 创建输出解析器
    # ==========================
    parser = StrOutputParser()

    # ==========================
    # 4. 组装调用链（管道写法）
    # 顺序：提示词 → 模型 → 解析结果
    # ==========================
    chain = prompt | llm | parser

    # ==========================
    # 5. 执行链，传入参数
    # ==========================
    result = chain.invoke(
        # 给模板传值：key 必须和 input_variables 一致
        {"user_input": "LangChain是大模型应用开发框架"}
    )

    # 打印最终结果
    print("翻译结果：", result)

# 程序入口：只有直接运行这个文件时，才执行main函数
if __name__ == "__main__":
    main()