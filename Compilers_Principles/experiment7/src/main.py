"""
main.py: 包含化学分子式解析器的主函数和测试代码。

此模块定义了一个函数，该函数可以计算给定化学分子式中的元素数量。
同时，它包含了一些测试代码，以验证解析器的正确性。
"""

from .lexer import lexer
from .parser import parser


def atom_count(formula):
    """
    计算给定化学分子式中的元素数量。

    Args:
    formula (str): 待分析的化学分子式。

    Returns:
    int: 元素的数量。
    """
    lexer.input(formula)
    return parser.parse(lexer=lexer)


if __name__ == "__main__":
    print(atom_count("He"))  # 输出: 1
