
# remove todos caracteres qeu não são números de uma expressão recebida
def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)