"""
test_parser.py: 包含对 main 模块中 atom_count 函数的测试用例。

此模块包含了对 atom_count 函数的多个单元测试,确保 atom_count 函数在各种输入条件下都能正确工作。

Usage:
    python3 -m pytest  # 从项目根目录运行所有测试
"""

import pytest
from src.main import atom_count


@pytest.mark.parametrize(
    "formula, expected", [
        ("He", 1),
        ("H2", 2),
        ("H2SO4", 7),
        ("CH3COOH", 8),
        ("NaCl", 2),
        ("C60H60", 120),
    ]
)
def test_molecule(formula, expected):
    assert atom_count(formula) == expected
