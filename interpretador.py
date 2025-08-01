tabela_de_simbolos = {}

def executa_no(no):
    if no is None:
        return

    tipo_no = no[0]

    if tipo_no == 'numero':
        return no[1]
    
    elif tipo_no == 'id':
        try:
            return tabela_de_simbolos[no[1]]
        except KeyError:
            print(f"Erro: Variável '{no[1]}' não definida.")
            return 0

    elif tipo_no in ['>', '<', '==', '!=', '>=', '<=']:
        resultado_esq = executa_no(no[1])
        resultado_dir = executa_no(no[2])
        if tipo_no == '>': return resultado_esq > resultado_dir
        if tipo_no == '<': return resultado_esq < resultado_dir
        if tipo_no == '==': return resultado_esq == resultado_dir
        if tipo_no == '!=': return resultado_esq != resultado_dir
        if tipo_no == '>=': return resultado_esq >= resultado_dir
        if tipo_no == '<=': return resultado_esq <= resultado_dir
    
    elif tipo_no == 'if':
        condicao = executa_no(no[1])
        if condicao:
            return executa_no(no[2])
        return None
    
    elif tipo_no == 'for':
        var_loop = no[1]
        
        val_inicio = executa_no(no[2])
        val_fim = executa_no(no[3])
        corpo_do_loop = no[4]

        for i in range(int(val_inicio), int(val_fim) + 1):
            tabela_de_simbolos[var_loop] = float(i)

            for comando in corpo_do_loop:
                executa_no(comando)
        return None

    elif tipo_no == 'umenos':
        return -executa_no(no[1])
    
    elif tipo_no in ['+', '-', '*', '/']:
        resultado_esq = executa_no(no[1])
        resultado_dir = executa_no(no[2])
        if tipo_no == '+': return resultado_esq + resultado_dir
        if tipo_no == '-': return resultado_esq - resultado_dir
        if tipo_no == '*': return resultado_esq * resultado_dir
        if tipo_no == '/':
            if resultado_dir == 0:
                print("Erro: Divisão por zero.")
                return 0
            return resultado_esq / resultado_dir
    
    elif tipo_no == 'atribuicao':
        nome_variavel = no[1]
        valor_expressao = executa_no(no[2])
        tabela_de_simbolos[nome_variavel] = valor_expressao
        return None

    elif tipo_no == 'print':
        valor = executa_no(no[1])
        print(valor)
        return None

    elif tipo_no == 'input':
        nome_variavel = no[1]
        try:
            valor_usuario = input(f'{nome_variavel}? ')
            valor_numerico = float(valor_usuario)
            tabela_de_simbolos[nome_variavel] = valor_numerico
        except ValueError:
            print(f"Entrada inválida. Por favor, digite um número.")
            tabela_de_simbolos[nome_variavel] = 0
        return None

def executa_programa(arvore):
    for no_statement in arvore:
        executa_no(no_statement)