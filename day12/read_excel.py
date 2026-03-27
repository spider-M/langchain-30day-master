# -*- coding: utf-8 -*-
import pandas as pd
from langchain.tools import StructuredTool

def read_excel(file_path: str) -> str:
    df = pd.read_excel(file_path)
    return df.to_string()

tool_excel = StructuredTool.from_function(read_excel)

if __name__ == "__main__":
    print(read_excel("test.xlsx"))