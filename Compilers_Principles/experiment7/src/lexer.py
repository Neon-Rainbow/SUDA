"""
lexer.py: 定义化学分子式解析器的词法分析组件。

此模块定义了词法分析器，它可以识别化学元素的符号和数量。
"""

import ply.lex as lex

tokens = (
    'SYMBOL',
    'COUNT'
)

t_SYMBOL = (r'C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F['
            r'erm]?|G[aed]|I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|U|V|W|Xe|Yb?|Z[nr]')

t_COUNT = r'\d+'


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()
