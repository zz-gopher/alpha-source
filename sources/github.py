# sources/github.py
import requests
from datetime import datetime, timedelta
from typing import List, Dict
from config import settings
from sources.base_source import BaseSource


class GitHubSource(BaseSource):
    @property
    def source_name(self) -> str:
        return "GitHub"

    def fetch_raw_data(self) -> List[Dict]:
        """按特定规则（如过去30天高Star）抓取 GitHub 数据"""
        date_threshold = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        query = f"created:>{date_threshold} stars:>100"
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=20"

        headers = {"Accept": "application/vnd.github.v3+json"}
        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"token {settings.GITHUB_TOKEN}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"[{self.source_name}] API 请求失败: {response.status_code}")
            return []

        items = response.json().get('items', [])

        # 统一格式化输出，只提取我们需要的数据，降低其他模块耦合
        formatted_data = []
        for item in items:
            formatted_data.append({
                "id": item['full_name'],  # 作为唯一标识
                "name": item['name'],
                "full_name": item['full_name'],
                "description": item['description'] or "",
                "url": item['html_url'],
                "stars": item['stargazers_count'],
                "language": item['language'] or "Unknown",
                "source": self.source_name
            })
        return formatted_data