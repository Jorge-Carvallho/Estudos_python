from random import randint

numeros = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(n,end=' ')
    print('Pronto!')
        
        
def soma_par(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {lista}, temos {soma}')
    

sorteia(numeros)

soma_par(numeros)
#  --------------------------------------------------------------------------------











