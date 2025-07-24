import ply.yacc as yacc
from lexer.my_lexer import tokens

# -----------------------------
# Parser for CustomScript
# -----------------------------
# Set the start symbol
start = 'program'

# Program entry point
def p_program(p):
    'program : statement_list'
    p[0] = p[1]

# Statement list (supports multiple statements)
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Variable declaration
def p_statement_var_decl(p):
    'statement : VAR ID EQUALS expression SEMICOLON'
    p[0] = {'type': 'var_decl', 'name': p[2], 'value': p[4]}

# Assignment statement
def p_statement_assignment(p):
    'statement : ID EQUALS expression SEMICOLON'
    p[0] = {'type': 'assignment', 'name': p[1], 'value': p[3]}

# Print statement
def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMICOLON'
    p[0] = {'type': 'print', 'value': p[3]}

# While loop
def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = {'type': 'while', 'condition': p[3], 'body': p[6]}

# If statement
def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = {'type': 'if', 'condition': p[3], 'then': p[6]}

# If-else statement
def p_statement_if_else(p):
    'statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'
    p[0] = {'type': 'if', 'condition': p[3], 'then': p[6], 'else': p[10]}

# Binary operations (arithmetic and comparison)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = {'type': 'binop', 'op': p[2], 'left': p[1], 'right': p[3]}

# Number literal
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = {'type': 'number', 'value': p[1]}

# Variable reference
def p_expression_var(p):
    'expression : ID'
    p[0] = {'type': 'var', 'name': p[1]}

# Error handling
def p_error(p):
    if p:
        print(f"Syntax Error: Unexpected token '{p.value}' near line {p.lineno}")
    else:
        print("Syntax Error: Unexpected end of input")

# Build the parser
parser = yacc.yacc()

def parse_code(code):
    return parser.parse(code)