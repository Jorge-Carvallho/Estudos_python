# Exercício 08
# Escreva um programa que leia um valor em metros e o exiba concertido em:
# kilometros, hectômetros, decâmetros, decimetros,centimetros, milimetros.


metros = float(input('Digite a distancia em metros: '))

km = metros / 1000
hectometros = metros / 100
decametros = metros / 10

decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
print(f'A medida de {metros} correspode a ---->')


print(f'{metros} metros para km resultado é --> {km}')
print(f'{metros} metros para hectômetro resultado é --> {hectometros}')
print(f'{metros} metros para decâmetro resultado é --> {decametros}')
print('*'* 60)
print(f'{metros} metros para decimetros  resultado é --> {decimetros}')
print(f'{metros} metros para centimetros resultado é --> {centimetros}')
print(f'{metros} metros para milimetros resultado é --> {milimetros}')

# obs::.f0--> número indica quantas casas decimais
#     :.2f formatará o número com 2 casas decimais.
#     :.5f formatará o número como 5 casas decimais.
