# Exercício 91
# Crie um programa onde 4 jogadores joguem um dadoe tenham resultados aleatórios
# Guarde esse reusltado em um dicionário.
# No final coloque esse dicionário em orden sabendo que o que o vencedortirou o maior número no dado

# from random import randint
# from operator import itemgetter
# jogoJogando = dict()

# jogoJogando['Jogador1'] = randint(1,6)
# jogoJogando['Jogador2'] = randint(1,6)
# jogoJogando['Jogador3'] = randint(1,6)
# jogoJogando['Jogador4'] = randint(1,6)

# print('Valores sorteados são:')

# for jogador,valor in jogoJogando.items():
#     print(f'O {jogador} tirou {valor} no dado.')

# ranking = list()

# sorted(jogoJogando.items()),key=itemgetter(1), reversed=True
# print()
# print('====Ranking dos jogadores====')




# ----------------------------------------------teste 01----------------------------------
from random import randint
from operator import itemgetter
jogadores = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1,6)   
}
for j ,v in jogadores.items():
    print(f'{j} tirou {v} no dado')
    
print()

print('=====Ranking dos jogadores====')
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)



for i,v in enumerate(ranking):
    print(f'{i+1}ªlugar: {v[0]} com {v[1]} pontos')

print('='*30 )

