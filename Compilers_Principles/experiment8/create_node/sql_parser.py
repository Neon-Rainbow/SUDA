import ply.lex as lex
import ply.yacc as yacc
import re
from math import *
from node import Node

reserved = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE',
    'ORDER': 'ORDER',
    'BY': 'BY',
    'AND': 'AND',
    'OR': 'OR',
    'AVG': 'AVG',
    'BETWEEN': 'BETWEEN',
    'IN': 'IN',
    'SUM': 'SUM',
    'MAX': 'MAX',
    'MIN': 'MIN',
    'COUNT': 'COUNT',
    'AS': 'AS',
}

# TOKENS
tokens = list(reserved.values()) + [
    'NAME', 'COMMA', 'LP', 'RP', 'NUMBER', 'DOT',
    'EQUALS', 'LT', 'GT', 'LE', 'GE', 'NE'
]


# DEFINE OF TOKENS
# Generic keyword token rule
def t_KEYWORD(t):
    r"""[A-Z]+"""
    t.type = reserved.get(t.value, 'NAME')  # Check for reserved words
    return t


# For example:
t_COMMA = r','
t_LP = r'\('
t_RP = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+(\.\d+)?'
t_DOT = r'\.'
t_EQUALS = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'<>'

# IGNORED
t_ignore = " \t"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# LEX ANALYSIS
lex.lex()


# PARSING
def p_query(t):
    """
    query :  select
    """
    t[0] = t[1]


def p_select(t):
    """
    select : SELECT list FROM table_list opt_where_clause
    """
    t[0] = Node('QUERY')
    node_select = Node("[SELECT]")
    node_select.add(t[2])
    t[0].add(node_select)
    node_from = Node("[FROM]")
    node_from.add(t[4])
    t[0].add(node_from)
    if t[5]:
        t[0].add(t[5])


def p_opt_where_clause(t):
    """
    opt_where_clause : WHERE condition
                     | empty
    """
    if len(t) > 2:
        t[0] = Node('[WHERE]')
        t[0].add(t[2])


def p_condition(t):
    """
    condition : NAME EQUALS NAME
              | NAME LT NAME
              | NAME GT NAME
              | NAME LE NAME
              | NAME GE NAME
              | NAME NE NAME
              | condition AND condition
              | condition OR condition
              | LP condition RP
              | NAME BETWEEN NAME AND NAME
    """
    t[0] = Node('[CONDITION]')

    if t[2] == "BETWEEN":
        t[0].add(Node(t[1]))
        t[0].add(Node('[BETWEEN]'))
        between_node = Node('BETWEEN_VALUES')
        between_node.add(Node(t[3]))
        between_node.add(Node(t[5]))
        t[0].add(between_node)
    else:
        for item in t[1:]:
            if isinstance(item, Node):
                t[0].add(item)
            else:
                t[0].add(Node(item))


def p_list(t):
    """
    list : list COMMA field
         | field
    """
    if len(t) == 2:  # single field
        t[0] = Node('[FIELDS]')
        t[0].add(t[1])
    else:  # multiple fields
        t[0] = t[1]  # Extend existing [FIELDS] node
        t[0].add(t[3])


def p_table_list(t):
    """
    table_list : table_list COMMA table
               | table
    """
    if len(t) == 2:  # single table
        t[0] = Node('[TABLES]')
        t[0].add(t[1])
    else:  # multiple tables
        t[0] = t[1]  # Extend existing [TABLES] node
        t[0].add(t[3])


def p_empty(t):
    """
    empty :
    """
    pass


def p_aggregate_function(t):
    """
    aggregate_function : AVG LP NAME RP
                       | SUM LP NAME RP
                       | MAX LP NAME RP
                       | MIN LP NAME RP
                       | COUNT LP NAME RP
    """
    t[0] = Node(f'[{t[1]}]')
    t[0].add(Node(t[3]))


def p_table(t):
    """
    table : NAME
          | NAME AS NAME
          | aggregate_function
          | aggregate_function AS NAME
    """
    t[0] = Node('[TABLE]')
    t[0].add(Node(t[1]))
    if len(t) > 2:
        asNode = Node('[AS]')
        asNode.add(Node(t[3]))
        t[0].add(asNode)


def p_field(t):
    """
    field : NAME
          | NAME AS NAME
          | aggregate_function
          | aggregate_function AS NAME
    """
    t[0] = Node('[FIELD]')
    if len(t) == 2:  # Either a simple name or an aggregate function without alias
        t[0].add(t[1])
    elif t[2] == 'AS' and isinstance(t[1], Node):  # An aggregate function with an alias
        agg_func_node = t[1]
        asNode = Node('[AS]')
        asNode.add(Node(t[3]))
        agg_func_node.add(asNode)
        t[0].add(agg_func_node)
    elif t[2] == 'AS':  # Either a simple name with an alias or an aggregate function with an alias
        t[0].add(Node(t[1]))
        asNode = Node('[AS]')
        asNode.add(Node(t[3]))
        t[0].add(asNode)
    else:  # Just a simple name without alias
        t[0].add(Node(t[1]))


yacc.yacc()


def createNode(query) -> Node:
    """
    该函数用来创建一个AST,用来表示SQL语句

    Args:
        query: 输入SQL语句

    Returns:
        返回一个AST的根节点
    """
    parse: Node = yacc.parse(query)
    return parse


if __name__ == "__main__":
    query = ('SELECT COUNT(column1) AS count_col1, COUNT(column2) AS count_col2, COUNT(column3) AS count_col3 '
             'FROM table1 AS tab1, table2 AS tab2 '
             'WHERE column1 BETWEEN value1 AND value2'
             )
    parse_node = createNode(query)
    parse_node.printNode()
