"""
语法：
program : statements
statements : statements statement | statement
statement : assignment | expr | print | if | while | for | break | function | return | class
assignment : variable ASSIGN expr | variable MINEQUAL expr | variable PLUSEQUAL expr | variable DPLUS | variable DMINUS
variable : variable LBRACKET expr RBRACKET | ID | ID DOT ID
expr : expr PLUS term | expr MINUS term | term | array | string
term : term TIMES factor | term DIVIDE factor | term EDIVIDE factor | factor
factor : variable | NUMBER | len | call | LPAREN expr RPAREN
exprs : exprs COMMA expr | expr
len : LEN LPAREN variable RPAREN
print : PRINT LPAREN exprs RPAREN | PRINT LPAREN RPAREN
array : LBRACKET exprs RBRACKET | LBRACKET RBRACKET
condition : condition OR join | join
join : join AND equality | equality
equality : equality EQ rel | equality NE rel | rel
rel : expr LT expr | expr LE expr | expr GT expr | expr GE expr | expr
if : IF LPAREN condition RPAREN LBRACE statements RBRACE
   | IF LPAREN condition RPAREN LBRACE statements RBRACE else
else : ELIF LPAREN condition RPAREN LBRACE statements RBRACE
     | ELIF LPAREN condition RPAREN LBRACE statements RBRACE else
     | ELSE LBRACE statements RBRACE
while : WHILE LPAREN condition RPAREN LBRACE statements RBRACE
for : FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN LBRACE statements RBRACE
break : BREAK
function : DEF ID LPAREN args RPAREN LBRACE statements RBRACE | DEF ID LPAREN RPAREN LBRACE statements RBRACE
args : args COMMA ID | ID
call : ID LPAREN exprs RPAREN | ID LPAREN RPAREN | ID DOT ID LPAREN exprs RPAREN | ID DOT ID LPAREN RPAREN
return : RETURN | RETURN exprs
class : CLASS ID LBRACE functions RBRACE
functions : functions function | function
string : STRING
"""

# coding=utf-8
from ply import yacc

from node import *
# noinspection PyUnresolvedReferences
from py_lex import *


# YACC for parsing Python


def p_program(t):
    """program : statements"""
    if len(t) == 2:
        t[0] = NonTerminal('Program')
        t[0].add(t[1])


def p_statements(t):
    """statements : statements statement
                  | statement"""
    if len(t) == 3:
        t[0] = NonTerminal('Statements')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t) == 2:
        t[0] = NonTerminal('Statements')
        t[0].add(t[1])


def p_statement(t):
    """ statement : assignment
                  | expr
                  | print
                  | if
                  | while
                  | for
                  | break
                  | function
                  | class
                  | return"""
    if len(t) == 2:
        t[0] = NonTerminal('Statement')
        t[0].add(t[1])


def p_assignment(t):
    """assignment : variable ASSIGN expr
                  | variable MINEQUAL expr
                  | variable PLUSEQUAL expr
                  | variable DPLUS
                  | variable DMINUS"""
    if len(t) == 4:
        t[0] = NonTerminal('Assignment')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    if len(t) == 3:
        t[0] = NonTerminal('Assignment')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))


def p_variable(t):
    """variable : variable LBRACKET expr RBRACKET
                | ID DOT ID
                | ID"""
    if len(t) == 2:
        t[0] = Variable('Variable')
        t[0].add(ID(t[1]))
    elif len(t) == 4:
        t[0] = Variable('Variable')
        t[0].add(ID(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(ID(t[3]))
    elif len(t) == 5:
        t[0] = Variable('Variable')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))


def p_expr(t):
    """expr : expr PLUS term
            | expr MINUS term
            | term
            | string
            | array"""
    if len(t) == 4:
        t[0] = NonTerminal('Expr')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Expr')
        t[0].add(t[1])


def p_term(t):
    """term : term TIMES factor
            | term DIVIDE factor
            | term EDIVIDE factor
            | factor"""
    if len(t) == 4:
        t[0] = NonTerminal('Term')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Term')
        t[0].add(t[1])


