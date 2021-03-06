
# O que esta bagaça faz?
# Remove os pontos e barras do cnpj, 
# verifica se não é uma sequencia de números iguais
# calcula os dítigos verificadores

import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    # se primeiro d
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
        # acima o cnpj é ele mesmo sem os dois digitos finais
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    # enumerate é comando python q pega o regressivos e separa em itens
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
        # pegou cada algarismo do cnpj, multiplicou pelo algarismo 
        # correspondente no regressivo e depois somou os resultados
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

# eh sequencia valida se o cnpj não é uma sequencia 
# de algarismos iguais
# para isto ele pega o primeiro caracter e repete 13 vezes
# por exemplo 1111111111111
def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
