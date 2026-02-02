from dotenv import load_dotenv
load_dotenv()

import os
import requests
import streamlit as st
from langchain_openai import ChatOpenAI


# -----------------------------
# 1. 读取 API Key
# -----------------------------
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")


# -----------------------------
# 2. 初始化 LLM（用于翻译城市名）
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -----------------------------
# 3. 中文城市名 → 英文城市名（最稳的方式）
# -----------------------------
def normalize_city(city: str) -> str:
    """用 LLM 自动把中文城市名翻译成英文城市名"""
    prompt = f"把这个中文城市名翻译成英文城市名，只输出英文：{city}"
    result = llm.invoke(prompt).content
    return result.strip()


# -----------------------------
# 4. 调用 OpenWeather API
# -----------------------------
def get_weather(city: str) -> str:
    # 先把中文城市名翻译成英文
    city_en = normalize_city(city)

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_en}&appid={OPENWEATHER_KEY}&units=metric&lang=zh_cn"
    )

    resp = requests.get(url).json()

    if resp.get("cod") != 200:
        return f"无法获取 {city} 的天气：{resp.get('message', '未知错误')}"

    weather = resp["weather"][0]["description"]
    temp = resp["main"]["temp"]
    humidity = resp["main"]["humidity"]
    wind = resp["wind"]["speed"]

    return (
        f"{city} 当前天气：{weather}，"
        f"温度 {temp}°C，"
        f"湿度 {humidity}% ，"
        f"风速 {wind} m/s"
    )


# -----------------------------
# 5. Streamlit UI
# -----------------------------
st.title("OpenWeather 天气助手（最终稳定版）")

user_input = st.text_input("请输入城市，例如：上海 / 北京 / 广州 / 深圳")

if user_input:
    answer = get_weather(user_input)
    st.write(answer)