def p_factor(t):
    """factor : variable
              | NUMBER
              | len
              | call
              | LPAREN expr RPAREN """
    if len(t) == 4:
        t[0] = NonTerminal('Factor')
        t[0].add(Terminal(t[1]))
        t[0].add(t[2])
        t[0].add(Terminal(t[3]))
    elif len(t) == 2:
        t[0] = NonTerminal('Factor')
        if isinstance(t[1], int) or str(t[1]).isdigit():
            t[0].add(Number(t[1]))
        else:
            t[0].add(t[1])


def p_exprs(t):
    """exprs : exprs COMMA expr
             | expr"""
    if len(t) == 4:
        t[0] = NonTerminal('Exprs')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Exprs')
        t[0].add(t[1])


def p_len(t):
    """len : LEN LPAREN variable RPAREN"""
    if len(t) == 5:
        t[0] = NonTerminal('Len')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))


def p_print(t):
    """print : PRINT LPAREN exprs RPAREN
             | PRINT LPAREN RPAREN"""
    if len(t) == 5:
        t[0] = NonTerminal('Print')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))
    elif len(t) == 3:
        t[0] = NonTerminal('Print')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(Terminal(t[3]))


def p_array(t):
    """array : LBRACKET exprs RBRACKET
             | LBRACKET RBRACKET"""
    if len(t) == 4:
        t[0] = NonTerminal('Array')
        t[0].add(Terminal(t[1]))
        t[0].add(t[2])
        t[0].add(Terminal(t[3]))
    elif len(t) == 3:
        t[0] = NonTerminal('Array')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))


def p_condition(t):
    """condition : condition OR join
                 | join"""
    if len(t) == 4:
        t[0] = NonTerminal('Condition')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Condition')
        t[0].add(t[1])


def p_join(t):
    """join : join AND equality
            | equality"""
    if len(t) == 4:
        t[0] = NonTerminal('Join')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Join')
        t[0].add(t[1])


def p_equality(t):
    """equality : equality EQ rel
                | equality NE rel
                | rel"""
    if len(t) == 4:
        t[0] = NonTerminal('Equality')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Equality')
        t[0].add(t[1])


def p_rel(t):
    """rel : expr LT expr
           | expr LE expr
           | expr GT expr
           | expr GE expr
           | expr"""
    if len(t) == 4:
        t[0] = NonTerminal('Relation')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
    elif len(t) == 2:
        t[0] = NonTerminal('Relation')
        t[0].add(t[1])


def p_if(t):
    """if : IF LPAREN condition RPAREN LBRACE statements RBRACE
          | IF LPAREN condition RPAREN LBRACE statements RBRACE else"""
    if 8 <= len(t) <= 9:
        t[0] = NonTerminal('If')
        t[0].add(Terminal(t[1]))  # if
        t[0].add(Terminal(t[2]))  # (
        t[0].add(t[3])  # condition
        t[0].add(Terminal(t[4]))  # )
        t[0].add(Terminal(t[5]))  # {
        t[0].add(t[6])  # statements
        t[0].add(Terminal(t[7]))  # }
        if len(t) == 9:
            t[0].add(t[8])  # `else`


def p_else(t):
    """else : ELIF LPAREN condition RPAREN LBRACE statements RBRACE
            | ELIF LPAREN condition RPAREN LBRACE statements RBRACE else
            | ELSE LBRACE statements RBRACE"""
    if len(t) == 5:
        t[0] = NonTerminal('Else')
        t[0].add(Terminal(t[1]))  # else
        t[0].add(Terminal(t[2]))  # {
        t[0].add(t[3])  # statements
        t[0].add(Terminal(t[4]))  # }
    elif 8 <= len(t) <= 9:
        t[0] = NonTerminal('Else')
        t[0].add(Terminal(t[1]))  # elif
        t[0].add(Terminal(t[2]))  # (
        t[0].add(t[3])  # condition
        t[0].add(Terminal(t[4]))  # )
        t[0].add(Terminal(t[5]))  # {
        t[0].add(t[6])  # statements
        t[0].add(Terminal(t[7]))  # }
        if len(t) == 9:
            t[0].add(t[8])  # `else`


def p_while(t):
    """while : WHILE LPAREN condition RPAREN LBRACE statements RBRACE"""
    if len(t) == 8:
        t[0] = NonTerminal('While')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))
        t[0].add(Terminal(t[5]))
        t[0].add(t[6])
        t[0].add(Terminal(t[7]))


