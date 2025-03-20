@echo off
set SCRIPT_PATH=%~dp0
set VENV_PATH=%SCRIPT_PATH%.venv\Scripts

if exist "%VENV_PATH%\python.exe" (
    "%VENV_PATH%\python.exe" -m md2html %*
) else (
    echo 错误：未找到虚拟环境，请先运行 uv venv 创建虚拟环境
    exit /b 1
) 