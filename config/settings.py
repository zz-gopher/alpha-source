import os
from pathlib import Path

# 加载项目根目录的 .env
_env_file = Path(__file__).resolve().parent.parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _key, _, _value = _line.partition("=")
            os.environ.setdefault(_key.strip(), _value.strip())

# Github 配置
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# 过滤黑名单
BLACKLIST_WORDS = ['awesome', 'tutorial', 'interview', 'roadmap', 'book', 'course']

# 极简配置
TOP_K = 5

# 数据库路径
DB_PATH = "alpha_source.db"