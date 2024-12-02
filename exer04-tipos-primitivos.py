# Exercício 04
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele

palavra = input('Digite algo: ')
print(f'O tipo primitivo desse valor é -- > {type(palavra)}')# tipo
print(f'So tem espaços -- > {palavra.isspace()}')# verifica espaços
print((f'É um número --> {palavra.isnumeric()}'))# verifica se é número
print(f'É alfabetico --> {palavra.isalpha()} ')# verifica se contém so letras
print(f'É alfanumérico --> {palavra.isalnum()} ')# verifica se contém letras e números
print(f'Esta em maiusculas --> {palavra.isupper()} ')# verifica se é maiúsculos
print(f'Esta em minúsculas --> {palavra.islower()} ')# verifica se é minúsculos
print(f'Esta capitalizada --> {palavra.istitle()}')# verifica se a palavra está maiúscula e minúsculas
