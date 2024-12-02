# Exercício 12
# Faça um algotiymo que leia preço de um produto e mostre seu novo preço, com 5% de desconto.

# ------------> obs: 2 formulas diferentes

preco_sem_desconto = float(input('Qual é o preço do produto: '))

preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 5 / 100)
# preço_com_desconto = preco_sem_desconto * (1 - 5 / 100)
print(f'O produto que custava R${preco_sem_desconto:.2f}, na promoção de 5% vai custar R${preco_com_desconto:.2f}')