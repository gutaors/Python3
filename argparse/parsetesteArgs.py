# programa que recebe largura e área de terreno e calcula a área
#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Calcular a área de um terreno')
# Adicionar os argumentos, aqui não serão posicionais, por causa do -l e -c abaixo, não têm que ser fornecidos na ordem
#as palavras largura e comprimento também podem ser usadas por causa do --
parser.add_argument('-l','--largura',type=int, help='Largura do Terreno')
parser.add_argument('-c','--comprimento',type=int, help='Comprimento do Terreno')

args = parser.parse_args()
def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area

if __name__=='__main__':
    print(" A área do terreno é de %s m2" %calcula_area(args.largura, args.comprimento))

# para usar digite no terminal: python3 parsetesteArgs.py -l 10 -c 15
# ou python3 parsetesteArgs.py --largura 10 --comprimento 15