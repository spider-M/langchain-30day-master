# -*- coding: utf-8 -*-
from langchain_community.llms import Tongyi
import os

os.environ["DASHSCOPE_API_KEY"] = "你的通义千问 KEY"
llm = Tongyi(model="qwen-turbo")
print(llm.invoke("你好"))