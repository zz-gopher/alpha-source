# main.py
from sources.github import GitHubSource
from notifiers.console import ConsoleNotifier
from core.engine import AlphaEngine
from datetime import datetime

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 启动 AlphaSource 引擎...")

    # 初始化模块
    github_source = GitHubSource()
    console_notifier = ConsoleNotifier()

    # 组装流水线
    engine = AlphaEngine(
        sources=[github_source],
        notifiers=[console_notifier]
    )

    # 运行
    engine.run()