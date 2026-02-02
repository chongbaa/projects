# myapp/ui_plugins/streamlit_ui/plugin.py

def run_ui(agent_factory):
    """
    UI 插件统一入口

    agent_factory: 传进来的函数（比如 build_agent）
    """
    import streamlit as st

    st.set_page_config(page_title="Weather Agent")
    st.title("Weather Agent · UI Plugin")

    query = st.text_input("请输入你的问题")

    if st.button("发送"):
        if not query.strip():
            st.warning("请输入内容")
            return

        # 🔥 关键点：UI 不知道 agent 内部
        agent = agent_factory()

        result = agent.invoke(
            {"messages": [("user", query)]},
            config={"configurable": {"thread_id": "ui"}}
        )

        st.success(result["messages"][-1].content)
