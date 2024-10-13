#loops Radicais
nome = 'Henrique'
print(nome, len(nome))
# while basicamente enquanto algo for verdadeiro execulte se for false o bloco de código é ignorado
i = 0
while i < len(nome): # 8 ou len(nome) o qual é mas correto
    print(nome[i])#enquanto I for menor que len(nome) imprima nome na posição de I, e atualize I somando mas 1 ate que seja menor de len(nome), ou seja, tamanho.
    i = i + 1 # o mesmo que i += 1
print('----------------------------------')
    
for i in range(len(nome)):# mesmo código do while mas organizado
    print(nome[i])
    
r = range(1,30,3)#range funciona como o splice passando o parámetro de início e final com passos ex: de 1, até 30 de 3
print(list(r))# passo o resultado da expressão para uma lista para ver o trabalho do range
for c in (nome):
    print(c) # Poderia fazer com qualquer letra o mesmo código de cima sem precisar usar o range pois a letra c neste caso iterara sobre uma de cada vez da string da variável (nome) 
print('---------------------------------')
# Usando ENUMERETE:
for c in nome: #retorna cada letra
    print(c)
for c in enumerate(nome): #retorna uma tupla com indice de cada elemento
    print(c)
for i,c in enumerate(nome):#retorna i  de indice e c referente a cada leta da string 
    print(i,c)
    
# Usando o continue:
for i, c in enumerate(nome):
    if c == 'e':
        #dentro coloquei o continue mas poderia fazer qualqeur coisa ai dentro, oi parar com break
        print('continuando ')
        continue
    print(i,c) # aqui segue o exemplo, ele vai continuar o código mas esta imprimindo dentro do if e continuando 
    
print('-------------------------------------------------------------------------\n')
# Imprimindo Caracteres com while
# Escreva um código que percorra uma string usando um loop while e imprima cada caractere da string individualmente. A string deve ser fornecida pelo usuário.
string = 'inconstitucionalissimamente'
i = 0
while i < len(string):
    print(string[i])
    i += 1
print('----------------------------------for----------------------------')
# Imprimindo Caracteres com for
# Reescreva o exercício anterior, mas dessa vez utilizando um loop for com range().
for i in range(len(string)):
    print(string[i])

# Contando Caracteres Específicos
# Solicite uma string do usuário e conte quantas vezes a letra "a" aparece na string. Use um loop for para isso.
contador_a = 0
for letra in string:
    if letra == 'a':
        contador_a += 1 
        
print(f' A letra (a) apareceu {contador_a} vezes')

# Imprimindo uma Sequência com range()
# Crie um código que utilize o range() para gerar uma lista de números de 10 a 50, pulando de 5 em 5, e imprima essa lista.
numeros = list(range(10,50,5))
print(numeros)

# Usando enumerate() para Iterar sobre Strings
# Escreva um código que peça uma string ao usuário e, usando enumerate(), imprima o índice e o caractere correspondente em cada iteração do loop.
for i, caracter in enumerate(string):
    print(f'O indice é --> {i} e caracter é -->  {caracter}')