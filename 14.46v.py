#Meta caracter
import re
# o ponto represneta qualquer caracter exwto o \n (nova linha)
print(re.match('.','\n'))# ponto retorna qualque caracter ao menos \n retorna none
print(re.search('.','\nabc'))# ponto no search apos o \n ele busca outra ocorrência e encontra neste caso
print(re.findall('.','')) # ponto aqui retorna uma lista vazia ou com as ocorrências em  [ ]


# #ancoras de inicio e final de string  ^ e $ 
# # ^ âncora de inicio de linha
# # $ âncora de final de linha

print(re.findall('^.', 'abc\ndef\nghi')) # retorna --> a <-- pois ele  percorre até antes do \n ou seja, até aquela linha, para ele outrapassar p \n,usar flag re.MULTILINE, ele passarar a corresponder ao início de cada linha
# resulta = ['a']
# findall('^.', 'abc\ndef\nghi', re.MULTILINE) # retorna o primeiro de cada linha 
# resultado = ['a', 'd','g']
#----------------------------------------------------------------------------------------------------

# use | para Or   <-- para (ou):
print('aqui v')
print(re.match('a|b', 'bc'))# o Or pode ser usado em qualque verificação de expressão no match, search, findall...
# or é uma condição normal que caso não tenha  --> a <--  verifique se tem --> b <-- : exemplo acima




# # $ âncora de fim de linha
# findall('.$', 'abc\ndef\nghi') 
# #retorna o caracter final de cada linha
print(re.findall('.$', 'abc\ndef\ncvg',re.MULTILINE))
# resultado = ['c', 'f','g']
# #retorna o caracter finald e cada linha percorrendo as linhas do \n
# ------------------------------------------------------------------------------------------------------
#ângora de inicia e final juntas
print(re.match('^.$','a'))# retorna padrão de apenas um caracter








 



















