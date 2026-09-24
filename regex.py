"""正则表达式引擎（Thompson NFA 构造 + 匹配/搜索/查找全部）。

语法（parse -> AST）：
- 字面量字符与转义 \. \* \\ \d（数字）
- 字符类 [abc] / [a-z] / [^abc]（否定）
- 或 a|b；分组 (expr)；重复 a* a+ a?（贪婪）
- 锚定 ^ $（仅在模式开头/结尾）

接口：
- compile(pattern) -> NFA（内部对象，含状态图）
- match(pattern, text) -> bool：全串匹配
- search(pattern, text) -> (start, end) | None：第一个匹配（贪婪最长）
- findall(pattern, text) -> [(start, end)...]：全部非重叠匹配

错误：非法模式 -> RegexError。
"""
from __future__ import annotations


class RegexError(Exception):
    pass


class NFA:
    """Thompson NFA：states[i] = {"eps": [...], "edges": [(pred, to)],
    "accept": bool}。"""

    def __init__(self):
        self.states: list[dict] = []
        self.start: int = 0
        self.anchor_start = False
        self.anchor_end = False


def compile(pattern: str) -> NFA:
    """解析 pattern 为 AST，Thompson 构造 NFA。非法模式抛 RegexError。"""
    raise NotImplementedError


def match(pattern: str, text: str) -> bool:
    """全串匹配（text 必须整个被 pattern 消费）。"""
    raise NotImplementedError


def search(pattern: str, text: str):
    """返回第一个匹配的 (start, end)（贪婪最长），无匹配返回 None。"""
    raise NotImplementedError


def findall(pattern: str, text: str) -> list:
    """返回全部非重叠匹配 [(start, end)...]。"""
    raise NotImplementedError
