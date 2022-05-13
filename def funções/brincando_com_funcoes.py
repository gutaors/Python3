# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# faça um código que diga <br>
# <ul> número é divisível por 3, <br>
# ou por 5 <br>
# ou por ambos <br>
# ou por nenhum dos dois<br>

def verifica(numero):
    if numero % 3 == 0:
        return 'divisível por 3'
    elif numero % 5 == 0:
        return 'divisível por 5'
    elif numero % 3 == 0 and numero % 5 == 0:
        return 'divisível por ambos'
    else:
        return f'{numero} não é divisível '
print(verifica(45634))


def verifica(numero):
    if numero % 3 == 0:
        return f'{numero} divisível por 3'
    elif numero % 5 == 0:
        return f'{numero} divisível por 5'
    elif numero % 3 == 0 and numero % 5 == 0:
        return f'{numero} divisível por ambos'
    return f'{numero} não é divisível '
print(verifica(45634))

print(verifica(45634435))

for random import randint


def func(*args):
    print (args)
func (1, 3, 5, 9)

lista = [1, 2, 3,  4, 5, 6]
n1, n2, *n, n6 = lista
print (n)

# o * desempacota os itens da lista
print(*lista, sep='-')



