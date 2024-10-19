#Atribuições
# 
from time import sleep
# row = 'Henrique', 'Noterói', 22.9, 43.1

# def f(t):# função f com valor de t atrabuido a variavel row fora da função chamando
#     # nome = t[0]
#     # cidade = t[1]# valores de nome, cidade lad, long, atribuidos aos valores t[indices] fora do escopo da função
#     # lat = t[2]
#     # long = t[3]
# #poderia ser formas abaixo ---v: 
#     # nome,cidade,lat,long = t[0], t[1],t[2],t[3]
#     nome,cidade,lat,long = t
#     print(nome, cidade, lat, long)
    
# if __name__ == '__main__':
#     f(row) # função f aqui chamando row passado como valor t para dentro da função
print('---------------------------------')
#Usando andescor
# def f(t):
#     nome, *_, long = t # o underscore aqui guarda todo o resto no *_ ( o modificador é o *  para testar os resultados so movimentar)
#     print(nome, long, _)# o underscore aqui passa todo o resto para uma lista 

# if __name__ == '__main__':
#     f(row)
#     print('----------------------------------------')

table = (('Henrique', 'Noterói', 22.9, 43.1),
         ('Vinicius', 'Santarém', 2.4, 54.7))

for row in table:
#     nome = row[0]
#     cidade = row[1]
#     lat = row[2]
#     long = row[3]
# #forma simplificada
    nome,cidade,lat,long = row
    print(nome, cidade, lat, long)
# posso fazer dentro do for abaixo exemplo:
print('-------------------------------------')

# for nome,cidade,lat,long in table:# aqui também posso usar underscore ( *_)
for name, *_, in table:# esse underscore agrupa os valores a lista 
    print(nome,_, long) # o que tiver agrupado no underscore de cima mostra a lista com a declaração deste 
    
print('----------------------------------------1---------------------------------------------')

# Exercício de Fixação
# Exercício 1: Desempacotamento Simples
# Dada a seguinte lista de tuplas, desempacote cada tupla em quatro variáveis e exiba o nome, cidade, latitude e longitude.
dados = [
    ('Ana', 'São Paulo', 23.5, 46.6),
    ('Carlos', 'Rio de Janeiro', 22.9, 43.2),
    ('Beatriz', 'Salvador', 12.9, 38.4)
]

for nome, cidade, latitude, longitude in dados:
    print(nome, cidade, latitude, longitude)
    
print('---------------------------------------2---------------------------------------')

# Exercício 2: Usando o Underscore
# Modifique o exercício anterior para usar o underscore (_) para capturar valores intermediários e exibir apenas o nome e a longitude.
for nome, _, _,longitude in dados:
    print(nome,longitude)

print('-----------------------------------------3--------------------------------------')
# Exercício 3: Desempacotamento Parcial com Underscore
# Na lista de tuplas, desempacote apenas o primeiro e o último valor de cada tupla, ignorando os valores intermediários com o underscore.
for nome, *_, longitude in dados:
    print(nome, longitude)
    
print('------------------------------------------4-------------------------------------')
# Exercício 4: Capturando Múltiplos Valores com o Underscore
# Dada a lista de tuplas, use o operador * com o underscore para capturar os valores intermediários e exibi-los como uma lista.
for nome, *valores_intermediarios,longitude in dados:
    print(f'Valores intermediários são {valores_intermediarios}')
    
print('-------------------------------------------5-----------------------------------------')

# Exercício 5: Função com Desempacotamento
# Crie uma função que receba uma tupla como parâmetro, desempacote os valores e retorne uma string formatada. A função deve ignorar o segundo valor usando o underscore.
   
def formatar_tupla(t):
    nome,_,latitude,longitude = t
    return f'{nome} está na latitude {latitude} e longitude {longitude}'
  
resultados = map(formatar_tupla,dados)
print(list(resultados))
      #ou
for tupla in dados:
    print(formatar_tupla(tupla))
print('-'* 70)
    
'''--------------------------------------------Revisão------------------------------------'''
# Exercícios:

# Crie uma lista de tuplas onde cada tupla contém o nome de uma pessoa, o país onde mora, a cidade onde nasceu e a sua idade. Desempacote as tuplas para exibir o nome e a idade de cada pessoa.
lista_tupla = [('Mirian','Brasil','Rio de Janeiro',32),
               ('Carlos','brasil', 'São Paulo', 22),
               ('Edi','Espanha','Madri',35)]

for nome,_,_,idade in lista_tupla: # aqui o exercício foi resolvido com uso de For 
    # sleep(0.8)
    print(nome, idade)
#-------- -------- ------ -------
# def l(f):
#     nome,*_,idade = f
#     sleep(0.8)
#     print(nome,idade)

