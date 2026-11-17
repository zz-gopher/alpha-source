import os

# Github 配置
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# 过滤黑名单
BLACKLIST_WORDS = ['awesome', 'tutorial', 'interview', 'roadmap', 'book', 'course']

# 极简配置
TOP_K = 5

# 数据库路径
DB_PATH = "alpha_source.db"