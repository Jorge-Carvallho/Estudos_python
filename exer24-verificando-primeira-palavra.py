# Exercício 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

nome_da_cidade = input('Você nasceu em qual cidade: ').strip()#retira os espaços do inicio e final

print(nome_da_cidade[:5].lower() == 'santo')
print(nome_da_cidade.lower().startswith('santo'))

# obs:--> poderia colocar com upper() no caso verificar maiúsculas no caso
