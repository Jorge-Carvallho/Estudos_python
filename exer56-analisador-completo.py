# Exercício 56
# Desenvolva um programa que leia nome, idade, sexo de 4 pessoas.
# No final do programa mostre:
# A média de idade do grupo:
# Qual o nome do homen mas velho do grupo:
# Quantas mulheres tem menos de 20 anos:


# somaidade = 0
# mediaidade = 0
# maioridadehomen = 0
# nomevelho = ''
# totalmulher20 = 0
# for p in range(1,5):
#     print(f'-------- {p}ª PESSOA -------')  
#     nome = input('Nome: ').strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]: ')).strip()
#     somaidade += idade   #a cada interacão soma a idade para obter a média
#     if p == 1 and sexo in 'Mm': # inicia a verificacao da idade e verifica se é masculino
#         maioridadehomen = idade #se for masculino atribua a idade a idade ao homen mas velho
#         nomevelho = nome # i atribui o nome do homen mas velho a variavel homenvelho
#     if sexo in 'Mm' and idade > maioridadehomen: # testa se idade é maioridadehomen
#         maioridadehomen = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade < 20: #verifica se quantas mulher menor de 20 anos
#         totalmulher20 +=1

    
# mediaidade = somaidade / 4
    
# print(f'A média de idade os integrante do grupo é {mediaidade}')
# print(f'O homen mais velho tem {maioridadehomen} e se chama {nomevelho}')
# print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos')


# -------------------------------------------------------------------------------------------------




somaidade = 0
mediaidade = 0
homen_mais_velho = 0
nome_homen_mais_velho = ''
total_mulheres = 0
for p in range(1,5):
    print(f'-------- {p}ª Pessoa --------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homen_mais_velho = idade
        nome_homen_mais_velho = nome
    if homen_mais_velho > idade:
        nome_homen_mais_velho
    if  sexo in 'Ff' and idade < 20:
        total_mulheres += 1
        
        
mediaidade = somaidade / 4   
print(f'A média de idade do grupo é {mediaidade}')
print(f'O nome do homen mas velhos se chama {nome_homen_mais_velho}')
print(f'Total de melheres menos que 20 anos são {total_mulheres}')
    
    


 
       
