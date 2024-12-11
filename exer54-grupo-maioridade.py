# Exercício 54
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.


maior_idade = 0
menor_idade = 0
ano = 2024
for c in range(1,8):
    data_nasc = int(input(f'\033[34m Em que ano {c} ª pessoa nasceu?\033[0m '))
    if ano - data_nasc > 18:
        maior_idade +=1
    else:
        menor_idade +=1
        
    
    
    
print(f'No total tivemos {maior_idade} pessoas com maior idade.')
print(f'No total tivemos {menor_idade} pessoas com menor idade.')
