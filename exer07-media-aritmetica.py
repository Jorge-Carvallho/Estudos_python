# Exercício 07
# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostrre a sua media

primeira_nota = float(input('Digite a primeira nota do aluno: '))
segunda_nota = float(input('Digite a segunda nota do aluno: '))

media = (primeira_nota + segunda_nota) / 2 

print(f'A media entre {primeira_nota} e {segunda_nota} é {media:.2f}')
