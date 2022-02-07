# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
# -

chaves

dados

# ## LENDO COM ITERACAO EXPLÍCITA

# com cabeçalho
import csv
with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    #note que como tem iteração, o for tem que está dentro do next
    for dado in dados:
        print(dado)

# sem cabeçalho, coloca next
import csv
with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)
    #note que como tem iteração, o for tem que está dentro do next
    for dado in dados:
        print(dado)

#LENDO NNORMAL
import csv
with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)
    #note que como tem iteração, o for tem que está dentro do next
    for dado in dados:
        print(dado)

# ## LENDO COM ITERACAO IMPLÍCITA

#LENDO NNORMAL
import csv
with open('clientes.csv', 'r') as arquivo:
# O x for x aqui embaixo é list comprehension
    dados = [x for x in csv.reader(arquivo)]
for dado in dados:
    print(dado)

#LENDO COMO DICIONARIO 
import csv
with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]
for dado in dados:
    print(dado)


