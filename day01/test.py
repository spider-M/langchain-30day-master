# 加载python-dotenv库，作用是：读取项目根目录下的 .env 文件里的环境变量
from dotenv import load_dotenv

# 从langchain_openai库中导入ChatOpenAI类，作用是：调用大模型（通义千问/GPT）
from langchain_openai import ChatOpenAI

# 导入操作系统相关的库，用来读取环境变量
import os

# 执行加载操作：把 .env 文件中的变量加载到程序里
load_dotenv()

# 定义主函数，程序的核心逻辑都在这里面
def main():
    # 创建一个大模型客户端，配置模型名称、API密钥、随机性参数
    llm = ChatOpenAI(
        model="qwen3-max",          # 指定使用的模型：通义千问 qwen3-max
        api_key=os.getenv("OPENAI_API_KEY"),  # 从.env文件读取你的 API Key
        temperature=0.7,            # 温度值：0最严谨，1最有创意
    )

    # 调用大模型，发送问题："你好 你是谁，你能帮我做什么"
    response = llm.invoke("你好 你是谁，你能帮我做什么")

    # 打印模型返回的回答内容
    print("AI 回复：", response.content)

# Python固定写法：表示当这个文件被直接运行时，才执行下面的代码
if __name__ == '__main__':
    main()  # 调用上面定义的 main 函数，启动程序