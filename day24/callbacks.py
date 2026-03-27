# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain.callbacks import StdOutCallbackHandler
import os
from dotenv import load_dotenv

load_dotenv()

handler = StdOutCallbackHandler()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), callbacks=[handler])
llm.invoke("你好，简单介绍自己")