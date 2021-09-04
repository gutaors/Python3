# decorador serve para adicionar alguma funcionalidade na função
# por exemplo, calcular quanto tempo demorou para rodar
# vou mostrar um exemplo e um template logo abaixo
#  EXEMPLO

from time import time
from time import sleep


def velocidade(funcao):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(10000)


# TEMPLATE SIMPLES
def master(funcao):
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        return resultado
    # Retorna a função que envolve
    return envolve

@master
def outra(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
outra(10000)

#TEMPLATE ELABORADO

#from biblioteca_besta import funcao_besta

def mestredouniverso(funcao):
    """
    Função decoradora: coloca mais texto, verifica o tempo etc
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@mestredouniverso
def chama(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
chama(10000)