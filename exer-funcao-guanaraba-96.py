#Exercício ------------------- ---------------- -----
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um tereno e retangular (largura e comprimento) e mostre a área do terreno
from time import sleep
def exercicio():
    print('    Controle de Terrenos')


def linha():
    print('--------------------------------')
    

def area():
    largura = float(input('Digite a largura (m):'))
    comprimento = float(input('Digite o comprimento (m):'))
    area = largura * comprimento
    sleep(0.9)
    print(f'A área do terreno é {area:.2f} metros quadrados com largura de {largura} e comprimento de {comprimento}')

    
exercicio()
linha()
area()

    