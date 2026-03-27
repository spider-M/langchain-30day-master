# -*- coding: utf-8 -*-
import sqlite3
from langchain.tools import tool

@tool
def sql_query(sql: str) -> str:
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    try:
        c.execute(sql)
        return str(c.fetchall())
    except Exception as e:
        return str(e)
    finally:
        conn.close()

if __name__ == "__main__":
    print(sql_query.invoke("SELECT name FROM sqlite_master WHERE type='table'"))