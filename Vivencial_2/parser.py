import ply.yacc as yacc  # Importa a biblioteca PLY para a construção do parser
from lexer import tokens  # Importa os tokens gerados pelo analisador léxico (lexer.py)

# Definindo a precedência dos operadores aritméticos
precedence = (
    ('left', 'PLUS', 'MINUS'),  # '+' e '-' têm a mesma precedência (esquerda)
    ('left', 'TIMES', 'DIVIDE'),  # '*' e '/' têm a mesma precedência (esquerda)
)

# Regras de Produção

# Esta regra define que um programa consiste em uma lista de declarações e comandos.
# Quando a análise sintática é concluída com sucesso, imprime a mensagem de sucesso.
def p_programa(p):
    '''programa : lista_declaracoes_comandos'''
    print("Análise sintática concluída com sucesso!")

# Define que uma lista de declarações e comandos pode ser uma única declaração/comando ou uma lista de vários deles.
def p_lista_declaracoes_comandos(p):
    '''lista_declaracoes_comandos : declaracao_comando
                                  | lista_declaracoes_comandos declaracao_comando'''
    pass  # Esta regra apenas passa para as próximas, validando a lista de declarações e comandos

# Uma declaração ou comando pode ser uma declaração de variável ou um comando como if, while ou atribuição.
def p_declaracao_comando(p):
    '''declaracao_comando : declaracao
                          | comando'''
    pass  # Esta regra verifica se o código contém uma declaração ou comando

# Define a regra para uma declaração de variável. Exemplo: 'int a;' ou 'float b;'
def p_declaracao(p):
    '''declaracao : tipo lista_variaveis SEMICOLON'''
    pass  # A declaração deve ter um tipo, lista de variáveis e terminar com ';'

# Define os tipos de variáveis aceitos: char, int ou float.
def p_tipo(p):
    '''tipo : CHAR
            | INT
            | FLOAT'''
    pass  # Aceita os tipos básicos de variáveis inspirados na linguagem C

# Define uma lista de variáveis que podem ser declaradas, com ou sem separação por vírgula. Exemplo: 'int a, b, c;'
def p_lista_variaveis(p):
    '''lista_variaveis : variavel
                       | lista_variaveis COMMA variavel'''
    pass  # Suporta múltiplas variáveis separadas por vírgulas ou uma única variável

# Define a regra para uma variável. Pode ser um identificador simples ou um array. Exemplo: 'a' ou 'a[10]'
def p_variavel(p):
    '''variavel : IDENTIFIER
                | IDENTIFIER LBRACKET NUMERO_INTEIRO RBRACKET'''
    pass  # Variável simples ou array de tamanho definido

# Define os comandos suportados pelo parser: if, while ou atribuição
def p_comando(p):
    '''comando : comando_if
               | comando_while
               | comando_atribuicao'''
    pass  # Aceita comandos de controle (if, while) e de atribuição

# Regra para o comando 'if'. Ele pode ter uma parte opcional 'else'.
def p_comando_if(p):
    '''comando_if : IF LPAREN condicao RPAREN LBRACE lista_comandos RBRACE opcional_else'''
    pass  # 'if (condição) {comandos}' com 'else' opcional

# Define o 'else' como opcional. Se existir, segue com '{comandos}', caso contrário, vazio.
def p_opcional_else(p):
    '''opcional_else : ELSE LBRACE lista_comandos RBRACE
                     | empty'''
    pass  # 'else {comandos}' ou nenhuma instrução 'else'

# Regra para o comando 'while'. Sintaxe: 'while(condição) {comandos}'
def p_comando_while(p):
    '''comando_while : WHILE LPAREN condicao RPAREN LBRACE lista_comandos RBRACE'''
    pass  # 'while (condição) {comandos}'

# Uma lista de comandos pode ser um único comando ou uma lista de vários comandos
def p_lista_comandos(p):
    '''lista_comandos : comando
                      | lista_comandos comando'''
    pass  # Suporta múltiplos comandos dentro de um bloco

# Regra para atribuição de variáveis. Exemplo: 'a = 5;' ou 'a += 1;'
def p_comando_atribuicao(p):
    '''comando_atribuicao : IDENTIFIER operador_atribuicao expressao_aritmetica SEMICOLON'''
    pass  # Suporta diferentes tipos de atribuição, como '=' e '+='

# Define os operadores de atribuição, como '=', '+=', '-=', etc.
def p_operador_atribuicao(p):
    '''operador_atribuicao : EQUAL
                           | PLUS_EQUAL
                           | MINUS_EQUAL
                           | TIMES_EQUAL
                           | DIVIDE_EQUAL'''
    pass  # Operadores de atribuição aceitos

# Define uma condição composta por duas expressões aritméticas e um operador relacional. Exemplo: 'a == b'
def p_condicao(p):
    '''condicao : expressao_aritmetica operador_relacional expressao_aritmetica'''
    pass  # Define condições com operadores relacionais, como 'a > b'

# Define os operadores relacionais aceitos, como '==', '!=', '<', '>'
def p_operador_relacional(p):
    '''operador_relacional : EQUAL_EQUAL
                           | NOT_EQUAL
                           | LESS_EQUAL
                           | GREATER_EQUAL
                           | LESS
                           | GREATER'''
    pass  # Operadores relacionais suportados

# Regra para expressões aritméticas que envolvem soma ou subtração
def p_expressao_aritmetica(p):
    '''expressao_aritmetica : expressao_aritmetica PLUS termo
                            | expressao_aritmetica MINUS termo
                            | termo'''
    pass  # Suporta operações aritméticas com '+' e '-'

# Regra para multiplicação ou divisão entre termos
def p_termo(p):
    '''termo : termo TIMES fator
             | termo DIVIDE fator
             | fator'''
    pass  # Suporta operações aritméticas com '*' e '/'

# Define um fator como um identificador, número ou uma expressão entre parênteses
def p_fator(p):
    '''fator : IDENTIFIER
             | numero
             | LPAREN expressao_aritmetica RPAREN'''
    pass  # Suporta expressões como 'a', '5' ou '(a + b)'

# Regra para números inteiros ou reais
def p_numero(p):
    '''numero : NUMERO_INTEIRO
              | NUMERO_REAL'''
    pass  # Reconhece números inteiros e números com ponto flutuante

# Define uma regra vazia, usada para casos onde algo é opcional
def p_empty(p):
    'empty :'
    pass  # Regra vazia para lidar com opções

# Função de tratamento de erro. Quando há um erro, ele imprime a linha e o token onde ocorreu o erro.
def p_error(p):
    if p:
        print(
            f"Erro sintático próximo ao token '{p.value}' na linha {p.lineno}")
    else:
        print("Erro sintático no final da entrada")

# Construção do Parser usando as regras acima
parser = yacc.yacc()
