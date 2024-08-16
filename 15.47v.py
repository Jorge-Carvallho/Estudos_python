#Classes de caracteres
import re

##  BUSCAR CLASSE DE CARACTER COM COUCHÊTES  --->> [] <<---

# # declarando uma classe de caracter com cochetes e faz a busca um caracter por vez e retorna
print(re.findall('[aeiou]', 'Henrique basto'))
# resultado = ['e','i','u','e', a','o']
print('-------------------------------------------------------------------------------\n')

# # declarando uma clase negando a busca e resoultando todos que não são do padrão
# re.findall('[^aeiou]', 'Henrique Bastos')#uso da ancora ^ dentro dos cochetes negando padrao
print(re.findall('[^aeiou]', 'Henrique Bastos'))#uso da âncora (^) dentro dos cochêtes significa negando padrão,ou seja:
#a âncora (^) dentor dos cochêtes fa faz a negação, (tudo que não for uma vogal sera imprimido)
# resultado = ['H', 'n', 'r', 'q', ' ', 'B', 's', 't', 's'] # a negação 

# # posso fazer Buscas com Renges
print(re.findall('[a-f]','Henrique Bastos')) # buscar entre a e f dentro da ocorrência :(apenas de a até f)
print(re.findall('[a-fA-Z]','Henrique Bastos')) #bucar de a ate f minúsculo e A ate Z maiúsculo
print(re.findall('[a-zA-Z]','Henrique Bastos'))# retorna todos minusculos e maiosculos de a ate z
print(re.findall('[a-zA-Z0-9_]','Henrique Bastos'))# retorna conjunto de caracteres aceitaves de palavras
print(re.findall('[\w]','Henrique Bastos'))# codigo que representa a ate z, 0 ate 9, maiúscula/minúscolas _
# # o \w acima não precisa esta dentro de uma classe para funcionar, exemplo
print(re.findall('\w', 'Henrique Bastos')) # mesma forma da de cima 

# # #ESPECIAIS SEQUÊNCIAS
# # \d == [0-9] class de 0 ate 9
# # \D == [^0-9] classe negando caracretes de 0 ate 9
# # \s == [\t\n\r\f\v] clase de controles
# # \S == [^\t\n\r\f\v] classe negando  controle acima
# # \w == [a-zA-Z0-9_] clase buscando a ate z minusculo e maiusculo de 0 a 0 e andescor (_)
# #\W == [^a-zA-Z0-9_] classe negando a de cima
