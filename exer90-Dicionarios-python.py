# Exercício 90
# Faça um programa que leia nome e a média de um aluno,
# guardando também a situação em um dicionárioo.
# No final mostre o conteúdo da estrutura na tela

# dados = dict()
# aluno = list()
# for c in range(0,2):
#     dados['nome:'] = str(input('Digite seu nome: '))
#     dados[f'Média:'] = float(input(f'Media de pessoa: '))
#     aluno.append(dados.copy())

# # print(dados)
# # print(aluno)
# for cada in aluno:
#     media = cada['Média:']
#     if cada['Média:'] > 7.0:
#        print(f'Sua media é {media}')
#     else:
#        print('Reprovado')
# # --------------------------------------resolução-------------------------------


# aluno = dict()
# aluno['Nome'] = str(input('Nome: '))
# aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
# if aluno['Média'] >= 7:
#     aluno['Situação'] = 'Aprovado'
# elif aluno['Média']>= 5 and aluno['Média'] < 7:
#     aluno['Situação'] = 'Recuperação'
# else:
#     aluno['Situação'] = 'Reprovado'


# print('='* 15)
# for k,v in aluno.items():
#     print(f'-  {k}, é igual a {v}')


# # print(aluno)

# --------------------------------------------novamente-----------------------------------------------------




produtos = dict()

produtos['Produto'] = str(input('Nome do produto: '))
produtos['Preço'] = float(input(f'Qual o preço do Produto {produtos["Produto"]} '))
produtos['Quantidade'] =  int(input(f'Quantas gramas o produto {produtos["Produto"]} tem  ' ))


print(produtos)