# Exercício 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tel 'SILVA' no nome.

nome = input('Digite o nome: ').strip()# retira todo os espaços do inicio e final da string
print('silva' in nome.lower())