# -*- coding: utf-8 -*-
import requests
from langchain.tools import tool

@tool
def erp_order_query(order_id: str, token: str = "test-token-123") -> str:
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://erp.example.com/api/order/{order_id}"
    try:
        resp = requests.get(url, headers=headers, timeout=8)
        return resp.text
    except Exception as e:
        return f"请求失败：{str(e)}"

if __name__ == "__main__":
    print(erp_order_query.invoke("123456"))