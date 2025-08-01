import ply.lex as lex

palavras_reservadas = {
    'PRINT': 'PRINT',
    'INPUT': 'INPUT',
    'IF'   : 'IF',
    'THEN' : 'THEN',
    'FOR'  : 'FOR',
    'TO'   : 'TO',
    'NEXT' : 'NEXT'
}

tokens = [
    'NUMERO',
    'MAIS',
    'MENOS',
    'VEZES',
    'DIVIDIR',
    'IGUAL',
    'PARENTESE_ESQ',
    'PARENTESE_DIR',
    'MAIOR_QUE',
    'MENOR_QUE',
    'MAIOR_IGUAL',
    'MENOR_IGUAL',
    'DIFERENTE',
    'ID'
] + list(palavras_reservadas.values())

t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r'='
t_PARENTESE_ESQ = r'\('
t_PARENTESE_DIR = r'\)'
t_MAIOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_DIFERENTE = r'!='

t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_reservadas.get(t.value.upper(), 'ID')
    return t

def t_nova_linha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

    
lexer = lex.lex()

if __name__ == '__main__':
    codigo_teste = """
    A = 10.5
    B = 20
    IF A > B THEN
        PRINT A + B
    """

    lexer.input(codigo_teste)

    print("--- INÍCIO DA ANÁLISE LÉXICA ---")
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
    print("--- FIM DA ANÁLISE LÉXICA ---")