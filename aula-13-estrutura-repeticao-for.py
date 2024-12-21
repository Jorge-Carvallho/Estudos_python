# Estrutura de repetição FOR (Variavel de Controle)



# # loop segue em frente
# for c in range(0,10):#mostrara de 0 ate 10
#     print('Vamos la')  # dentro do for, de 0, 10 vai repetir 10 vezes
# print('FIM')# fora do for (froa da contagem)

# -------------------------------------------------------------------------------

# loop segue de frente pra trás

for c in range(10,0,-1): # ele mostrara de 10 ate 0 de 
# lembre que o ultimo ele não mosytra caso não começe pelo 0, digamos que fosse 1 até 10,
# mostrarar --> 1 ate 9
    
    print(c)
print('Fim')

# -----------------------------------------------------------------------------------


# n = int(input('Digite um número: '))

# for c in range(0,n+1): # digamos que o usuario coloque 9, ele mostra até 8 
# # por isso adicionei n+1 a frente do n pra mostrar ele mesmo
#     print(c)
# print('Fim')

        
# -------------------------------- ou ------------------------------------------------
                            
# inicio = int(input('Digite o inicio: '))
# fim = int(input('Digite o fim: '))
# passo = int(input('Digite o passo: '))

# for c in range(inicio,fim+1,passo):
#     print(c)
# print('Fim')

# -----------------------------------ou-------------------------------------------------
soma  = 0
for c in range(0, 4):
    n= int(input('Digite um valor: '))
    soma += n
    print(n)
print(f' A soma dos números foram {soma}')
from random import randint, choice,choices, sample

# randint() é usado para classificar um único número inteiro em um intervalo.
sorteia = randint(0,1) #--> retorna um número sorteado


# choice() sorteia um único item aleatório de uma sequência.
lista = [0,1,2,3,4,5,6]
sorteia = choice(lista)


# choices() permite classificar vários itens com possibilidade de reprodução .
lista = [0,1,2,3,4,5,63,4,7,3,5]
sorteia = choices(range(0,5),k=5)

