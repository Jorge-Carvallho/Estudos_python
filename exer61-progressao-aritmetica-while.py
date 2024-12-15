# Exercício 61
# Refaça odesafio 051, lendo p primerio termo e a razão de um PA
# mostrando os 10 primerios termos da progressão usando a estrutura while



termo = int(input('Digite o primerio termo: '))
razao = int(input('Digite sua razaõ '))

cont = 0


while cont < 9:
    print(termo,end='')
    if cont < 9:
        print('->',end='')

    termo += razao
    cont += 1 
print(termo)
 










