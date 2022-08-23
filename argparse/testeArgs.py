# programa que recebe largura e área de terreno e calcula a área
#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Calcular a área de um terreno')
# Adicionar os argumentos, serão posicionais, têm que ser fornecidos na ordem
parser.add_argument('largura',type=int, help='Largura do Terreno')
parser.add_argument('comprimento',type=int, help='Comprimento do Terreno')

args = parser.parse_args()
def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area

if __name__=='__main__':
    print(" A área do terreno é de %s m2" %calcula_area(args.largura, args.comprimento))

# para usar digite no terminal: python3 testeArgs.py 10 15