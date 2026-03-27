# -*- coding: utf-8 -*-
import gradio as gr
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_fn(message, history):
    return llm.invoke(message).content

demo = gr.ChatInterface(chat_fn)

if __name__ == "__main__":
    demo.launch()