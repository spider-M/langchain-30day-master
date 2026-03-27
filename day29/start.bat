@echo off
echo 正在启动 LangChain API 服务...
uvicorn day27.api_server:app --host 0.0.0.0 --port 8000
pause