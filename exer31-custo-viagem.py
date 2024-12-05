# Exercício 31
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem,cobrando R$0.50 por km para viagem de até 200km,
# e R$0.45 para viagem mais longas.




distancia_viagem = int(input('Qual foi a distância da viagem: '))
km_base = 200
preco_base= 75.00
preco_km_passado = 1.95
valor_passagem_atualizado = ((distancia_viagem - km_base) * preco_km_passado) + preco_base

if distancia_viagem <= km_base:
    print(f'Você esta preste a começar uma viagem {distancia_viagem:.1f}Km')
    print(f'O valor da passagem foi R${preco_base:.2f}')
else:
    print('-=-'* 20)
    print(f'Você esta preste a começar uma viagem de {distancia_viagem:.1f}km')
    print(f'O preço de sua passagem será R${valor_passagem_atualizado:.2f}')
    print('-=-'* 20)
    
    
    
    
    