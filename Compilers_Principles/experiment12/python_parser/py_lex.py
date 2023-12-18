# coding=utf-8
import sys

from ply import lex

# LEX for parsing Python

reserved_words = {
    'print': 'PRINT',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'len': 'LEN',
    'break': 'BREAK',
    'and': 'AND',
    'or': 'OR',
    'def': 'DEF',
    'return': 'RETURN',
}
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'ASSIGN',
          'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'DPLUS', 'DMINUS', 'ID', 'EDIVIDE', 'MINEQUAL', 'PLUSEQUAL',
          'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', ] + list(reserved_words.values())

# Define of tokens
t_PLUSEQUAL = r'\+='
t_MINEQUAL = r'-='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EDIVIDE = r'//'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ASSIGN = r'='
t_DPLUS = r'\+\+'
t_DMINUS = r'--'
t_COMMA = r','
t_SEMICOLON = r';'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='


# 识别 ID，首先检查是否为保留字print，若是则申明其类型，否则为 ID
def t_ID(t):
    r"""[A-Za-z_][A-Za-z0-9_]*"""
    t.type = reserved_words.get(t.value, 'ID')
    return t


# 识别新行，并将行号 + 1
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_NUMBER(t):
    r"""[0-9]+"""
    t.value = int(t.value)
    return t


# 忽略的字符
t_ignore = ' \t'


# 错误处理程序
def t_error(t):
    print("\nInvalid token '%s' at line %d" % (t.value[0], t.lexer.lineno), file=sys.stderr)
    t.lexer.skip(1)


lex.lex()
