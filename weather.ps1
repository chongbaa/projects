# 激活虚拟环境
$venvPath = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    & $venvPath
} else {
    Write-Host "虚拟环境不存在，请先创建 .venv" -ForegroundColor Red
    exit
}

# 启动 Streamlit 应用
streamlit run .\src\weather_agent\main.py
