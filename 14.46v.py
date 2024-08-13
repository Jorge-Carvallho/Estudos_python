#Metacaracter
import re
print(re.match('.','\n'))# ponto retorna qualque caracter ao menos \n retorna none
print(re.search('.','\nabc'))# ponto no search apos o \n ele busca outra ocorrência e encontra neste caso
print(re.findall('.','')) # ponto aqui retorna uma lista vazia ou com as ocorrências em  [ ]


# #ancoras de inicio e final de string  ^ e $ 
# # ^ ancora de inicio de linha

print(re.findall('^.', 'abc\ndef\nghi')) # retorna --> a <-- pois ele  percorre até antes do \n ou seja, até aquela linha, para ele outrapassar p \n,usar flag re.MULTILINE, ele passarar a corresponder ao início de cada linha
# resulta = ['a']
# findall('^.', 'abc\ndef\nghi', re.MULTILINE) # retorna o primeiro de cada linha 
# resultado = ['a', 'd','g']
#----------------------------------------------------------------------------------------------------

 233 m 46

# # $ ancora de fim de linha
# findall('.$', 'abc\ndef\nghi') 
# #retorna o caracter final de cada linha
# findall('.$', 'abc\ndef\ncvg',re.MULTILINE)
# resultado = ['c', 'f','g']
# #retorna o caracter finald e cada linha percorrendo as linhas do \n



























# # declarando uma classe de caracter com cochetes e faz a busca um caracter por vez e retorna
# re.findall('[aeiou]', 'Henrique Basto')
# resultado = ['e','i','u','a','o']

# # declarando uma clase negando a busca e resoultando todos que nao são do padrão
# re.findall('[^aeiou]', 'Henrique Bastos')#uso da ancora ^ dentro dos cochetes negando padrao
# resultado = ['H', 'n', 'r', 'q', ' ', 'B', 's', 't', 's'] # a negação

# # posso fazer alguns Renges, alguns de codigos prontos
# re.findall('[a-f]','Henrique Bastos') # buscar apenas de a até f
# re.findall('[a-fA-Z]','Henrique Bastos') #bucar de a ate f minusculo e A ate Z maiusculo
# re.findall('[a-zA-Z]','Henrique Bastos')# retorna todos minusculos e maiosculos de a ate z
# re.findall('[a-zA-Z0-9_]','Henrique Bastos')# retorna conjunto de caracteres aceitaves de palavras
# re.findall('[\w]','Henrique Batstos')# codigo que representa a ate z, 0 ate 9, maius/minuscolas, e _
# # o \w acima naop precisa esta dentro de uma classe para funcionar, exemplo
# re.findall('\w', 'Henrique Bastos') # mesma forma da de cima 

# # #ESPECIAIS SEQUENCIAS
# # \d == [0-9] class de 0 ate 9
# # \D == [^0-9] classe negando caracretes de 0 ate 9
# # \s == [\t\n\r\f\v] clase de controles
# # \S == [^\t\n\r\f\v] classe negando  controle acima
# # \w == [a-zA-Z0-9_] clase buscando a ate z minusculo e maiusculo de 0 a 0 e andescor (_)
# #\W == [^a-zA-Z0-9_] classe negando a de cima
