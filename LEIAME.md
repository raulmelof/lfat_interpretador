# Projeto 2: Interpretador para a Linguagem BASIC

**Disciplina:** GRULFAT (Linguagens Formais e Autômatos )
**Professor:** [Alexandra Aparecida de Souza/Thiago Schumacher Barcelos]
**Data de Entrega:** 04/07/2025

---

## Integrantes da Equipe

* **Raul Melo Farias** - Prontuário: `GU3046923`
* **Gabriel Vinicius Santos Rosa** - Prontuário: `GU3046991`
* **Jonathan Zorzim Rodrigues** - Prontuário: `GU3046966`

---

## 1. Sobre o Projeto

Este projeto consiste na implementação de um interpretador para um subconjunto da linguagem de programação BASIC. O interpretador foi desenvolvido em **Python** utilizando a biblioteca **PLY (Python Lex-Yacc)** e é capaz de realizar análise léxica, sintática e semântica para executar programas escritos na gramática especificada.

O objetivo foi construir um pipeline completo, desde a leitura de um código-fonte em texto até a execução de suas instruções, como operações aritméticas, entrada/saída de dados e desvios condicionais.

---

## 2. Especificação da Linguagem

A versão da linguagem BASIC implementada suporta as seguintes funcionalidades:

## 3. Decisões de Projeto e Arquitetura

**Ferramentas Python e PLY**
Em vez da combinação tradicional de C com Flex/Bison, optamos por Python e a biblioteca PLY.
Justificativa: Esta escolha permitiu focar na lógica principal do projeto (a teoria de compiladores, gramáticas e interpretação) em vez de gastar tempo com a complexidade de gerenciamento de memória do C ou configuração de Makefiles. A sintaxe limpa do Python e a facilidade de uso de suas estruturas de dados, como dicionários, foram ideais para uma implementação rápida e robusta da tabela de símbolos e da árvore sintática.

**Arquitetura em Três Estágios**
O projeto foi modularizado em três componentes principais, seguindo o padrão clássico de compiladores:

    Analisador Léxico (lexer_basic.py): Responsável por ler o código-fonte e convertê-lo em uma sequência de tokens (palavras-chave, operadores, números, etc.).

    Analisador Sintático (parser_basic.py): Responsável por receber os tokens, validar se a sequência obedece à gramática (análise sintática) e, crucialmente, construir a Árvore Sintática Abstrata (AST).

    Interpretador (interpretador.py): Responsável por "caminhar" pela AST gerada pelo parser e executar as instruções (análise semântica).

Justificativa: Esta separação de responsabilidades torna o código mais limpo, organizado e fácil de depurar. Cada módulo cuida de uma única tarefa bem definida.

**Representação da Árvore Sintática Abstrata (AST)**
A AST, que é a estrutura de dados central do projeto, foi representada utilizando tuplas aninhadas do Python.
Exemplo: A expressão A = 10 + 5 é transformada na tupla ('atribuicao', 'A', ('+', ('numero', 10.0), ('numero', 5.0))).
Justificativa: Esta abordagem é leve e extremamente simples de implementar e depurar. O uso de tuplas imutáveis evita modificações acidentais na árvore após sua criação. Para um projeto deste escopo, criar uma hierarquia de classes para cada tipo de nó foi considerado um excesso de complexidade desnecessário.

**Tabela de Símbolos**
As variáveis da linguagem são armazenadas em uma Tabela de Símbolos global.
Implementação: Um simples dicionário Python (tabela_de_simbolos = {}).
Justificativa: Para uma linguagem como o BASIC, que não possui escopo de função ou aninhado, um dicionário global é a estrutura mais direta e eficiente para mapear nomes de variáveis aos seus valores.

## 4. Como Executar o Programa

**Pré-requisitos**
*Python 3.x instalado e configurado no PATH do sistema.
*A biblioteca PLY.

**Instalação da Dependência**
Para instalar o PLY, execute o seguinte comando no seu terminal:

    py -m pip install ply

    ou

    pip install ply

**Execução**
O programa é executado diretamente através do arquivo do parser, que orquestra a análise e a interpretação. Para rodar, navegue até a pasta do projeto e execute:

    py parser_basic.py

#### Funcionalidades Implementadas

* **Atribuição de Variáveis:** Permite atribuir valores numéricos a variáveis (ex: `A = 10`).
* **Entrada de Dados:** Captura dados numéricos do usuário através do comando `INPUT`.
* **Saída de Dados:** Imprime resultados de expressões ou valores de variáveis na tela com o comando `PRINT`.
* **Expressões Aritméticas:** Suporta as quatro operações básicas (`+`, `-`, `*`, `/`) com tratamento de precedência de operadores e uso de parênteses.
* **Números Negativos:** Permite o uso de números negativos (ex: `PRINT -1`).
* **Condicionais:** Implementa a estrutura `IF ... THEN ...` com operadores relacionais (`>`, `<`, `==`, `!=`, `>=`, `<=`).

#### Gramática (BNF)

A estrutura da linguagem foi definida pela seguinte gramática em Backus-Naur Form:

```bnf
program : statement_list

statement_list : statement
               | statement_list statement

statement : assign_statement
          | print_statement
          | if_statement
          | input_statement

assign_statement : ID IGUAL expression
print_statement  : PRINT expression
input_statement  : INPUT ID
if_statement     : IF condition THEN statement

condition : expression '>' expression
          | expression '<' expression
          | expression '==' expression
          | expression '!=' expression
          | expression '>=' expression
          | expression '<=' expression

expression : expression '+' term
           | expression '-' term
           | term

term : term '*' factor
     | term '/' factor
     | factor

factor : NUMERO
       | ID
       | '(' expression ')'
       | '-' factor