def p_for(t):
    """for : FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN LBRACE statements RBRACE"""
    if len(t) == 12:
        t[0] = NonTerminal('For')
        t[0].add(Terminal(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))
        t[0].add(t[5])
        t[0].add(Terminal(t[6]))
        t[0].add(t[7])
        t[0].add(Terminal(t[8]))
        t[0].add(Terminal(t[9]))
        t[0].add(t[10])
        t[0].add(Terminal(t[11]))


def p_break(t):
    """break : BREAK"""
    if len(t) == 2:
        t[0] = NonTerminal('Break')
        t[0].add(Terminal(t[1]))


def p_function(t):
    """function : DEF ID LPAREN args RPAREN LBRACE statements RBRACE
                | DEF ID LPAREN RPAREN LBRACE statements RBRACE"""
    if len(t) == 9:
        t[0] = NonTerminal('Function')
        t[0].add(Terminal(t[1]))
        t[0].add(ID(t[2]))
        t[0].add(Terminal(t[3]))
        t[0].add(t[4])
        t[0].add(Terminal(t[5]))
        t[0].add(Terminal(t[6]))
        t[0].add(t[7])
        t[0].add(Terminal(t[8]))
    elif len(t) == 8:
        t[0] = NonTerminal('Function')
        t[0].add(Terminal(t[1]))
        t[0].add(ID(t[2]))
        t[0].add(Terminal(t[3]))
        t[0].add(Terminal(t[4]))
        t[0].add(Terminal(t[5]))
        t[0].add(t[6])
        t[0].add(Terminal(t[7]))


def p_args(t):
    """args : args COMMA ID
            | ID"""
    if len(t) == 4:
        t[0] = NonTerminal('Args')
        t[0].add(t[1])
        t[0].add(Terminal(t[2]))
        t[0].add(ID(t[3]))
    elif len(t) == 2:
        t[0] = NonTerminal('Args')
        t[0].add(ID(t[1]))


def p_call(t):
    """call : ID LPAREN exprs RPAREN
            | ID LPAREN RPAREN
            | ID DOT ID LPAREN exprs RPAREN
            | ID DOT ID LPAREN RPAREN"""
    if len(t) == 5:
        t[0] = NonTerminal('Call')
        t[0].add(ID(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(t[3])
        t[0].add(Terminal(t[4]))
    elif len(t) == 4:
        t[0] = NonTerminal('Call')
        t[0].add(ID(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(Terminal(t[3]))
    elif len(t) == 7:
        t[0] = NonTerminal('Call')
        t[0].add(ID(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(ID(t[3]))
        t[0].add(Terminal(t[4]))
        t[0].add(t[5])
        t[0].add(Terminal(t[6]))
    elif len(t) == 6:
        t[0] = NonTerminal('Call')
        t[0].add(ID(t[1]))
        t[0].add(Terminal(t[2]))
        t[0].add(ID(t[3]))
        t[0].add(Terminal(t[4]))
        t[0].add(Terminal(t[5]))


def p_return(t):
    """return : RETURN
              | RETURN exprs"""
    if len(t) == 2:
        t[0] = NonTerminal('Return')
        t[0].add(Terminal(t[1]))
    elif len(t) == 3:
        t[0] = NonTerminal('Return')
        t[0].add(Terminal(t[1]))
        t[0].add(t[2])


def p_class(t):
    """class : CLASS ID LBRACE functions RBRACE"""
    if len(t) == 6:
        t[0] = NonTerminal('Class')
        t[0].add(Terminal(t[1]))
        t[0].add(ID(t[2]))
        t[0].add(Terminal(t[3]))
        t[0].add(t[4])
        t[0].add(Terminal(t[5]))


def p_functions(t):
    """functions : functions function
                 | function"""
    if len(t) == 2:
        t[0] = NonTerminal('Functions')
        t[0].add(t[1])
    elif len(t) == 3:
        t[0] = NonTerminal('Functions')
        t[0].add(t[1])
        t[0].add(t[2])


def p_string(t):
    """string : STRING"""
    if len(t) == 2:
        t[0] = NonTerminal('String')
        t[0].add(String(t[1]))


def p_error(t):
    print(t)
    if t is None:
        raise SyntaxError("Syntax error")
    raise SyntaxError("Syntax error '%s' at line %d" % (t.value[0], t.lexer.lineno))


yacc.yacc()
