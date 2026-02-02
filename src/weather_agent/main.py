import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver

# 加载 .env
load_dotenv()

# 工具：实时天气查询
@tool
def get_weather(city: str) -> str:
    """查询指定城市的实时天气"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "没有找到 API Key，请检查 .env 文件中的 OPENWEATHER_API_KEY"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=zh_cn&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"无法获取 {city} 的天气信息: {data.get('message', '未知错误')}"

        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{city} 当前天气：{desc}，气温 {temp}°C"

    except Exception as e:
        return f"查询 {city} 天气时出错: {str(e)}"

# 初始化 Agent
llm = ChatOpenAI(model="gpt-4o-mini")
memory = MemorySaver()

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="你是一个天气助手。",
    checkpointer=memory,
)

# -------------------------
# Streamlit Web UI
# -------------------------

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("⛅ Weather Agent")

city = st.text_input("City：")

if st.button("Query Weather"):
    if city.strip():
        result = agent.invoke(
            {"messages": [("user", f"{city}How is Weather today？")]},
            config={"configurable": {"thread_id": "webui"}}
        )
        st.success(result["messages"][-1].content)
    else:
        st.warning("Weather Query")
