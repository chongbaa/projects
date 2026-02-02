# myapp/core/registry.py

from dataclasses import dataclass
from typing import Callable, Optional, List
import importlib
import os
import yaml


# -------------------------
# 插件的统一抽象
# -------------------------
@dataclass
class Plugin:
    name: str                 # 插件名
    type: str                 # "tool" / "ui"
    module: object            # plugin.py 模块对象
    entry: Optional[Callable] # UI 插件入口函数（tool 插件可为 None）
    config: dict              # plugin.yaml 的完整配置


# -------------------------
# 插件发现（核心）
# -------------------------
def discover_plugins(*roots: str) -> List[Plugin]:
    """
    扫描多个插件目录，发现并加载插件元信息
    """
    plugins: List[Plugin] = []

    for root in roots:
        if not os.path.isdir(root):
            continue

        for name in os.listdir(root):
            plugin_dir = os.path.join(root, name)
            yaml_path = os.path.join(plugin_dir, "plugin.yaml")

            if not os.path.isfile(yaml_path):
                continue

            # 读取 plugin.yaml
            with open(yaml_path, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f) or {}

            # 是否启用
            if not cfg.get("enabled", False):
                continue

            plugin_type = cfg.get("type")
            if not plugin_type:
                raise RuntimeError(f"插件 {name} 缺少 type 字段")

            # 计算模块导入路径
            # 例如：myapp.plugins.weather.plugin
            module_path = cfg.get(
                "module",
                f"{_path_to_module(root)}.{name}.plugin"
            )

            module = importlib.import_module(module_path)

            # entry 只对 UI 插件有意义
            entry = None
            if "entry" in cfg:
                entry = getattr(module, cfg["entry"])

            plugins.append(
                Plugin(
                    name=cfg.get("name", name),
                    type=plugin_type,
                    module=module,
                    entry=entry,
                    config=cfg,
                )
            )

    return plugins


def _path_to_module(path: str) -> str:
    """
    把文件系统路径转换为 Python 模块路径
    """
    path = os.path.abspath(path)
    parts = []

    while True:
        path, tail = os.path.split(path)
        if not tail:
            break
        parts.append(tail)
        if os.path.isfile(os.path.join(path, "__init__.py")):
            continue
        else:
            break

    return ".".join(reversed(parts))


# -------------------------
# 插件选择器（非常重要）
# -------------------------
def get_ui_plugin(plugins: List[Plugin]) -> Plugin:
    """
    返回第一个 UI 插件（只允许一个）
    """
    for p in plugins:
        if p.type == "ui":
            return p
    raise RuntimeError("没有启用的 UI 插件")


def get_tool_plugins(plugins: List[Plugin]) -> List[Plugin]:
    """
    返回所有 tool 插件
    """
    return [p for p in plugins if p.type == "tool"]
