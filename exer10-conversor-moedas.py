# Exercicio 10
# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar.
#  valor do dolar esse momento 5.98

# valor_real = float(input('Quanto dinherio você tem na carteira: '))
# dolar = 5.98

# resultado = valor_real / dolar


# print(f'O valor {valor_real} reais equivale a {resultado:.2f} dolar')


# ou


real = float(input('Quanto dinherio você tem na carteira: '))
dolar = real / 6.00

print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))