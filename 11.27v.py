#Atribuições
# 
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
    
  
  

      