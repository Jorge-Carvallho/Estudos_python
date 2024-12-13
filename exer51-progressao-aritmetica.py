# Exercício 51
# Desenvolva um programa que leia o primerio termo e a razâo de uma PA
# No final mostre os 10 primerios termos dessa prograssâo.




print('='* 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('='* 30)

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a RAZÂO: ')) 
cont = 0
print(termo, end=' --> ')
for c in range(0,10):
    termo += razao
    cont +=1
    print(f'{termo}',end=' --> ')
print('Acabou')

    
   