import ply.lex as lex  # Importa a biblioteca PLY para construção do analisador léxico (lexer)

# Palavras Reservadas
# Definimos as palavras-chave da linguagem que estamos reconhecendo (char, int, float, if, else, while).
reserved = {
    'char': 'CHAR',
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

# Lista de Tokens
# Aqui definimos todos os tokens que o lexer deve reconhecer, incluindo operadores e símbolos.
# A lista inclui tanto tokens manuais (como PLUS, MINUS) quanto as palavras reservadas.
tokens = [
    'IDENTIFIER',  # Identificadores (nomes de variáveis, funções, etc.)
    'NUMERO_INTEIRO',  # Números inteiros
    'NUMERO_REAL',  # Números reais (com ponto flutuante)
    'PLUS',  # Operador de adição '+'
    'MINUS',  # Operador de subtração '-'
    'TIMES',  # Operador de multiplicação '*'
    'DIVIDE',  # Operador de divisão '/'
    'PLUS_EQUAL',  # Operador '+='
    'MINUS_EQUAL',  # Operador '-='
    'TIMES_EQUAL',  # Operador '*='
    'DIVIDE_EQUAL',  # Operador '/='
    'EQUAL',  # Operador de atribuição '='
    'EQUAL_EQUAL',  # Operador de igualdade '=='
    'NOT_EQUAL',  # Operador de desigualdade '!='
    'LESS_EQUAL',  # Operador 'menor ou igual' '<='
    'GREATER_EQUAL',  # Operador 'maior ou igual' '>='
    'LESS',  # Operador 'menor que' '<'
    'GREATER',  # Operador 'maior que' '>'
    'SEMICOLON',  # Ponto-e-vírgula ';'
    'COMMA',  # Vírgula ','
    'LBRACKET',  # Colchete esquerdo '['
    'RBRACKET',  # Colchete direito ']'
    'LPAREN',  # Parêntese esquerdo '('
    'RPAREN',  # Parêntese direito ')'
    'LBRACE',  # Chave esquerda '{'
    'RBRACE',  # Chave direita '}'
] + list(reserved.values())  # Adicionamos também as palavras reservadas à lista de tokens

# Expressões Regulares para Tokens Simples
# Aqui, definimos como o lexer reconhecerá cada um desses tokens com expressões regulares (regex).

t_PLUS = r'\+'  # Reconhece o símbolo '+' para adição
t_MINUS = r'-'  # Reconhece o símbolo '-' para subtração
t_TIMES = r'\*'  # Reconhece o símbolo '*' para multiplicação
t_DIVIDE = r'/'  # Reconhece o símbolo '/' para divisão
t_PLUS_EQUAL = r'\+='  # Reconhece '+='
t_MINUS_EQUAL = r'-='  # Reconhece '-='
t_TIMES_EQUAL = r'\*='  # Reconhece '*='
t_DIVIDE_EQUAL = r'/='  # Reconhece '/='
t_EQUAL_EQUAL = r'=='  # Reconhece '==', operador de igualdade
t_EQUAL = r'='  # Reconhece '=' para atribuição
t_NOT_EQUAL = r'!='  # Reconhece '!=', operador de diferença
t_LESS_EQUAL = r'<='  # Reconhece '<=', menor ou igual
t_GREATER_EQUAL = r'>='  # Reconhece '>=', maior ou igual
t_LESS = r'<'  # Reconhece '<', menor que
t_GREATER = r'>'  # Reconhece '>', maior que
t_SEMICOLON = r';'  # Reconhece ';', para terminar instruções
t_COMMA = r','  # Reconhece ',' como separador de variáveis ou argumentos
t_LBRACKET = r'\['  # Reconhece '[', para declaração de arrays
t_RBRACKET = r'\]'  # Reconhece ']', para fechar arrays
t_LPAREN = r'\('  # Reconhece '(', para abrir expressões ou argumentos
t_RPAREN = r'\)'  # Reconhece ')', para fechar expressões ou argumentos
t_LBRACE = r'\{'  # Reconhece '{', para abrir blocos de código
t_RBRACE = r'\}'  # Reconhece '}', para fechar blocos de código

# Ignorar espaços e tabulações
# O lexer vai ignorar espaços e tabulações, pois não são relevantes para a análise sintática.
t_ignore = ' \t'

# Função para reconhecer comentários.
# Qualquer linha que comece com '//' será ignorada pelo lexer.
def t_COMMENT(t):
    r'//.*'
    pass  # Ignora o comentário e não retorna um token para ele

# Função para identificar Identificadores e Palavras Reservadas
# Se a sequência de caracteres se parecer com uma palavra reservada (como 'int', 'if'), ela será marcada como tal.
# Caso contrário, será tratada como um identificador (nome de variável, função, etc.).
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores começam com uma letra ou '_', seguidos por letras, números ou '_'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica se o identificador é uma palavra reservada
    return t  # Retorna o token identificado

# Função para reconhecer números reais (com casas decimais).
# Exemplo: 3.14, 0.99
def t_NUMERO_REAL(t):
    r'\d+\.\d+'  # Números reais têm dígitos seguidos de um ponto e mais dígitos
    t.value = float(t.value)  # Converte o valor reconhecido para float
    return t  # Retorna o token do número real

# Função para reconhecer números inteiros.
# Exemplo: 123, 456
def t_NUMERO_INTEIRO(t):
    r'\d+'  # Reconhece uma sequência de dígitos
    t.value = int(t.value)  # Converte o valor reconhecido para inteiro
    return t  # Retorna o token do número inteiro

# Função para contar o número de linhas
# Cada vez que uma nova linha for encontrada, o contador de linhas será incrementado.
def t_newline(t):
    r'\n+'  # Reconhece uma ou mais quebras de linha
    t.lexer.lineno += len(t.value)  # Incrementa o número de linhas pelo número de quebras de linha encontradas

# Função de Tratamento de Erros
# Caso o lexer encontre um caractere não reconhecido, ele chamará esta função.
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")  # Exibe o caractere ilegal e a linha onde ocorreu o erro
    t.lexer.skip(1)  # Pula o caractere inválido e continua analisando

# Construção do Lexer
# Aqui o lexer é criado com base nas regras definidas anteriormente.
lexer = lex.lex()
