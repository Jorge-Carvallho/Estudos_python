# Exercício 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# --> O nome com todas as letras maiúsculas:
# --> O nome com todas as letras minúsculas:
# --> Quantas letras ao todo no nome sem considerar os espaços:
# --> Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()# elimina os espaços do inicio e fim 

print('Seu nome em maiúsculo é -->', nome.upper())
print('-'* 15)#------------------------
print('Seu nome minúsculos é -->', nome.lower())
print('-'* 15)#------------------------


# -----------------------------------------------------------------------
# nome_sem_espaços = nome.replace(' ', '')
# print(f'Seu nome sem espaços é --> {nome_sem_espaços} e o tamanho é --> {len(nome_sem_espaços)}')
                    #ou
print('Tamanho do nome apenas as letras--> ',len(nome) - nome.count(' '))
#---------------------------------------------------------------------------
print('-'* 15)#------------------------


                
print(f'Primerio nome tem letras -->', {nome.find(' ')})#forma 01
print('Tamanho do primerio nome é -->',len(nome.split()[0]))#forma 02
primerio_nome = nome.split()[0] #forma 03
print(f'O primerio nome foi --> {primerio_nome} e o tamanho foi --> {len(primerio_nome)}')




