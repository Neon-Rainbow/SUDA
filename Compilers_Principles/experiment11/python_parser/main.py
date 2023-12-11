"""
这个模块提供了一系列用于表示和处理抽象语法树（AST）节点的类。AST是源代码的树状结构表示，用于语言解析和其他编译器相关任务。

主要类包括：
- Node：所有节点的基类，提供基本的节点功能。
- NonTerminal：用于表示非终结符的节点。
- LeftValue、Number、ID、Terminal：特殊类型的节点，分别用于表示左值、数字、标识符和其他终结符。

这些类支持构建和操作复杂的AST结构，适用于编译器的前端处理，如语法分析和语义分析。

使用示例：
    node = NonTerminal('expression')
    node.add(LeftValue('variable'))
    node.add(Number('42'))
"""
import sys
from time import sleep

import translation
from py_yacc import yacc

if len(sys.argv) != 2:
    print('不正确的用法', file=sys.stderr)
    exit(1)

try:
    with open(sys.argv[-1], 'r', encoding='utf-8') as file:
        text = file.read()
    # syntax parse
    root = yacc.parse(text)
    print("语法树：", root)
    if root is None:
        exit(0)
    # translation
    print('运行结果：')
    translation.translate(root)
    print("当前变量表：", translation.var_table)
except Exception as e:
    sys.stdout.flush()
    sleep(0.05)
    print(*e.args, file=sys.stderr)
    # raise e