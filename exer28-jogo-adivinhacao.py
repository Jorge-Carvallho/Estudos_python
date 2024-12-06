# Exercício 28
# Escreva um programa que faça o computadpr "pensar" em um númerointerio entre 0 e 5
# e peça para o usuário testar descobrir qual o número escolhido pelo computador.
# O progrema deverá escrever na tela se o usuário venceu ou perdeu.


import random
from time import sleep
num_maquina = random.randint(0,5)
print('-=-'* 30)
num_maquina = print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-'* 30)

num_pensado = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')
sleep(0.5)
if num_pensado == num_maquina:
    print(f'Parebêns você venceu, eu tinha pensado no número {num_maquina} mesmo.')
else:
    print(f'Eu venci agora, pensei no número {num_maquina} e não no {num_pensado}.')


