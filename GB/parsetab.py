
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDECHAR COMMA DIVIDE DIVIDE_EQUAL ELSE EQUAL EQUAL_EQUAL FLOAT GREATER GREATER_EQUAL IDENTIFIER IF INT LBRACE LBRACKET LESS LESS_EQUAL LPAREN MINUS MINUS_EQUAL NOT_EQUAL NUMERO_INTEIRO NUMERO_REAL PLUS PLUS_EQUAL RBRACE RBRACKET RPAREN SEMICOLON TIMES TIMES_EQUAL WHILEprograma : lista_declaracoes_comandoslista_declaracoes_comandos : declaracao_comando\n                                  | lista_declaracoes_comandos declaracao_comandodeclaracao_comando : declaracao\n                          | comandodeclaracao : tipo lista_variaveis SEMICOLONtipo : CHAR\n            | INT\n            | FLOATlista_variaveis : variavel\n                       | lista_variaveis COMMA variavelvariavel : IDENTIFIER\n                | IDENTIFIER LBRACKET NUMERO_INTEIRO RBRACKETcomando : comando_if\n               | comando_while\n               | comando_atribuicaocomando_if : IF LPAREN condicao RPAREN LBRACE lista_comandos RBRACE opcional_elseopcional_else : ELSE LBRACE lista_comandos RBRACE\n                     | emptycomando_while : WHILE LPAREN condicao RPAREN LBRACE lista_comandos RBRACElista_comandos : comando\n                      | lista_comandos comandocomando_atribuicao : IDENTIFIER operador_atribuicao expressao_aritmetica SEMICOLONoperador_atribuicao : EQUAL\n                           | PLUS_EQUAL\n                           | MINUS_EQUAL\n                           | TIMES_EQUAL\n                           | DIVIDE_EQUALcondicao : expressao_aritmetica operador_relacional expressao_aritmeticaoperador_relacional : EQUAL_EQUAL\n                           | NOT_EQUAL\n                           | LESS_EQUAL\n                           | GREATER_EQUAL\n                           | LESS\n                           | GREATERexpressao_aritmetica : expressao_aritmetica PLUS termo\n                            | expressao_aritmetica MINUS termo\n                            | termotermo : termo TIMES fator\n             | termo DIVIDE fator\n             | fatorfator : IDENTIFIER\n             | numero\n             | LPAREN expressao_aritmetica RPARENnumero : NUMERO_INTEIRO\n              | NUMERO_REALempty :'
    
