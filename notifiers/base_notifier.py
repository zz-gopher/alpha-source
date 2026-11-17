# notifiers/base_notifier.py
from typing import List, Dict

class BaseNotifier:
    def push(self, items: List[Dict]):
        """执行推送逻辑，必须由子类实现"""
        raise NotImplementedError