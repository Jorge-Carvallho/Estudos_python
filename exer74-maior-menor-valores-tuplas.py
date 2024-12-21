# Exercício 74
# Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
# Depois disso , mostre uma listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla


from random import choices, randint
# sorteados = tuple(choices(range(0,20),k=5))
# print(f'Os valores sorteados foram {sorteados}')

# for n in sorteados:
#     print(f'{n} ', end='')
# print()

# print(f'O maior numero foi {max(sorteados)}')
# print(f'O menor número foi {min(sorteados)}')


# -------------------------------------------------------------------------------------


numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os vaores sorteados  foram ', end='')
for n in numeros:
    print(f'{n}',end=' ')


print(f'\nO maior número foi {max(numeros)}')
print(f'O menor números foi { min(numeros)}')




# numeros = (sorteados)
# for c in range(sorteados):
#     print(numeros)