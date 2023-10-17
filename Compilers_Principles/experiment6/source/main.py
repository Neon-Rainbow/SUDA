import ply.lex as lex

reserved = {
    'while': 'WHILE',
    'if': 'IF',
    'cout': 'COUT',
}


# List of token names
tokens = (
    'INT',
    'ID',
    'EQUALS',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LT',
    'STRING',
    'SEMICOLON',
    'COMMA',
    'ENDL',
    'LSHIFT',
    *reserved.values(),
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LT = r'<'
t_SEMICOLON = r';'
t_COMMA = r','
t_ENDL = r'endl'
t_LSHIFT = r'<<'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\".*?\"'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
with open('prog.cc', 'r') as f:
    data = f.read()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
