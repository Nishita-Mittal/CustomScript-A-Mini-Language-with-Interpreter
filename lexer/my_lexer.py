import ply.lex as lex

# -----------------------------
# Lexer for CustomScript
# -----------------------------
# Reserved words
reserved = {
    'var': 'VAR',
    'print': 'PRINT',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR'
}

# List of token names
# (Add reserved words at the end)
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'SEMICOLON'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_GT        = r'>'
t_LT        = r'<'
t_GE        = r'>='
t_LE        = r'<='
t_EQ        = r'=='
t_NE        = r'!='
t_SEMICOLON = r';'

t_ignore = ' \t'

# Identifier and reserved word rule
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Integer literal rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Single-line comment rule (ignore //...)
def t_COMMENT(t):
    r'//.*'
    pass

# Build the lexer
lexer = lex.lex()
