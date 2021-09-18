#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=O9vhwaQAuHU
# https://pythonacademy.com.br/blog/domine-decorators-em-pythonhttps://www.youtube.com/watch?v=O9vhwaQAuHU

# ### 1 - EMBUTINDO F DENTRO DE F1 DO JEITO TRADICIONAL: primeiro entender esta logica aqui:

# In[24]:


#funcao que vai ter a outra embutida - vai decorar (abraçar) e executar a outra
def f1(func):
    def wrapper():
        print('inicio')
        func()
        print('final')
#este () aqui embaixo só é necessario para botar a função f dentro da função f1
    return wrapper()
#funcao que vai ser abraçada - decorada
def f():
    print('ola')
    
#print(f1(f))
#executa sem decorar
f()


# #agora vou botar f dentro de f1

# In[23]:


# para isto aqui funcionar eu preciso ir lá na f1 e no  no return wrapper e colocar ()
f1(f)


# ### 2- EMBUTINDO F DENTRO DE F1 COM DECORATOR

# In[13]:


#funcao que vai ter a outra embutida - vai decorar (abraçar) e executar a outra
def f1(func):
    def wrapper():
        print('inicio')
        func()
        print('final')

    return wrapper
#basta colocar arroba e nome da função que quero decorar (que vai receber a outra dentro dela)

@f1
#funcao que vai ser abraçada - decorada
def f():
    print('ola')
    
#print(f1(f))
#executa de forma decorada
f()


# ### 3- EMBUTINDO F DENTRO DE F1 COM DECORATOR E PASSANDO ARGUMENTOS

# In[29]:


#funcao que vai ter a outra embutida - vai decorar (abraçar) e executar a outra
def f1(func):
    #aqui na wrapper(empacotadora coloco args e kwargs * e **)
    def wrapper(*args,**kwargs):
        print('inicio')
        #não é so na wrapper, lembre se que aqui na func(funcao) também coloco args e kwargs * e **
        func(*args,**kwargs)
        print('final')

    return wrapper
#basta colocar arroba e nome da função que quero decorar (que vai receber a outra dentro dela)
@f1
#funcao que vai ser abraçada - decorada
#veja que desta vez coloco argumento nome
def f(nome,gentileza):
    #quarta alteração desta vez, colocar nome no print
    print('ola '+nome+gentileza)
    
#print(f1(f))
#executa de forma decorada
f("gustavo"," tudo bem?")


# ### 4-CALCULANDO TEMPO DE EXECUCAO

# In[30]:


import time

# Define nosso decorator
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# Decora a função com o decorator
@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

# Executa a função main
main()


# In[ ]:




