#! /usr/bin/env python
# coding=utf-8
from parser.py_yacc import yacc
from utils.text_utils import clear_text
from utils.data_translator import trans, v_table

if __name__ == "__main__":
    text = clear_text(open('data/example.py', 'r').read())

    # syntax parse
    root = yacc.parse(text)
    root.print_node(0)

    # translation
    trans(root)
    print(v_table)
