# Exercício 29
# Excreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima da velocidade

# velocidade_permitida = 80
# velocidade = int(input('Qual a velocidade atual do carro: '))
# valor_km = 7
# valor_multa_base = 220
# if velocidade <= velocidade_permitida:
#     print('Tenha um bom dia! Dirija com seguraça!')
# else:
#     acima_da_velocidade = velocidade - velocidade_permitida
#     total_da_multa = valor_multa_base + acima_da_velocidade * valor_km
#     print('-=-'*30)
#     print('Multado! Você excedeu o limite permitido que é de 80Km/h')
#     print(f'Você deve pagar uma multa de R${total_da_multa:.2f}')
#     print('Tenha um bom dia! Dirija com segurança')
#     print('-=-'*30)

# ------------------------------------------------resolução-----------------------------------------------------

velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80 )* 7.00
    print(f'Você deve pagar uma multa de {multa:.2f}')
    print('MULTADO! Você excedeu o limete permitiddo que é de 80Km/h.')

print('Tenha um bom dia! Dirija com segurança!')