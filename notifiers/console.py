# notifiers/console.py
from datetime import datetime


from notifiers.base_notifier import BaseNotifier
from config import settings


class ConsoleNotifier(BaseNotifier):
    def push(self, items: List[Dict]):
        if not items:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 今日无符合条件的高价值新项目。")
            return

        print(f"\n📅 今日 AlphaSource 速递 (Top {len(items)}):")
        print("-" * 50)

        for idx, item in enumerate(items, 1):
            rank_icon = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else "✨"
            print(f"{rank_icon} 【{item['full_name']}】 | 🌟 {item['stars']} | 🏷️ {item['language']}")
            print(f"🔗 {item['url']}")
            print(f"💡 {item['description']}\n")