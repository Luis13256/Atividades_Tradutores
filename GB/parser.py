import ply.yacc as yacc
from lexer import tokens  # noqa: F401

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras de Produção


def p_programa(p):  # Define que um programa consiste em uma lista de declarações e comandos.
    '''programa : lista_declaracoes_comandos'''
    print("Análise sintática concluída com sucesso!")


def p_lista_declaracoes_comandos(p):  # Define que uma lista de declarações e comandos pode ser uma única declaração/comando ou uma lista de vários deles.
    '''lista_declaracoes_comandos : declaracao_comando
                                  | lista_declaracoes_comandos declaracao_comando'''
    pass  # Esta regra apenas passa para as próximas, validando a lista de declarações e comandos


def p_declaracao_comando(p):  # Uma declaração ou comando pode ser uma declaração de variável ou um comando como if, while ou atribuição.
    '''declaracao_comando : declaracao
                          | comando'''
    pass  # Esta regra verifica se o código contém uma declaração ou comando


def p_declaracao(p):  # Define a regra para uma declaração de variável. Exemplo: 'int a;' ou 'float b;'
    '''declaracao : tipo lista_variaveis SEMICOLON'''
    pass  # A declaração deve ter um tipo, lista de variáveis e terminar com ';'


def p_tipo(p):  # Define os tipos de variáveis aceitos: char, int ou float.
    '''tipo : CHAR
            | INT
            | FLOAT'''
    pass  # Aceita os tipos básicos de variáveis inspirados na linguagem C


def p_lista_variaveis(p):  # Define uma lista de variáveis que podem ser declaradas. Exemplo: 'int a, b, c;'
    '''lista_variaveis : variavel
                       | lista_variaveis COMMA variavel'''
    pass  # Suporta múltiplas variáveis separadas por vírgulas ou uma única variável


def p_variavel(p):  # Define a regra para uma variável. Pode ser um identificador simples ou um array. Exemplo: 'a' ou 'a[10]'
    '''variavel : IDENTIFIER
                | IDENTIFIER LBRACKET NUMERO_INTEIRO RBRACKET'''
    pass  # Variável simples ou array de tamanho definido


def p_comando(p):  # Define os comandos suportados pelo parser: if, while ou atribuição
    '''comando : comando_if
               | comando_while
               | comando_atribuicao'''
    pass  # Aceita comandos de controle (if, while) e de atribuição


def p_comando_if(p):  # Regra para o comando 'if'. Ele pode ter uma parte opcional 'else'.
    '''comando_if : IF LPAREN condicao RPAREN LBRACE lista_comandos RBRACE opcional_else'''
    pass  # 'if (condição) {comandos}' com 'else' opcional


def p_opcional_else(p):  # Define o 'else' como opcional. Se existir, segue com '{comandos}', caso contrário, vazio.
    '''opcional_else : ELSE LBRACE lista_comandos RBRACE
                     | empty'''
    pass  # 'else {comandos}' ou nenhuma instrução 'else'


def p_comando_while(p):  # Regra para o comando 'while'. Sintaxe: 'while(condição) {comandos}'
    '''comando_while : WHILE LPAREN condicao RPAREN LBRACE lista_comandos RBRACE'''
    pass  # 'while (condição) {comandos}'


def p_lista_comandos(p):  # Uma lista de comandos pode ser um único comando ou uma lista de vários comandos
    '''lista_comandos : comando
                      | lista_comandos comando'''
    pass  # Suporta múltiplos comandos dentro de um bloco


def p_comando_atribuicao(p):  # Regra para atribuição de variáveis. Exemplo: 'a = 5;' ou 'a += 1;'
    '''comando_atribuicao : IDENTIFIER operador_atribuicao expressao_aritmetica SEMICOLON'''
    pass  # Suporta diferentes tipos de atribuição, como '=' e '+='


def p_operador_atribuicao(p):  # Define os operadores de atribuição, como '=', '+=', '-=', etc.
    '''operador_atribuicao : EQUAL
                           | PLUS_EQUAL
                           | MINUS_EQUAL
                           | TIMES_EQUAL
                           | DIVIDE_EQUAL'''
    pass  # Operadores de atribuição aceitos


def p_condicao(p):  # Define uma condição composta por duas expressões aritméticas e um operador relacional. Exemplo: 'a == b'
    '''condicao : expressao_aritmetica operador_relacional expressao_aritmetica'''
    pass  # Define condições com operadores relacionais, como 'a > b'


def p_operador_relacional(p):  # Define os operadores relacionais aceitos, como '==', '!=', '<', '>'
    '''operador_relacional : EQUAL_EQUAL
                           | NOT_EQUAL
                           | LESS_EQUAL
                           | GREATER_EQUAL
                           | LESS
                           | GREATER'''
    pass  # Operadores relacionais suportados


def p_expressao_aritmetica(p):  # Regra para expressões aritméticas que envolvem soma ou subtração
    '''expressao_aritmetica : expressao_aritmetica PLUS termo
                            | expressao_aritmetica MINUS termo
                            | termo'''
    pass  # Suporta operações aritméticas com '+' e '-'


def p_termo(p):  # Regra para multiplicação ou divisão entre termos
    '''termo : termo TIMES fator
             | termo DIVIDE fator
             | fator'''
    pass  # Suporta operações aritméticas com '*' e '/'


def p_fator(p):  # Define um fator como um identificador, número ou uma expressão entre parênteses
    '''fator : IDENTIFIER
             | numero
             | LPAREN expressao_aritmetica RPAREN'''
    pass  # Suporta expressões como 'a', '5' ou '(a + b)'


def p_numero(p):  # Regra para números inteiros ou reais
    '''numero : NUMERO_INTEIRO
              | NUMERO_REAL'''
    pass  # Reconhece números inteiros e números com ponto flutuante


def p_empty(p):  # Define uma regra vazia, usada para casos onde algo é opcional
    'empty :'
    pass  # Regra vazia para lidar com opções


def p_error(p):  # Função de tratamento de erro.
    if p:
        print(
            f"Erro sintático próximo ao token '{p.value}' na linha {p.lineno}")
    else:
        print("Erro sintático no final da entrada")


# Construção do Parser
parser = yacc.yacc()
