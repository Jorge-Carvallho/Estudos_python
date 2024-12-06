# Exercício 32
# Faca um programa que leia um ano qualuqer
# e mostre se ele é bissexto

# import datetime

# ano = int(input('Digite um ano ou 0 para verificar o ano atual: '))

# if ano == 0:
#     ano = datetime.datetime.now().year
    
# if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
#     print(f' O ano {ano} é Bissexto')
# elif  ano % 4 == 0  and ano % 100 != 0:
#     print(f'O ano {ano} é Bissexto')
# else:
#     print(f'O ano {ano} não é Bissexto')

    

#        --------------resolução---------------


from datetime import date

ano = int(input('Qual ano você quer analisar, coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISEXTO.')
else:
    print(f'O ano {ano} NÃO É BISEXTO.')