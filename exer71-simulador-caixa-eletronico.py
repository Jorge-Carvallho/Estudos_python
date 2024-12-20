# Exercício 71
# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio pergunte ao usuário qual sera o valor a ser sacado número inteiros
# e o programa  vai informa quantas cédulas de cada valor serão entregues.

# OBS: Considere que o caixa possui Cédulas de 50,20,10,1 real.




# valor = int(input('Qaul o valor voce quer sacar: '))
# total = valor
# ced = 50
# totalced = 0
# while True:
#     if total >=  ced:
#         total -= ced
#         totalced += 1 
#     else:
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de {ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totalced = 0
#         if total == 0:
#             break
        
        # -------------------------------------resolução -------------------------------
        
# valor = int(input('Qual valor quer sacar: '))
# total = valor
# ced = 50
# totalced = 0
# while True:
#     if  total >= ced:
#         total -= ced
#         totalced += 1
#     else: 
#         if totalced > 0:
#             print(f'total de cedulas {totalced}  celdulas de {ced}')
#         if ced == 50:
#             ced = 20
#         elif  ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totalced = 0
#         if total == 0:
#             break



valor = int(input('Qual o valor quer sacar: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f' Foram {totalced} cédulas  de {ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10: 
            ced = 1
        totalced = 0
        if total == 0:
            break
        
        












