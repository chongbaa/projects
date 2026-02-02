from langchain_core.tools import tool

@tool
def get_clothing_advice(temp_celsius: float) -> str:
    if temp_celsius < 10:
        return "穿羽绒服和围巾吧，外面很冷！"
    elif temp_celsius < 20:
        return "穿外套或毛衣比较合适。"
    else:
        return "天气不错，穿轻便点就行。"
