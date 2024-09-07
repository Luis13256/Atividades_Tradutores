import ply.lex as lex
import ply.yacc as yacc

# Definição dos tokens
tokens = (
    'TYPE', 'IDENTIFIER', 'NUMBER', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON'
)

# Regras de expressões regulares para tokens
t_ignore = ' \t'

def t_TYPE(t):
    r'char|int|float'
    return t

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_NUMBER = r'\d+'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Definição das regras de parsing
def p_declaration(p):
    'declaration : type var_list SEMICOLON'
    p[0] = (p[1], p[2])

def p_type(p):
    'type : TYPE'
    p[0] = p[1]

def p_var_list_single(p):
    'var_list : var'
    p[0] = [p[1]]

def p_var_list_multiple(p):
    'var_list : var COMMA var_list'
    p[0] = [p[1]] + p[3]

def p_var(p):
    '''var : IDENTIFIER
           | IDENTIFIER LBRACKET NUMBER RBRACKET'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

# Função para testar o parser
def test_parser(input_string):
    result = parser.parse(input_string)
    print(f"Result for '{input_string}': {result}")

if __name__ == '__main__':
    test_parser('int a;')
    test_parser('char x[10];')
    test_parser('float y;')
