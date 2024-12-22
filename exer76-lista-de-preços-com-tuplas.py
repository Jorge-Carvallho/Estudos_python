# Exercício 76
# Crie um programa que tenha uma tupla única com nomes e seus respectivos preços 
# na sequencia
# No final mostre uma listagem de preços,organizando os dados em forma tabular


produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'caderno',15.90, 'estojo',25.90, 'trasferidor', 4.20,
            'Compasso',9.99, 'mochila', 120.32, 'canetas',22.30 ,'livros', 34.90
            )

print('--'*20)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('--'*20)
# cont = 0

# for i in range(0, len(produtos),2):
#     nome = produtos[i]
#     preco = produtos[i + 1]
     
#     print(f'{nome:<11} ------------------------------ R${preco:>9} ')
    
# print('-' * 55)
# # -------------------------------------resolução-------------------------------------


for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end= '')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
print('--'* 20)