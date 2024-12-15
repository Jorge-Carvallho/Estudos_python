# Exercício 62
# Melhore o desafio 61 perguntano para o usuário se ela quer mostrar mais alguns termos.
# O programa encerra quandoele disser que quer mostrar 0 termo.

# print('''   Gerador de PA 
# -=-=-=-=-=-=-=-=-=-=''')



# termo = (int(input('Primerio termo: ')))
# razao = int(input('Razão da PA: '))
# quant_termos = int(input('Quantos termos você quer mostrar: '))

# c =0

# while c < quant_termos:
#     print(termo,end='')
#     if c < quant_termos -1:
#         print('->',end='')
        
#     termo += razao
#     c += 1
# quant_termos = str(input('\nQuer mostrar mais termos [S/N] ')).strip().upper()
# if quant_termos == 'S':
#     quant_termos = int(input('Quantos termos você quer mostrar mais: '))
#     quant_termos += c 
    

#     print('saindo')
    
# print(termo)

# --------------------------resolução--------------------------------------

print('Gerador de PA')
print('-='* 10)

primeiro = int(input('Primerio termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    while cont < 11 + total:
        print(termo,end='')
        print('->', end='')
        
        termo += razao
        cont += 1
    print(' PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    total += mais
        
print('Saindo')