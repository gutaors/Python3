# decorador serve para adicionar alguma funcionalidade na função
# por exemplo, calcular quanto tempo demorou para rodar

def velocidade(funcao):
    def escrava(*args, **kwargs):
        return funcao(*args, **kwargs)
    return escrava



@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(10000)
