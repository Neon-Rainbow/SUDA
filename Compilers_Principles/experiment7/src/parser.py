"""
parser.py: 包含化学分子式解析器的语法分析器组件。

此模块定义了一个语法分析器，用于解析化学分子式并计算其中的原子数量。

Classes:
    Atom: 表示化学分子式中的一个原子，包括元素符号和数量。

Functions:
    p_species_list_multiple(p): 处理多个化学物种的情况。
    p_species_list_single(p): 处理单个化学物种的情况。
    p_species_symbol(p): 处理单个符号的情况。
    p_species_symbol_count(p): 处理符号和数量的情况。
    p_error(p): 语法错误处理函数。
"""

import ply.yacc as yacc
from .lexer import tokens

class Atom:
    """表示化学分子式中的一个原子.

    Attributes:
        symbol (str): 元素的符号.
        count (int): 元素的数量.
    """

    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = count

    def __repr__(self):
        return f"Atom({self.symbol}, {self.count})"

def p_species_list(p):
    """
    species_list : species_list species
                    | species
    """
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_species(p):
    """
    species : SYMBOL
               | SYMBOL COUNT
    """
    if len(p) == 3:
        p[0] = int(p[2])
    else:
        p[0] = 1


def p_error(p):
    print(f"Syntax error at {p.value}")


parser = yacc.yacc()
