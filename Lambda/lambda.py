#aula 60

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