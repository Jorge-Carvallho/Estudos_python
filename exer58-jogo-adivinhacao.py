# Exercício 58
# Melhore o jogo do DESAFIO 28 onde o computadpr vai pensar eme um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acerta, mostrando
# no final quantos palpites foram necessários para vencer


# from time import sleep
# from random import randint

# num_maquina = randint(0,2)
# cont = 1
# print('-=-' * 25)
# print(f'{"Sou seu computador":^60}')
# print(f'{"Acabei de pensar em um número entre 0 e 10":^60}')
# print(f'{"Será que consegue adivinhar qual":^60}')
# print('-=-' * 25)

# pensei = int(input('Qual é seu palpite: '))
# print('Processando ....')
# sleep(0.9)
# while pensei != num_maquina:
#     print('Você errou')
#     if pensei > num_maquina:
#         print('Menos.. tente novamente')
#     elif num_maquina > pensei:
#         print('Mais.. tente novamente')
#     pensei = int(input('Qual é seu palpite novamente: '))
#     print('Processando ....')
#     sleep(0.9)
#     cont += 1
    
    
# print('Acertou')
# print(f'Foi necessário {cont} tentativas  para acertar')
    
    
# ----------------------------------------------------------------------


from random import randint

computador  = randint(0,10)
print('Sou seu computador... Acabeide pensar em um número de 1 até 10.!')
print('Sera que você consegue adivinhar qual foi?')
acertou =  False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites +=1
    if jogador == computador:
        acertou = True
    elif jogador > computador:
        print('Menos um pouco')
    elif jogador < computador:
        print('Mais um pouco')
        
print('Acertou!!')
print(f'Você tentou {palpites} vezes até acerta.')









    
