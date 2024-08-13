#EXPRESSÕES REGULARES


# codigo console --> fron re import match, search, findall <<=============

# import re
# # re.match ('abc','abc')  <----------------------
# # informa se a frase é iniciado com os caraceres buscados
#( match ele busca o padrão no inicio da frase ou palavra)

# # re.search('abc', 'ao longo da frase existe abc')      <----------------------
# # informa se ao longo da frase e encontrado o padrao
#(search ele busca o padrão ao londo da frase um palavra )

    
# 01 -------------------------------------------------------------------------------   
# padrao = 'abc'
# string = 'abc no começou da frase'

# resultado_macth = re.match(padrao,string)

# if resultado_macth:
#     print(f'A string {string} começa com o padrão')
# else:
#     print(f'A string {string} não comeca com padrão')
# 01---------------------------------------------------------------------------------


# 02 -------------------------------------------------------------------------------
# padrao =  'abc'
# string1 = '"A frase tem abc1abd9"'
# resultado_search = re.search(padrao, string1)

# if resultado_search:
#     print(f'A string {string1} contém abc padrão')
# else:
#     print(f'A string {string1} não contém abc padrão')
# 02
# ------------------------------------------------------------------------------------------


# 03-------------------------------------------------------------------------
# import re

# def verificar_padrao(padrao, texto):
#     if re.match(padrao,texto):
#         return True
#     elif re.search(padrao, texto):
#         return True
#     else:
#         return False
    
    
# def teste_verificar_padrao():
#     assert verificar_padrao('ddd','abcdf') == False
#     assert verificar_padrao('abc', 'a frase tem abc no meio') == True
#     assert verificar_padrao('abc', 'xyz') == False
#     assert verificar_padrao('','qualquer coisa') == True
#     assert verificar_padrao('abc', '' ) == False

#     print('Todos os testes passaram com sucesso')
    
# if __name__ == "__main__":
#     teste_verificar_padrao()
# # 03---------------------------------------------------------------------------------------
    
    
# 04-------------------------------------------------------------------------------------------
# retorna None se não aparecer no padrão definido
import re

resultado1 = re.findall('.','abc') # o . retorna qualque caracter exeto uma nova linha = \n
print(resultado1)

resultado2 = re.findall('.','acd')# o . retorna qualque caracter exeto uma nova linha = \n
print(resultado2)

resultado3 = re.findall('abc','acc')# retorna uma lista vazia pois não foi encontrado nenhum parametro definido 
if not resultado3 :
  print('Nenhum resultado encorntrado')
else:
    resultado = resultado3
    print(resultado3)
    
resultado4 = re.findall ('abc', 'abc123123abcjabc')
#(findall ele retorna uma lista com todas as ocorrências encontradas nesse padrão definido no primeiro parametro)
print(resultado4)
# 04------------------------------------------------------------------


# 05 -----------------------------------------------------------------------
padrao = 'abc'
texto = 'O rato abc roeu o abc do rei abcd23abc'
ocorencia = re.finditer(padrao, texto)
for match in ocorencia:
    start = match.start()
    end =  match.end()
    # print(f'ocorrencia encontrada no { match.group()}')
    print(f' posição no indice {start}-{end}')
# 05-------------------------------------------------------------------------------





# #ancoras de inicio e final de string  ^ e $ 
# # ^ ancora de inicio de linha
# findall('^.', 'abc\ndef\nghi') # retorna  o a pois ele nao percorre o \n informado acima, necessario usar uma flegue
# resulta = ['a']
# findall('^.', 'abc\ndef\nghi', re.MULTILINE) # retorna o primeiro de cada linha 
# resultado = ['a', 'd','g']
# # $ ancora de fim de linha
# findall('.$', 'abc\ndef\nghi') 
# #retorna o caracter final de cada linha
# findall('.$', 'abc\ndef\ncvg',re.MULTILINE)
# resultado = ['c', 'f','g']
# #retorna o caracter finald e cada linha percorrendo as linhas do \n

