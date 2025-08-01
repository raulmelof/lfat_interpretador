import ply.yacc as yacc
from lexer import tokens
from interpretador import executa_programa

precedence = (
    ('left', 'MAIS', 'MENOS'),
    ('left', 'VEZES', 'DIVIDIR'),
    ('right', 'UMENOS'),
)

# --- regras da gramatica (tradução do BNF para funções python) ---

def p_program(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assign_statement
                 | print_statement
                 | if_statement
                 | input_statement
                 | for_statement'''
    p[0] = p[1]

def p_assign_statement(p):
    'assign_statement : ID IGUAL expression'
    p[0] = ('atribuicao', p[1], p[3])

def p_print_statement(p):
    'print_statement : PRINT expression'
    p[0] = ('print', p[2])

def p_input_statement(p):
    'input_statement : INPUT ID'
    p[0] = ('input', p[2])

def p_if_statement(p):
    'if_statement : IF condition THEN statement'
    p[0] = ('if', p[2], p[4])

def p_for_statement(p):
    'for_statement : FOR ID IGUAL expression TO expression statement_list NEXT ID'
    if p[2] != p[9]:
        print(f"Erro de sintaxe: A variável no NEXT ('{p[9]}') não corresponde à variável do FOR ('{p[2]}').")
        p[0] = None
    else:
        p[0] = ('for', p[2], p[4], p[6], p[7])

def p_condition(p):
    '''condition : expression MAIOR_QUE expression
                 | expression MENOR_QUE expression
                 | expression IGUAL IGUAL expression
                 | expression DIFERENTE expression
                 | expression MAIOR_IGUAL expression
                 | expression MENOR_IGUAL expression'''
    if p[2] == '=' and p[3] == '=':
        p[0] = ('==', p[1], p[4])
    else:
        p[0] = (p[2], p[1], p[3])

# --- regras para expressões matemáticas (com hierarquia) ---

def p_expression_binop(p):
    '''expression : expression MAIS term
                  | expression MENOS term'''
    p[0] = (p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term VEZES factor
            | term DIVIDIR factor'''
    p[0] = (p[2], p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor(p):
    '''factor : NUMERO
              | ID
              | PARENTESE_ESQ expression PARENTESE_DIR'''
    if len(p) == 2:
        if isinstance(p[1], float):
            p[0] = ('numero', p[1])
        else:
            p[0] = ('id', p[1])
    else:
        p[0] = p[2]

def p_factor_umenus(p):
    'factor : MENOS factor %prec UMENOS'
    p[0] = ('umenos', p[2])

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe: fim inesperado do arquivo!")

parser = yacc.yacc()

# --- seção para testar o interpretador ---
if __name__ == '__main__':
    codigo_final = """
    PRINT 5 * 10
    
    INPUT VALOR
    
    IF VALOR > 50 THEN
        PRINT 1
    
    IF VALOR == 50 THEN
        PRINT 0
        
    IF VALOR < 50 THEN
        PRINT -1

    FOR I = 1 TO 10
        PRINT I
        A = I * 10
        PRINT A
    NEXT I
    """

    print("--- INÍCIO DA EXECUÇÃO DO PROGRAMA ---")
    arvore = parser.parse(codigo_final)
    if arvore:
        executa_programa(arvore)
    print("--- FIM DA EXECUÇÃO DO PROGRAMA ---")