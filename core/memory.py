import sqlite3
from datetime import datetime
from config import settings

class MemoryDB:
    def __init__(self):
        self.conn = sqlite3.connect(settings.DB_PATH)
        self._init_tables()

    def _init_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scanned_repos (
                repo_id TEXT PRIMARY KEY,
                url TEXT,
                stars INTEGER,
                scanned_at DATE
            )
        ''')
        self.conn.commit()

    def is_scanned(self, repo_id: str) -> bool:
        """检查项目是否已经被记录过"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM scanned_repos WHERE repo_id = ?", (repo_id,))
        return cursor.fetchone() is not None

    def mark_scanned(self, repo_id: str, url: str, stars: int):
        """将项目标记为已扫描"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO scanned_repos (repo_id, url, stars, scanned_at) VALUES (?, ?, ?, ?)",
            (repo_id, url, stars, datetime.now().date())
        )
        self.conn.commit()