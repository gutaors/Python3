# decorador serve para adicionar alguma funcionalidade na função
#por exemplo, calcular quanto tempo demorou para rodar

def velocidade(funcao):
    def escrava(*args, **kwargs):
        return funcao(*args, **kwargs)
return escrava


@velocidade
def demora():
    for i in range(5):
        sleep(1)