# if __name__ == '__main__': # aqui o exercício foi resolvido com uso de funcões
    # l(lista_tupla[0])
    # l(lista_tupla[1])
    # l(lista_tupla[2])
print('-' * 60)  

    

     
    
# Dada a lista de tuplas abaixo, desempacote apenas o primeiro valor e o último, ignorando os intermediários com o underscore:
pessoas = [('Lucas', 'Brasil', 'Recife', 30), 
           ('Juliana', 'Portugal', 'Lisboa', 25)]
# def l(pess):
#     nome,*_,idade = pess   #resolvido com função
#     print(nome,idade)

# l(pessoas[0])
# l(pessoas[1])

for nome,*_, idade in pessoas: # resolvido em FOR
    print(nome,idade,)
print('-' * 60)
    

# Escreva uma função que receba uma tupla contendo quatro elementos: Estado(), cidade, temperatura e umidade. Desempacote a tupla e retorne uma string formatada com o estado() e a cidade, ignorando os valores numéricos.
previsao_tempo = [('Amazonas','Capimirim', 27, 31.2),
                  ('Pará','Aven', 25, 31.1),
                  ('Bahia','Salvador',29, 29.9)]
def prev(t):
    estado,cidade,*_ = t
    # sleep(0.9)
    return f'O estado é {estado}, e a cidade é {cidade}' # ou return print(f'O estado é {estado}, e a cidade é {cidade}')

for t in previsao_tempo:
    print(prev(t))
    # ou --> da forma abaixo
# prev(previsao_tempo[0])
# prev(previsao_tempo[1])
# prev( previsao_tempo[2])
print('-'* 60)

# Use o operador * e o underscore para capturar o primeiro valor de cada tupla e todos os valores intermediários, ignorando o último, e depois exiba os valores intermediários como uma lista.
def prev(t):
    estado,*intermediarios = t
    intermediarios = intermediarios[:-1]
    # sleep(0.9)
    return print(intermediarios)

prev(previsao_tempo[0])
prev(previsao_tempo[1])
prev(previsao_tempo[2])
print('-'* 60)



# Modifique o seguinte código para que a variável valores_intermediarios capture apenas os dois últimos valores da tupla usando o underscore para ignorar o primeiro valor:
dados = [('Ana', 'São Paulo', 23.5, 46.6), 
         ('Carlos', 'Rio de Janeiro', 22.9, 43.2),
         ('Amazonas','Capimirim', 27, 31.2)]
    
def v(i):
    primeiros_valores, *intermediarios = i
    intermediarios = intermediarios[1:]
    # sleep(0.9)
    # return intermediarios 
    return print(intermediarios)


# for item in dados:
#     sleep(0.9)
#     print(v(item))                                             # esse exercício foi resolvido de 3 formas diferentes
    
    # ou 
 
v(dados[0])
v(dados[1])
v(dados[2])
print('-'* 60)

    # ou
    
def v(i):
    _,_,valor1,valor2 = i
    # sleep(0.9)
    print([valor1, valor2])

v(dados[0])
v(dados[1])
v(dados[2])
print('-'* 60)

# Dada uma lista de tuplas onde cada tupla contém três elementos: nome, cidade e temperatura, crie uma função que desempacote apenas o nome e a temperatura, e retorne uma string formatada com essa informação.
tempo = [('Ana', 'São Paulo', 23.5 ), 
         ('Carlos', 'Rio de Janeiro', 22.9 ),
         ('Amazonas','Capimirim', 27 )]
def d(f):
    nome,_,temperatura = f
    sleep(0.9)
    return f'O nome é {nome} e a temperatura é {temperatura}'

print(d(tempo[0]))
print(d(tempo[1]))
print(d(tempo[2]))
print('a cidade de cada um é\n')

# Modifique o código acima para exibir apenas o segundo valor de cada tupla, ignorando os demais com o underscore:
def d(f):
    _,cidade,_ = f
    sleep(0.9)
    return f'---> {cidade}'


print(d(tempo[0]))
print(d(tempo[1]))
print(d(tempo[2]))






# Modifique o código abaixo para exibir apenas o segundo valor de cada tupla, ignorando os demais com o underscore:
# cidades = [('São Paulo', 23.5, 46.6), ('Rio de Janeiro', 22.9, 43.2)]
# Escreva uma função que receba uma lista de tuplas, onde cada tupla contém um nome, uma idade e uma cidade. A função deve desempacotar os valores, ignorar a cidade e retornar uma lista contendo apenas os nomes e idades.

# Dada uma lista de tuplas, modifique o código abaixo para usar o underscore e capturar os dois primeiros valores da tupla, ignorando o último:

# valores = [('Maria', 29, 100), ('João', 35, 200)]
# Escreva um código que desempacote uma tupla contendo cinco elementos e use o operador * para capturar o segundo, terceiro e quarto elementos, ignorando o primeiro e o quinto.