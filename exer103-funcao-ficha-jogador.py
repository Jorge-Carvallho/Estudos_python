# Exercício 103
# Faça um proghrama qie tenha um afunção chamada ficha(),que
# receba dois parâmetros opcionais: o nome d eum jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente


# def ficha(nome='desconhecido',gols='0'):
#     if nome == '':
#         nome = '< desconhecido >'
#     if not gols.isdigit():
#         gols = 0 
        
#     return f'O nome do jogador é {nome}, e fez {gols} gols'
    

    
    
# nome = str(input('Digite o nome do Jogador: '))
# gols = str(input('Difite quantos gols o jogador fez: '))
    
    

# print(ficha(nome,gols))
# ----------------------------------------------------------------------------------------

n = str(input('Digite o nome do Jogador: ' ))
g = str(input('Número de gols: '))


def ficha(nome='desconhecido', gols=0):
    if nome == '':
        nome = 'Desconhecido'
    
    if not gols.isdigit(): # posso colocar sem usar ele o isdigit()
        gols = 0
    else:
        gols = int(gols)
        
    print(f'O Jogador {nome}, fez {gols} gols no campeonato')


ficha(n, g)