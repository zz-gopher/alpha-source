# core/engine.py
from typing import List
from sources.base_source import BaseSource
from notifiers.base_notifier import BaseNotifier
from core.memory import MemoryDB
from config import settings


class AlphaEngine:
    def __init__(self, sources: List[BaseSource], notifiers: List[BaseNotifier]):
        self.sources = sources
        self.notifiers = notifiers
        self.memory = MemoryDB()

    def _filter_and_dedup(self, raw_items: List[dict]) -> List[dict]:
        """执行初筛与去重逻辑"""
        valid_items = []
        for item in raw_items:
            # 1. 过滤黑名单词汇
            text_to_check = f"{item['name']} {item['description']}".lower()
            if any(word in text_to_check for word in settings.BLACKLIST_WORDS):
                continue

            # 2. 本地查重
            if self.memory.is_scanned(item['id']):
                continue

            valid_items.append(item)

        return valid_items

    def run(self):
        """执行流水线主循环"""
        all_candidates = []

        # 1. 遍历所有数据源抓取数据
        for source in self.sources:
            raw_data = source.fetch_raw_data()
            all_candidates.extend(raw_data)

        # 2. 本地过滤与去重
        filtered_candidates = self._filter_and_dedup(all_candidates)

        # 3. 截取 Top K (在接入 LLM 后，这里将替换为 LLM 打分排序)
        final_targets = filtered_candidates[:settings.TOP_K]

        # 4. 推送到终端
        for notifier in self.notifiers:
            notifier.push(final_targets)

        # 5. 记录已推送项目，更新记忆库
        for target in final_targets:
            self.memory.mark_scanned(target['id'], target['url'], target['stars'])