
# remove todos caracteres qeu não são números de uma expressão recebida
# importa regular expressions

import re
def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

cnpj = '213ads1f231asdf32qewrt45qet4qret654wer///'
cnpj = apenas_numeros(cnpj)
print (cnpj)