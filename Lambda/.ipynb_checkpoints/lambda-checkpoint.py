# aula 60
#
# Lambdas são funções sem nomes
#

def funcao(arg, arg2):
    return arg*arg2

var=funcao(2,2)

#escrevendo a mesma função no formato lambda
# tambem conhecida como anonima, pois ela não tem nome
a=lambda x,y: x * y
print(a(2,2))

#então vamos criar uma lista
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
#se rodarmos o sort ele ordena pela primeira chave
lista.sort()
print(lista)

#agora vamos criar uma funcao que permite ordenar por outra chave
def func(item):
    return item[1]

lista.sort(key=func)
print (lista)

#usando funcao lambda
lista.sort(key=lambda item: item[1], reverse=True)
print (lista)



lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista,key=lambda i: i[1], reverse=True))

# ## Outro Exemplo

# +
lambda x:3*x+1

#equivale a 

def funcao(x):
    return 3*x+1
# explicando
# lambda parametro:return

# para usar podemos atribuir a uma variável
calc = lambda x:3*x+1

calc(3)
# -

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

nome_completo('  ANGElina    ', '       jolie')

# ## Usando da forma que se deve usar as funções lambda
# ### ordenar uma lista pegando os sobrenomes

autores = ['isaac asimov', 'ray bradbury', 'robert heinlein', 'arthur c. clarke'
           , 'frank herbert', 'orson scott card', 'douglas adams'
           , 'h. g. wells', 'leigh brackett']


autores.sort(key=lambda sobrenome:sobrenome.split(' ')[-1].lower())
print(autores)


# ## lambda dentro de um def
#

def geradora_funcao_quadratica (a, b, c):
    """retorna a função f(x) = a*x**2 + b*x + c"""
    return lambda x: a* x ** 2 + b * x + c


# aqui passo valores para a, b, c
teste = geradora_funcao_quadratica(2, 3, -5)

# aqui executo passando valor de x
print(teste(0))
print(teste(1))
print(teste(2))

# podemos fazer direto, sem o teste que gera a lambda e depois a chamada dela
# AQUI EMBAIXO JÁ PASSO VALORES PARA a, b, c  depois x
print(geradora_funcao_quadratica(2, 3, -5)(2))