_lr_action_items = {'CHAR':([0,2,3,4,5,7,8,9,16,28,58,71,73,74,76,79,],[10,10,-2,-4,-5,-14,-15,-16,-3,-6,-23,-47,-20,-17,-19,-18,]),'INT':([0,2,3,4,5,7,8,9,16,28,58,71,73,74,76,79,],[11,11,-2,-4,-5,-14,-15,-16,-3,-6,-23,-47,-20,-17,-19,-18,]),'FLOAT':([0,2,3,4,5,7,8,9,16,28,58,71,73,74,76,79,],[12,12,-2,-4,-5,-14,-15,-16,-3,-6,-23,-47,-20,-17,-19,-18,]),'IF':([0,2,3,4,5,7,8,9,16,28,58,61,67,68,69,70,71,72,73,74,76,77,78,79,],[13,13,-2,-4,-5,-14,-15,-16,-3,-6,-23,13,13,13,-21,13,-47,-22,-20,-17,-19,13,13,-18,]),'WHILE':([0,2,3,4,5,7,8,9,16,28,58,61,67,68,69,70,71,72,73,74,76,77,78,79,],[14,14,-2,-4,-5,-14,-15,-16,-3,-6,-23,14,14,14,-21,14,-47,-22,-20,-17,-19,14,14,-18,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,16,20,21,22,23,24,25,26,27,28,29,31,46,47,48,49,50,51,52,53,54,55,56,58,61,67,68,69,70,71,72,73,74,76,77,78,79,],[15,15,-2,-4,-5,19,-14,-15,-16,-7,-8,-9,-3,36,36,36,-24,-25,-26,-27,-28,-6,19,36,36,36,36,-30,-31,-32,-33,-34,-35,36,36,-23,15,15,15,-21,15,-47,-22,-20,-17,-19,15,15,-18,]),'$end':([1,2,3,4,5,7,8,9,16,28,58,71,73,74,76,79,],[0,-1,-2,-4,-5,-14,-15,-16,-3,-6,-23,-47,-20,-17,-19,-18,]),'RBRACE':([7,8,9,58,68,69,70,71,72,73,74,76,78,79,],[-14,-15,-16,-23,71,-21,73,-47,-22,-20,-17,-19,79,-18,]),'LPAREN':([13,14,20,21,22,23,24,25,26,27,31,46,47,48,49,50,51,52,53,54,55,56,],[20,21,31,31,31,-24,-25,-26,-27,-28,31,31,31,31,-30,-31,-32,-33,-34,-35,31,31,]),'EQUAL':([15,],[23,]),'PLUS_EQUAL':([15,],[24,]),'MINUS_EQUAL':([15,],[25,]),'TIMES_EQUAL':([15,],[26,]),'DIVIDE_EQUAL':([15,],[27,]),'SEMICOLON':([17,18,19,34,35,36,37,38,39,41,42,59,60,63,64,65,66,],[28,-10,-12,-38,-41,-42,-43,-45,-46,58,-11,-13,-44,-36,-37,-39,-40,]),'COMMA':([17,18,19,42,59,],[29,-10,-12,-11,-13,]),'LBRACKET':([19,],[30,]),'NUMERO_INTEIRO':([20,21,22,23,24,25,26,27,30,31,46,47,48,49,50,51,52,53,54,55,56,],[38,38,38,-24,-25,-26,-27,-28,43,38,38,38,38,-30,-31,-32,-33,-34,-35,38,38,]),'NUMERO_REAL':([20,21,22,23,24,25,26,27,31,46,47,48,49,50,51,52,53,54,55,56,],[39,39,39,-24,-25,-26,-27,-28,39,39,39,39,-30,-31,-32,-33,-34,-35,39,39,]),'RPAREN':([32,34,35,36,37,38,39,40,44,60,62,63,64,65,66,],[45,-38,-41,-42,-43,-45,-46,57,60,-44,-29,-36,-37,-39,-40,]),'PLUS':([33,34,35,36,37,38,39,41,44,60,62,63,64,65,66,],[47,-38,-41,-42,-43,-45,-46,47,47,-44,47,-36,-37,-39,-40,]),'MINUS':([33,34,35,36,37,38,39,41,44,60,62,63,64,65,66,],[48,-38,-41,-42,-43,-45,-46,48,48,-44,48,-36,-37,-39,-40,]),'EQUAL_EQUAL':([33,34,35,36,37,38,39,60,63,64,65,66,],[49,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'NOT_EQUAL':([33,34,35,36,37,38,39,60,63,64,65,66,],[50,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'LESS_EQUAL':([33,34,35,36,37,38,39,60,63,64,65,66,],[51,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'GREATER_EQUAL':([33,34,35,36,37,38,39,60,63,64,65,66,],[52,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'LESS':([33,34,35,36,37,38,39,60,63,64,65,66,],[53,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'GREATER':([33,34,35,36,37,38,39,60,63,64,65,66,],[54,-38,-41,-42,-43,-45,-46,-44,-36,-37,-39,-40,]),'TIMES':([34,35,36,37,38,39,60,63,64,65,66,],[55,-41,-42,-43,-45,-46,-44,55,55,-39,-40,]),'DIVIDE':([34,35,36,37,38,39,60,63,64,65,66,],[56,-41,-42,-43,-45,-46,-44,56,56,-39,-40,]),'RBRACKET':([43,],[59,]),'LBRACE':([45,57,75,],[61,67,77,]),'ELSE':([71,],[75,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes_comandos':([0,],[2,]),'declaracao_comando':([0,2,],[3,16,]),'declaracao':([0,2,],[4,4,]),'comando':([0,2,61,67,68,70,77,78,],[5,5,69,69,72,72,69,72,]),'tipo':([0,2,],[6,6,]),'comando_if':([0,2,61,67,68,70,77,78,],[7,7,7,7,7,7,7,7,]),'comando_while':([0,2,61,67,68,70,77,78,],[8,8,8,8,8,8,8,8,]),'comando_atribuicao':([0,2,61,67,68,70,77,78,],[9,9,9,9,9,9,9,9,]),'lista_variaveis':([6,],[17,]),'variavel':([6,29,],[18,42,]),'operador_atribuicao':([15,],[22,]),'condicao':([20,21,],[32,40,]),'expressao_aritmetica':([20,21,22,31,46,],[33,33,41,44,62,]),'termo':([20,21,22,31,46,47,48,],[34,34,34,34,34,63,64,]),'fator':([20,21,22,31,46,47,48,55,56,],[35,35,35,35,35,35,35,65,66,]),'numero':([20,21,22,31,46,47,48,55,56,],[37,37,37,37,37,37,37,37,37,]),'operador_relacional':([33,],[46,]),'lista_comandos':([61,67,77,],[68,70,78,]),'opcional_else':([71,],[74,]),'empty':([71,],[76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes_comandos','programa',1,'p_programa','parser.py',14),
  ('lista_declaracoes_comandos -> declaracao_comando','lista_declaracoes_comandos',1,'p_lista_declaracoes_comandos','parser.py',19),
  ('lista_declaracoes_comandos -> lista_declaracoes_comandos declaracao_comando','lista_declaracoes_comandos',2,'p_lista_declaracoes_comandos','parser.py',20),
  ('declaracao_comando -> declaracao','declaracao_comando',1,'p_declaracao_comando','parser.py',25),
  ('declaracao_comando -> comando','declaracao_comando',1,'p_declaracao_comando','parser.py',26),
  ('declaracao -> tipo lista_variaveis SEMICOLON','declaracao',3,'p_declaracao','parser.py',31),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',36),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',37),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',38),
  ('lista_variaveis -> variavel','lista_variaveis',1,'p_lista_variaveis','parser.py',43),
  ('lista_variaveis -> lista_variaveis COMMA variavel','lista_variaveis',3,'p_lista_variaveis','parser.py',44),
  ('variavel -> IDENTIFIER','variavel',1,'p_variavel','parser.py',49),
  ('variavel -> IDENTIFIER LBRACKET NUMERO_INTEIRO RBRACKET','variavel',4,'p_variavel','parser.py',50),
  ('comando -> comando_if','comando',1,'p_comando','parser.py',55),
  ('comando -> comando_while','comando',1,'p_comando','parser.py',56),
  ('comando -> comando_atribuicao','comando',1,'p_comando','parser.py',57),
  ('comando_if -> IF LPAREN condicao RPAREN LBRACE lista_comandos RBRACE opcional_else','comando_if',8,'p_comando_if','parser.py',62),
  ('opcional_else -> ELSE LBRACE lista_comandos RBRACE','opcional_else',4,'p_opcional_else','parser.py',67),
  ('opcional_else -> empty','opcional_else',1,'p_opcional_else','parser.py',68),
  ('comando_while -> WHILE LPAREN condicao RPAREN LBRACE lista_comandos RBRACE','comando_while',7,'p_comando_while','parser.py',73),
  ('lista_comandos -> comando','lista_comandos',1,'p_lista_comandos','parser.py',78),
  ('lista_comandos -> lista_comandos comando','lista_comandos',2,'p_lista_comandos','parser.py',79),
  ('comando_atribuicao -> IDENTIFIER operador_atribuicao expressao_aritmetica SEMICOLON','comando_atribuicao',4,'p_comando_atribuicao','parser.py',84),
  ('operador_atribuicao -> EQUAL','operador_atribuicao',1,'p_operador_atribuicao','parser.py',89),
  ('operador_atribuicao -> PLUS_EQUAL','operador_atribuicao',1,'p_operador_atribuicao','parser.py',90),
  ('operador_atribuicao -> MINUS_EQUAL','operador_atribuicao',1,'p_operador_atribuicao','parser.py',91),
  ('operador_atribuicao -> TIMES_EQUAL','operador_atribuicao',1,'p_operador_atribuicao','parser.py',92),
  ('operador_atribuicao -> DIVIDE_EQUAL','operador_atribuicao',1,'p_operador_atribuicao','parser.py',93),
  ('condicao -> expressao_aritmetica operador_relacional expressao_aritmetica','condicao',3,'p_condicao','parser.py',98),
  ('operador_relacional -> EQUAL_EQUAL','operador_relacional',1,'p_operador_relacional','parser.py',103),
  ('operador_relacional -> NOT_EQUAL','operador_relacional',1,'p_operador_relacional','parser.py',104),
  ('operador_relacional -> LESS_EQUAL','operador_relacional',1,'p_operador_relacional','parser.py',105),
  ('operador_relacional -> GREATER_EQUAL','operador_relacional',1,'p_operador_relacional','parser.py',106),
  ('operador_relacional -> LESS','operador_relacional',1,'p_operador_relacional','parser.py',107),
  ('operador_relacional -> GREATER','operador_relacional',1,'p_operador_relacional','parser.py',108),
  ('expressao_aritmetica -> expressao_aritmetica PLUS termo','expressao_aritmetica',3,'p_expressao_aritmetica','parser.py',113),
  ('expressao_aritmetica -> expressao_aritmetica MINUS termo','expressao_aritmetica',3,'p_expressao_aritmetica','parser.py',114),
  ('expressao_aritmetica -> termo','expressao_aritmetica',1,'p_expressao_aritmetica','parser.py',115),
  ('termo -> termo TIMES fator','termo',3,'p_termo','parser.py',120),
  ('termo -> termo DIVIDE fator','termo',3,'p_termo','parser.py',121),
  ('termo -> fator','termo',1,'p_termo','parser.py',122),
  ('fator -> IDENTIFIER','fator',1,'p_fator','parser.py',127),
  ('fator -> numero','fator',1,'p_fator','parser.py',128),
  ('fator -> LPAREN expressao_aritmetica RPAREN','fator',3,'p_fator','parser.py',129),
  ('numero -> NUMERO_INTEIRO','numero',1,'p_numero','parser.py',134),
  ('numero -> NUMERO_REAL','numero',1,'p_numero','parser.py',135),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',140),
]
