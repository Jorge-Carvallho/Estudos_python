# Manipulando Texto
frase = 'Curso em video Python'
print(frase[3]) # fatiamento de strings, retorna a letra do indíce [ inicio (:) até final (:) de quantos em quantos
# obs---> O último índice em slices não é incluído. Por exemplo, [1:10] pega do índice 1 até o 9, O 10  não mostra
print('-'* 25)

print('Texto pequeno --> duas aspas ' '  ')
print('Texto grande --> três aspas """ -- """ ' )
# obs:--> letra maiúsculas e minúsculas são diferentes ex: 
print('-'* 25)

print('letra o minuscula ---> ',frase.count('o')) #--> returna quantas vezes aparece a letra (o) minúscula
print('letra o maiúscula --->',frase.count('O')) # --> returna quantas vezes apareceu a letra (O) maiúsculas
print('frase maiuscula quantas letras maiúscula --->', frase.upper().count('O')) # --> returna o mesmo que o print()count com O maiúsculo / na frase jogada para letra maiúscula,contar quantas letras maiúsculas O existem
print('-'* 25)
frase_teste_01 = '   Curso em video Python     '
print(len(frase_teste_01))# returna  a qunatidade de caracteres(letras da frase ou palavra) contando com os espaços
print(len(frase_teste_01.strip()))# returna a quantidade de caracteres, porém remove os espacos doinicio e fim da frase
print('-'* 25)

print(frase.replace('Python', 'linguagem de programação'))#replace remove a palavra Python por linguagem de programação
print(frase)# o replace não altera a string original, ele cria uma cópia entâo posso fazer 
frase = frase.replace('Python', 'linguagem de programação') # aqui a frase alterada foi atribuida a variavel frase
print(frase)
print('-'* 25)
frase01 = 'Curso em Video Python'

print('video' in frase)# returna True or False se palavra tem em frase
print(frase.find('Video'))# retorna o indice da palavra aparti de onde se inicia a palavra indicada,
#--> caso a palavra não exita na frase ele retorna -1 
print(frase.lower().find('video'))# transformou a frase em minúscula e verificou se tinha a palavra minuscula na frase1,
# retornou i indici inicial da palavra consultada na frase, caso nao tenha returna -1
print('-'* 25)

print(frase)# frase inteira
frase_dividida = frase.split()# frase dividida
print(frase_dividida) # posso consultar a frase dividida por indices
print(frase_dividida[3])# retuna frase dividida no indice 3
print(frase_dividida[0][3])# dentro do indice 0 da frase dividida posso buscar o indice da palavra que retornou do primerio indice,
# que nesse caso indice 0 é a palavra Curso e indice 3 é a letra s



