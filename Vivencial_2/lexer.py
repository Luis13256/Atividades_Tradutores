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
    'IDENTIFIER',  # Identificadores (nomes de variáveis, funções, etc.)
    'NUMERO_INTEIRO',
    'NUMERO_REAL',
    'PLUS',  # '+'
    'MINUS',  # '-'
    'TIMES',  # '*'
    'DIVIDE',  # '/'
    'PLUS_EQUAL',  # '+='
    'MINUS_EQUAL',  # '-='
    'TIMES_EQUAL',  # '*='
    'DIVIDE_EQUAL',  # '/='
    'EQUAL',  # '='
    'EQUAL_EQUAL',  # '=='
    'NOT_EQUAL',  # '!='
    'LESS_EQUAL',  # '<='
    'GREATER_EQUAL',  # '>='
    'LESS',  # '<'
    'GREATER',  # '>'
    'SEMICOLON',  # ';'
    'COMMA',  # ','
    'LBRACKET',  # '['
    'RBRACKET',  # ']'
    'LPAREN',  # '('
    'RPAREN',  # ')'
    'LBRACE',  # '{'
    'RBRACE',  # '}'
] + list(reserved.values())

# Expressões Regulares para Tokens Simples
# Definimos como o lexer reconhecerá cada um desses tokens com expressões regulares (regex).

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

t_ignore = ' \t'  # Ignorar espaços e tabulações


def t_COMMENT(t):  # Função para reconhecer comentários.
    r'//.*'
    pass  # Ignora o comentário e não retorna um token para ele


def t_IDENTIFIER(t):  # Função para identificar Identificadores e Palavras Reservadas
    # Identificadores começam com uma letra ou '_', seguidos por letras, números ou '_'
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verifica se o identificador é uma palavra reservada
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t  # Retorna o token identificado


def t_NUMERO_REAL(t):  # Função para reconhecer números reais (com casas decimais). Exemplo: 3.14, 0.99
    r'\d+\.\d+'  # Números reais têm dígitos seguidos de um ponto e mais dígitos
    t.value = float(t.value)  # Converte o valor reconhecido para float
    return t  # Retorna o token do número real


def t_NUMERO_INTEIRO(t):  # Função para reconhecer números inteiros.
    r'\d+'  # Reconhece uma sequência de dígitos
    t.value = int(t.value)  # Converte o valor reconhecido para inteiro
    return t  # Retorna o token do número inteiro


def t_newline(t):  # Função para contar o número de linhas
    r'\n+'  # Reconhece uma ou mais quebras de linha
    # Incrementa o número de linhas pelo número de quebras de linha encontradas
    t.lexer.lineno += len(t.value)


def t_error(t):  # Função de Tratamento de Erros
    # Exibe o caractere ilegal e a linha onde ocorreu o erro
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)  # Pula o caractere inválido e continua analisando


lexer = lex.lex()  # Construção do Lexer
