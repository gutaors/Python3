
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
lista.sort()
print(lista)

def func(item):
    return item[1]

lista.sort(key=func)
print (lista)

#usando funcao lambda
lista.sort(key=lambda item: item[1], reverse=True)
print (lista)