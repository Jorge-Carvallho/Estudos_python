#Mais do que strings

nome = 'Marcelo Mota'

print(type(nome))# class str

#strings são imutaveis, qualquer operacão dentro daquela string vai gerar uma nova string ou seja, nome continua sendo'Marcelo Mota'
print(nome)
print(nome.upper())# retorna uma versão da string com todos maiúsculos
print(nome.capitalize())# coloca a primeira letra da primeira palavra em maiúscula
print(nome.title())# coloca todas as primeira letras das palavras em maiúsculas
print(nome.replace('a', 'AA'))# o replace infoma dentro da string o que quero subistituir  por qual quero substituir, retorna uma nova string com a substituição feita
print(nome.split('r'))# ele consome a letra informada e troca por um espaço e da seguimento a str, retorna uma lista com os carateres
print('marcelo' + ' ' + 'mota')# concatena a str 
print(' '.join(['marcelo','mota']))# é usado pra concatenar uma lista de str com o que for adicionado ou informado dentro do espaço
print(len(nome))#retorna o comprimento da str com os espaços somados incluidos


