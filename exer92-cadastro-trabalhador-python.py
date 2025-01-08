# Exercício 92
# Crie um programa que leia um nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá também
# ano de contratação e o salário. Calcule e acrescente, além da idade , com quantas anos
# a pessoa vai se aposentar


# dados_trabalhador = {
#     'Nome': str(input('Nome: ')),
#     'Ano de nascimento:': int(input('Ano de nascimento: ')),   
#     'Carteira de trabalho Nª': int(input('Número da carteira de trabalho (0 não tem): '))
# }
# idade = 2024 - dados_trabalhador['Ano de nascimento:']
# aposentadoria = 60 - idade
# dados_trabalhador['Idade'] = dados_trabalhador.pop('Ano de nascimento:')
# dados_trabalhador['Idade'] = idade

# # -----------------novo dicionario arurmado em ordem do exercício--------------
# dados_trabalhador = {
#     'nome': dados_trabalhador['Nome'],
#     'Idade': idade,
#     'Carteira de trabalho Nª': dados_trabalhador['Carteira de trabalho Nª']
# }

#     # -----------verifica se carteira de trabalho tem número-------------
# if dados_trabalhador['Carteira de trabalho Nª'] == 0:
#     dados_trabalhador['Carteira de trabalho Nª'] = 'ctps valor tem 0'

#     print('='* 30)
#     # -------mostra resultado na tela----------------

#     for d,v in dados_trabalhador.items():
#         print(f' - {d} tem o valor --> {v}')

#     # ---------------caso a carteira tenha número--------------------

# else:

#     dados_trabalhador['Carteira de trabalho Nª']
#     dados_trabalhador['Ano de contratação'] = str(input('Ano de contratação: '))
#     dados_trabalhador['Salário'] = int(input('Salário: '))
#     dados_trabalhador['Aposentadoria'] = aposentadoria
    
    
#     for d, v in dados_trabalhador.items():
#         print(f' - {d} tem o valor --> { v}')


# ---------------------------------------resolução------------------------------------------


from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 caso não tenha): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salários'] = int(input('Salário R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35 ) - datetime.now().year)
    
print('-='* 30)
for k ,v in dados.items():
    print(f' - {k} tem o valor --> {v}')