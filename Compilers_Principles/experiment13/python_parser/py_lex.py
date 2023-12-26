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
    'class': 'CLASS',
}
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'ASSIGN',
          'LBRACE', 'RBRACE', 'SEMICOLON', 'COMMA', 'DPLUS', 'DMINUS', 'ID', 'EDIVIDE', 'MINEQUAL', 'PLUSEQUAL',
          'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'DOT', 'STRING', ] + list(reserved_words.values())

# Define of tokens
t_PLUSEQUAL = r'\+='
t_MINEQUAL = r'-='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EDIVIDE = r'//'  # 整除
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ASSIGN = r'='
t_DPLUS = r'\+\+'  # 自增
t_DMINUS = r'--'  # 自减
t_COMMA = r','
t_SEMICOLON = r';'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_DOT = r'\.'


# 识别字符串，解决 "string" <token> "string" 情况下匹配不到两个字符串的问题
def t_STRING(t):
    r'".*"|\'.*\''
    start, end = t.lexer.lexmatch.span()  # 匹配到的位置
    quot = t.lexer.lexdata[start]
    # 找到第一个结束引号的位置：除第一个引号外，首次出现的不在\字符后面的引号
    for i in range(start, end + 1):
        if t.lexer.lexdata[i] == quot:
            if i == start:
                continue
            if t.lexer.lexdata[i - 1] == '\\':
                continue
            end = i
            break
    t.lexer.lexpos = end + 1  # 修改（提前）分析点
    t.value = t.lexer.lexdata[start:end + 1]  # 修改数据
    return t


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
