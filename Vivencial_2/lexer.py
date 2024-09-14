import ply.lex as lex

# Palavras Reservadas
reserved = {
    'char': 'CHAR',
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

# Lista de Tokens
tokens = [
    'IDENTIFIER',
    'NUMERO_INTEIRO',
    'NUMERO_REAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'TIMES_EQUAL',
    'DIVIDE_EQUAL',
    'EQUAL',
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'LESS',
    'GREATER',
    'SEMICOLON',
    'COMMA',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
] + list(reserved.values())

# Expressões Regulares para Tokens Simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_TIMES_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='
t_EQUAL_EQUAL = r'=='
t_EQUAL = r'='
t_NOT_EQUAL = r'!='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Comentários (opcional)


def t_COMMENT(t):
    r'//.*'
    pass

# Identificadores e Palavras Reservadas


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Números Reais


def t_NUMERO_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Números Inteiros


def t_NUMERO_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Contagem de Linhas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de Erros


def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)


# Construção do Lexer
lexer = lex.lex()
