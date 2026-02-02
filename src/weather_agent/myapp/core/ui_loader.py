# myapp/core/ui_loader.py

import importlib
import os
import yaml


def load_ui():
    """
    找到 enabled 的 UI 插件，返回它的入口函数
    """
    base_dir = os.path.dirname(__file__)
    ui_root = os.path.abspath(
        os.path.join(base_dir, "..", "ui_plugins")
    )

    for name in os.listdir(ui_root):
        plugin_dir = os.path.join(ui_root, name)
        yaml_path = os.path.join(plugin_dir, "plugin.yaml")

        if not os.path.isfile(yaml_path):
            continue

        with open(yaml_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        if not cfg.get("enabled"):
            continue

        module = importlib.import_module(
            f"myapp.ui_plugins.{name}.plugin"
        )

        return getattr(module, cfg["entry"])

    raise RuntimeError("没有启用的 UI 插件")
