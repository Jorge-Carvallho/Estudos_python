# Exercício 55
# Faca um programa que leia o peso de cinco pessoas 
# No final mostre qual foi o maior e menor peso lidos.


peso_maior = 0
peso_menor = 0
for c in range(1,6):
    peso_pessoa = float(input(f'Peso da pessoa {c}ª pessoa: '))
    if c == 1: # inicia o loop atribuindo o primerio peso como maior e como menor
        # para aparti daqui então fazer as comparaçoes abaixo
        peso_maior = peso_pessoa # atribuo peso_maior a pessoa
        peso_menor = peso_pessoa # atribuo peso_menor a pessoa
    else:
        if  peso_pessoa > peso_maior: #se peso da pessoa for maior do que o peso maior
            # que iniciei acima com o primeiro peso, entao passa a ser maior peso
            peso_maior = peso_pessoa # então ele passa a ser o maior
        
        if  peso_pessoa < peso_menor: # se peso da pessoa for menor do que iniciado acima 
            # peso menor passa a ser menor peso
            peso_menor = peso_pessoa

        
print(f'O maior peso lido foi {peso_maior}Kg')
print(f'O menor peso lido foi {peso_menor}Kg')

# ---------------------------------------------ou-----------------------------------
  

