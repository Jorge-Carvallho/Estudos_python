# Exercício 49
# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
# so que agora utilizando o for

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(f' {num} x {c:2} = {num* c}')
    