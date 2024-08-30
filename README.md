
PLY Lexical Analyzer Implementation

Ferramenta Escolhida
A ferramenta escolhida para a implementação deste analisador léxico é o PLY (Python Lex-Yacc). PLY é uma implementação em Python das ferramentas tradicionais de compiladores lex e yacc, que são usadas para análise léxica e sintática. Optamos por utilizar o PLY devido à sua simplicidade e robustez, além de ser totalmente escrito em Python, o que facilita a integração com outros projetos desenvolvidos nessa linguagem.

Descrição do Projeto
Este projeto implementa um analisador léxico utilizando o PLY para reconhecer diferentes padrões de expressões regulares. As expressões regulares definidas são capazes de identificar:

1. Números de telefones celulares no Brasil com o código de área: Exemplo - (11) 98765-4321
2. Placas de Carros Brasileiros: Exemplo - ABC-1234
3. CPF (Cadastro de Pessoas Físicas): Exemplo - 123.456.789-00
4. Números Reais: Exemplo - 45.67
5. Tags HTML: Exemplo - <div>Some HTML content</div>
6. URLs de Páginas Web: Exemplo - https://www.example.com
7. Palavras da Língua Portuguesa: Exemplo - palavra
8. CNPJ (Cadastro Nacional da Pessoa Jurídica): Exemplo - 12.345.678/0001-95
9. Identificadores da Linguagem C: Exemplo - variavel

Código-Fonte
A seguir está o código-fonte da implementação, devidamente comentado para facilitar o entendimento:

import ply.lex as lex

# List of token names
tokens = (
    'TELEFONE',        # Números de telefone com DDD
    'PLACA',           # Placas de carros brasileiros
    'CPF',             # Cadastro de Pessoas Físicas
    'NUMERO_REAL',     # Números reais
    'TAG_HTML',        # Tags HTML padrão
    'URL',             # URLs de páginas web
    'PALAVRA_PT',      # Palavras da Língua Portuguesa
    'CNPJ',            # Cadastro Nacional da Pessoa Jurídica
    'IDENTIFICADOR_C', # Identificadores na linguagem C
)

# 8. CNPJ - Reconhece o formato de CNPJ
def t_CNPJ(t):
    r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'
    return t

# 1. Números de telefones celulares no Brasil com o código de área
def t_TELEFONE(t):
    r'\(\d{2}\)\s\d{5}-\d{4}'
    return t

# 2. Placas de Carros Brasileiros
def t_PLACA(t):
    r'[A-Z]{3}-\d{4}|[A-Z]{3}\d[A-Z]\d{2}'
    return t

# 3. CPF
def t_CPF(t):
    r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    return t

# 4. Números reais
def t_NUMERO_REAL(t):
    r'\d+\.\d+'
    return t

# 5. Tags HTML (padrão)
def t_TAG_HTML(t):
    r'<[^>]+>'
    return t

# 6. URL de páginas web
def t_URL(t):
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return t

# 7. Palavras da Língua Portuguesa
def t_PALAVRA_PT(t):
    r'[a-zA-ZÀ-ÿ]+'
    return t

# 9. Identificadores da Linguagem C
def t_IDENTIFICADOR_C(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignored characters (spaces, tabs, newlines)
t_ignore = ' \t\r\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Example input data
data = '''
(11) 98765-4321
ABC-1234
123.456.789-00
45.67
<div>Some HTML content</div>
https://www.example.com
palavra
12.345.678/0001-95
variavel
'''
