# Exercício 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: Digite um número: 1834
# unidade--> 4
# dezena --> 3
# centena --> 8
# milhar --> 1

# --------------------------------fórmula com strings-----------------------------
# numeros_digitados = input('Digite um número de 0 ate 9999: ')
# numeros_digitados = numeros_digitados.zfill(4)

# unidade = numeros_digitados[-1]
# dezena = numeros_digitados[-2]
# centena = numeros_digitados[-3]
# milhar = numeros_digitados[-4]

# print(f'''Os números digitados foram 
#       \nNa unidade--> {unidade} 
#       \nNa dezena--> {dezena} 
#       \nNa centena--> {centena} 
#       \nNo milhar--> {milhar}''')


# ------------------------------------fórmula com números inteiros-------------------------------

numero = int(input('Informe um número:'))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade --> {u} ')
print(f'Dezena --> {d}')
print(f'Centena --> {c}')
print(f'Milhar --> {m}')
