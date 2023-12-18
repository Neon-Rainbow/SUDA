import sys
from time import sleep

from translation import Translator
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
    print('该python文件运行结果：')
    tran = Translator(root)
    tran.translate()
    print(f"变量表中存放的内容:{tran.var_table}")
except Exception as e:
    sys.stdout.flush()
    sleep(0.05)
    print(*e.args, file=sys.stderr)
    raise e
