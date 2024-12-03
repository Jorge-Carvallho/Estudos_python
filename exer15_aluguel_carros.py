# Exercício 15
# Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

# diarias_alugadas = float(input('Quantos dias carro ficou alugado: '))
# km_rodados = float(input('Quantos km foram rodados nesses dias:'))

# valor_diaria = 60.00
# valor_km = 0.15

# valor_dias_alugados = diarias_alugadas * valor_diaria  
# total_km_rodados = km_rodados * valor_km

# print(f'total a pagar é {valor_dias_alugados + total_km_rodados}')











# Exercício
# ----------------------outra forma------------------------

dias = int(input('Quantidades de dias alugados: '))
km = float(input('Quantos km rodados: '))

pago =(dias * 60.0) + (km * 0.15)

print(f'O total a pagar é de R${pago}')

