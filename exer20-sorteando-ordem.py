# Exercício 20
# O memso professor do desafio anterior quer sortear a ordem de apresentaçãode trabalho ods alunos.
# Faça um programa que leia o nome dos quatros e mostre a ordem sorteada.


from random import choice, shuffle


aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')    # sortea um nome aleatório
aluno4 = input('Qaurto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(lista)


print(f'A ordem dos alunos escolhido foi {lista} -->')
