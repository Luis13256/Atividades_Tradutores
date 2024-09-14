import ply.yacc as yacc
from lexer import tokens  # noqa: F401

# Precedência dos Operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras de Produção


def p_programa(p):
    '''programa : lista_declaracoes_comandos'''
    print("Análise sintática concluída com sucesso!")


def p_lista_declaracoes_comandos(p):
    '''lista_declaracoes_comandos : declaracao_comando
                                  | lista_declaracoes_comandos declaracao_comando'''
    pass


def p_declaracao_comando(p):
    '''declaracao_comando : declaracao
                          | comando'''
    pass


def p_declaracao(p):
    '''declaracao : tipo lista_variaveis SEMICOLON'''
    pass


def p_tipo(p):
    '''tipo : CHAR
            | INT
            | FLOAT'''
    pass


def p_lista_variaveis(p):
    '''lista_variaveis : variavel
                       | lista_variaveis COMMA variavel'''
    pass


def p_variavel(p):
    '''variavel : IDENTIFIER
                | IDENTIFIER LBRACKET NUMERO_INTEIRO RBRACKET'''
    pass


def p_comando(p):
    '''comando : comando_if
               | comando_while
               | comando_atribuicao'''
    pass


def p_comando_if(p):
    '''comando_if : IF LPAREN condicao RPAREN LBRACE lista_comandos RBRACE opcional_else'''
    pass


def p_opcional_else(p):
    '''opcional_else : ELSE LBRACE lista_comandos RBRACE
                     | empty'''
    pass


def p_comando_while(p):
    '''comando_while : WHILE LPAREN condicao RPAREN LBRACE lista_comandos RBRACE'''
    pass


def p_lista_comandos(p):
    '''lista_comandos : comando
                      | lista_comandos comando'''
    pass


def p_comando_atribuicao(p):
    '''comando_atribuicao : IDENTIFIER operador_atribuicao expressao_aritmetica SEMICOLON'''
    pass


def p_operador_atribuicao(p):
    '''operador_atribuicao : EQUAL
                           | PLUS_EQUAL
                           | MINUS_EQUAL
                           | TIMES_EQUAL
                           | DIVIDE_EQUAL'''
    pass


def p_condicao(p):
    '''condicao : expressao_aritmetica operador_relacional expressao_aritmetica'''
    pass


def p_operador_relacional(p):
    '''operador_relacional : EQUAL_EQUAL
                           | NOT_EQUAL
                           | LESS_EQUAL
                           | GREATER_EQUAL
                           | LESS
                           | GREATER'''
    pass


def p_expressao_aritmetica(p):
    '''expressao_aritmetica : expressao_aritmetica PLUS termo
                            | expressao_aritmetica MINUS termo
                            | termo'''
    pass


def p_termo(p):
    '''termo : termo TIMES fator
             | termo DIVIDE fator
             | fator'''
    pass


def p_fator(p):
    '''fator : IDENTIFIER
             | numero
             | LPAREN expressao_aritmetica RPAREN'''
    pass


def p_numero(p):
    '''numero : NUMERO_INTEIRO
              | NUMERO_REAL'''
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p:
        print(
            f"Erro sintático próximo ao token '{p.value}' na linha {p.lineno}")
    else:
        print("Erro sintático no final da entrada")


# Construção do Parser
parser = yacc.yacc()
