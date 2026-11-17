# sources/base_source.py
from typing import List, Dict


class BaseSource:
    def fetch_raw_data(self) -> List[Dict]:
        """抓取原始数据，必须由子类实现"""
        raise NotImplementedError

    @property
    def source_name(self) -> str:
        raise NotImplementedError