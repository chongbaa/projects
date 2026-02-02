# myapp/core/engine.py

from myapp.core.registry import discover_plugins, get_tool_plugins
import os


class DummyAgent:
    """
    最小可用 Agent，只用于验证系统结构
    """
    def __init__(self, tools):
        self.tools = tools

    def invoke(self, input, config=None):
        tool_names = [t.__name__ for t in self.tools]

        return {
            "messages": [
                type(
                    "Msg",
                    (),
                    {
                        "content": f"DummyAgent 收到问题：{input['messages'][-1][1]}\n"
                                   f"已加载 tools: {tool_names}"
                    },
                )()
            ]
        }


def build_agent():
    # 1. 找到 plugins 目录
    base = os.path.dirname(__file__)
    plugins_root = os.path.abspath(
        os.path.join(base, "..", "plugins")
    )

    # 2. 发现所有插件
    plugins = discover_plugins(plugins_root)

    # 3. 只保留 tool 插件
    tool_plugins = get_tool_plugins(plugins)

    # 4. 汇总 tools
    tools = []
    for p in tool_plugins:
        if hasattr(p.module, "tools"):
            tools.extend(p.module.tools)

    # 5. 创建 agent（真实存在！）
    agent = DummyAgent(tools)

    return agent
