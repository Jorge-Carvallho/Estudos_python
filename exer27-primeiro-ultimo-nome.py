# Exercício 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguidao primerio
# e o último nome separadamente.
nome = input('Digite sue nome completo: ').strip()

# primeiro_nome = nome.split()[0]
# ultimo_nome = nome.split()[-1]

# print(f'Seu primerio nome foi {primeiro_nome}')
# print(f'Seu último nome foi {ultimo_nome}'


    # --------------------------------ou ----------------------------

nome = nome.split()
print(f'Primeiro nome é ---> {nome[0]}')
print(f'Último nome é ---> {nome[-1]}')
    

    
    