#Mais do que strings

nome = 'Marcelo Mota'

print(type(nome))# class str

#---strings são imutaveis(nao pode ser mudada), qualquer operacão dentro daquela string vai gerar uma nova string ou seja, nome continua sendo'Marcelo Mota' e a mudança sera uma nova string

print(nome)
print(nome.upper())# retorna uma versão da string com todos maiúsculos
print(nome.capitalize())# coloca a primeira letra da primeira palavra em maiúscula
print(nome.title())# coloca todas as primeira letras das palavras em maiúsculas
print(nome.replace('a', 'AA'))# o replace infoma dentro da string o que quero subistituir  por qual quero substituir, retorna uma nova string com a substituição feita
print(nome.split('r'))# ele consome a letra informada e troca por um espaço e da seguimento a str, retorna uma lista com os carateres mas não consume o espaço da letra em que foi realizado o split(o mesmo que retirada)
print('marcelo' + ' ' + 'mota')# concatena a str 
print(' '.join(['marcelo','mota']))# join ele pega neste caso as string e uno uma a outra (concatena) com, o que vem antes do join que é as aspas(' ') é o separador que sera colocado entre as strings----------> exemplo abaixo
print(len(nome))#retorna o comprimento da str com os espaços somados incluidos

print('------------------------------------------')

#Exercícios:
#Crie uma variável chamada frase e atribua a ela a string: "aprendendo python é divertido".
frase = 'Aprendendo python é divertido'
print(frase)
print('-------------------------------------------')
#Utilize os métodos de string para realizar as seguintes operações:
#Imprima a string toda em maiúsculas.
#Imprima a string com a primeira letra em maiúscula.
#Imprima a string com todas as primeiras letras de cada palavra em maiúsculas.
#Substitua todas as ocorrências da letra "e" por "E".
#Divida a string em uma lista de palavras, utilizando o espaço como delimitador.
#Concatene as palavras "Python" e "é" com a palavra "fantástico" usando o operador + e imprima o resultado.
#Use o método join para unir as palavras ["Python", "é", "fantástico"] com um espaço entre elas e imprima o resultado.
#Imprima o comprimento da string frase.

print(frase.upper())
print(frase.title())
print(frase.replace('e', 'E'))
print(frase.split(' '))
print('Python ' + 'é' + ' fantástico')
print(' '.join(['Python', 'é', 'fantástico']))
print(len(frase))


print('-------------------------------------teste auqi em baixo-------------------------')

"""exemplo .join eu poderia colocar um caracter ou um esapaco ou pular linha entre as strings """
nome = 'Jorge '
nomes = ['Nilson', 'Miranda', 'de', 'carvalho']
resultado = ' '.join(nomes)
resultado1 = ' - '.join(nomes)
resultado2 = '\n'.join(nomes)
print(nome + resultado,' resultado')
print(nome + resultado1, 'resultado 1')
print(nome + resultado2, ' resultado 2')

print('---------------------------------------------------------------------------')

# Exercícios:
# Exercício 1: Crie uma variável chamada palavra e atribua a ela a string "linguagem de programação". Use os métodos de string para:
# Imprimir a string toda em maiúsculas.
# Imprimir a string com a primeira letra da primeira palavra em maiúscula.
# Imprimir a string com todas as primeiras letras de cada palavra em maiúsculas.
# Substituir todas as ocorrências da letra "a" por "A".
# Dividir a string em uma lista de palavras, utilizando o espaço como delimitador.
palavra = 'linguagem de programação'
print(palavra.upper())
print(palavra.capitalize())
print(palavra.title())
print(palavra.replace('a', 'A'))
print(palavra.split(' '))

# Exercício 2: Crie uma variável chamada nome_completo e atribua a ela a string "Maria Fernanda da Silva". Utilize o método split para dividir o nome completo em uma lista de palavras. Depois, use o método join para concatenar essas palavras novamente, mas separando-as por um hífen (-).
nome_completo = 'Maria Fernanda da Silva'
lista_de_nomes = nome_completo.split(' ')
print(lista_de_nomes)
lista_de_nomes = ' '.join(lista_de_nomes)
print(lista_de_nomes)

# Exercício 3: Dada a string "Python é poderoso e versátil", faça o seguinte:
# Imprima a string com todas as letras em minúsculas.
# Substitua todas as ocorrências da palavra "poderoso" por "impressionante".
# Divida a string em uma lista de palavras, utilizando o espaço como delimitador.
# Imprima o comprimento da string.
string = 'Python é poderoso e versátil'
print(string.lower())
print(string.replace('poderoso','impressionante'))
print(string.split(' '))
print(len(string))

# Exercício 4: Crie uma frase de sua escolha e faça as seguintes operações:
# Verifique o comprimento da frase.
# Concatene a frase com outra frase de sua escolha, utilizando o operador +.
# Substitua todas as ocorrências da letra "o" por "0" (zero).
# Divida a frase em uma lista de palavras.
# Use o método join para unir as palavras com um espaço entre elas e imprima o resultado.
frase = 'Aqui estão alguns exercícios para você praticar, baseados no conteúdo sobre strings e seus métodos'
print(len(frase))
print('Esse texto esta comcatenado com, ' +  frase)
print(frase.replace('o','0'))
frase_lista = frase.split()
print('Frase em lista ',  frase_lista)
frase_lista= ' '.join(frase_lista)

print(frase_lista)