# Pair-wise GSB 基线：Thompson NFA 正则引擎

题目（0-1 代码生成）：实现正则表达式引擎（Thompson NFA 构造 + 匹配/搜索/查找全部）。

- 骨架：`regex.py`（compile/match/search/findall 均 `raise NotImplementedError`）
- 验收：`python -m pytest tests/test_regex.py -q` 全绿
- 约束：只 import 标准库；必须真实构造 NFA（禁止调 re，禁止暴力指数回溯）
