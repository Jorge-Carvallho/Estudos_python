from time import sleep
from random import randint
print('''Suas opcões:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogada_usuario = int(input('Qual a sua jogada: '))
computador = int(randint(0,2))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

if jogada_usuario == 0 and computador == 2 :
    print('Usuario ganhou!!')
    
elif jogada_usuario == 2 and computador == 1:
    print('Usuario ganhou!!')

elif jogada_usuario == 1 and computador == 0:
    print('Usuário ganhou!!')
    
elif jogada_usuario == computador:
    print('Empate')

else:
    print('Computador ganhou!!')
    
    
    
    