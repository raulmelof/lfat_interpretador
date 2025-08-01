# Interpretador BASIC em Python

![Linguagem](https://img.shields.io/badge/Python-3.x-blue.svg)
![Biblioteca](https://img.shields.io/badge/Biblioteca-PLY-yellow.svg)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)

Um interpretador funcional para um subconjunto da linguagem de programação BASIC, desenvolvido como projeto para a disciplina de **Gramáticas, Linguagens Formais e Autômatos (GRULFAT)**. O projeto abrange todo o pipeline de interpretação de uma linguagem, desde a análise de código-fonte em texto até a execução de suas instruções.

---

## ✨ Funcionalidades

A versão da linguagem BASIC implementada suporta:

* **Atribuição de Variáveis:** `VAR = EXPRESSAO`
* **Expressões Aritméticas:** Suporte para `+`, `-`, `*`, `/` com tratamento de precedência e parênteses.
* **Números Unários:** Tratamento de números negativos (ex: `-10`).
* **Comandos de I/O:** `PRINT` para saída de dados e `INPUT` para entrada interativa.
* **Estruturas Condicionais:** `IF ... THEN` com operadores relacionais (`>`, `<`, `==`, `!=`, `>=`, `<=`).
* **Laços de Repetição:** Estrutura `FOR I = <início> TO <fim> ... NEXT I` para loops definidos.

---

## 🏗️ Arquitetura

O interpretador foi projetado com uma arquitetura modular clássica de três estágios, facilitando o desenvolvimento, depuração e extensibilidade.

`Código Fonte (.bas)` -> **[ Lexer ]** -> `Fluxo de Tokens` -> **[ Parser ]** -> `Árvore Sintática Abstrata (AST)` -> **[ Interpretador ]** -> `Saída no Console`

1.  **Analisador Léxico (`lexer_basic.py`):** Utiliza expressões regulares para converter o código-fonte em um fluxo de *tokens* (números, palavras-chave, operadores, etc.).

2.  **Analisador Sintático (`parser_basic.py`):** Valida a sequência de tokens com base em uma gramática LALR(1) e constrói uma **Árvore Sintática Abstrata (AST)** que representa a estrutura lógica do programa. A AST é representada por tuplas aninhadas para simplicidade e eficiência.

3.  **Interpretador (`interpretador.py`):** Percorre a AST de forma recursiva ("AST Walker"). Para cada nó na árvore, ele executa a ação semântica correspondente, seja realizar um cálculo, modificar a tabela de símbolos, ou interagir com o console. A **Tabela de Símbolos**, que armazena as variáveis, é implementada com um dicionário Python.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Biblioteca Principal:** [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/ply.html) - Uma biblioteca Python que implementa as tradicionais ferramentas de análise léxica (Lex) e sintática (Yacc).

---

## 🚀 Como Executar

**1. Pré-requisitos:**
   - Ter o [Python 3](https://www.python.org/downloads/) instalado.

**2. Clone o Repositório:**
   ```bash
   git clone [URL_DO_SEU_REPOSITORIO_AQUI]
   cd [NOME_DA_PASTA_DO_PROJETO]
