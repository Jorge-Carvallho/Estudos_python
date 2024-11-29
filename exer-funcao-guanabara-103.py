# Exercício
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome do jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='<desconhecido>',gols=0):
    nome = nome
    # nome.strip('')
    return(f'O nome do jogador é {nome} e marcou {gols} gols.')
    



#print(ficha())
#ficha('Evandro', 5)
#print(ficha('Miranda', 2))
      
      


assert ficha() == f'O nome do jogador é <desconhecido> e marcou 0 gols.'
assert ficha('Evandro', 5) == f'O nome do jogador é Evandro e marcou 5 gols.'
assert ficha('Miranda', 2) == f'O nome do jogador é Miranda e marcou 2 gols.'



# n= 'Jorge'
# g=  
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:ficha(n,g)
    
    
    
    
    