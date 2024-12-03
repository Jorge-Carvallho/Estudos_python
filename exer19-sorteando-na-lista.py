# Exercicio 19
# Um professor quer sortear um doa quatro alunos para apagar o quadro.
# Faça um programa queajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice


aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')    # sortea um nome aleatório
aluno4 = input('Qaurto aluno: ')

nomes = [aluno1, aluno2, aluno3, aluno4]





print(f'O aluno escolhido foi {choice(nomes)}-->')
