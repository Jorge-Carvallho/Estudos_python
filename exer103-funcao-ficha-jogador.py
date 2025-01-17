

def ficha(nome='desconhecido',gols='0'):
    if nome == '':
        nome = '< desconhecido >'
    if not gols.isdigit():
        gols = 0 
        
    return f'O nome do jogador é {nome}, e fez {gols} gols'
    

    
    
nome = str(input('Digite o nome do Jogador: '))
gols = str(input('Difite quantos gols o jogador fez: '))
    
    

print(ficha(nome,gols))
