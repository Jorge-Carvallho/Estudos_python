# Exercício 57
# Faça um programa que leia o sexo de uma pessoa.
# mas so aceite os valores (M) ou (F).
# Caso esteja errado, peça a digitação novamente ate ter um valor correto.


# sexo = ''
# # feminino = masculino = 0

# while sexo != 'M' and sexo != 'F':
#     sexo= str(input('Digite seu sexo: ')).upper()
#     if sexo == 'F':
#         # feminino += 1
#         print('Feminino registrado')
#     elif sexo == 'M':
#         # masculino += 1
#         print('Masculino registrado')
#     else:
#         print('Digite uma letra valida (M/F)')
    
# # print(masculino)
# # print(feminino)
# print('Fim')

# -------------------------------------------resolução--------------------------------------------

sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite o sexo [M/F]: ')).strip().upper()[0]
    
print(f'Sexo {sexo} registrado com sucesso')



# ----------------------------------ou-----------------------------------------------



# sexo = ''

# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    
#     if sexo == 'M':
#         print('Usuário é Masculino.')
#     elif sexo == 'F':
#         print('Usuário é feminino.')
#     else:
#         print('Entrada inválida! Digite [M/F]')
    
# print('FIM')








