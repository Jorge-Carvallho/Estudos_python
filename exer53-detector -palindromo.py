# Exercício 53
# Crie um programa que leia a frase qualquer e diga se ela é um palindromo,
# desconsiderando os espaços.

# frase = str(input('Digite uma frase: ')).strip().replace(' ','')
# print(f'\033[34m {len(frase)}')
# fraseinvertida = frase[-1::-1]
# # print(frase)
# # print(fraseinvertida)

# if frase == fraseinvertida:
#     print(f'O inverso de {frase} é {fraseinvertida}\nPalavra é um palindromo')
# else:
#     print('Não é um palindromo')

# ----------------------ou--------------------------


frase = str(input('Digite uma frase: ')).strip().lower()
palavra = frase.split() # trasforma a frase do input em uma (LISTA) de palavras.
junto = ''.join(palavra)# join faz a união das palavras da frase.
inverso = ''

for letra in range(len(junto) -1, -1, -1): # para cada letra do índice de (junto) que nada mas é, que a frase trasformada em uma list, depois juntada 
# pra ter acesso pelo índice, que começa de -1 -1 e -1, de trás vindo pra trás, de de -1 a -1
   
    inverso += junto[letra]# aqui atribuo junto que já está de trás pra frente a inverso, não referenciando a indice mas sim a letra


if junto == inverso:
    print(f'o inverso da palavra ({junto}) é igual a ({inverso})\nPalavra é um palíndromo')
else:
    print(f'Palavra ({junto}) não é um palíndromo da palavra ({inverso})')