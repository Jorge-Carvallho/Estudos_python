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

print('----------------------------------1------------------------------------')
#  Exercícios Expressões Regulares

# Exercício 1. Verificar Início da String
# Escreva uma função que verifique se a frase começa com o padrão "começou". A função deve receber uma string e retornar uma mensagem indicando se a string começa com o padrão ou não.
# def verifica_inicio(s):
#     padrao = 'comecou'
   
#     if re.match(padrao,s):
#         print('frase comecou no padrão')
#     else:
#       print('Nao comecou no padrão')   # verificar se alguma frese ou a string está comecando com a palavra

# verifica_inicio('comecou')
# verifica_inicio('comecou agora')
# verifica_inicio('agora comecou')
# verifica_inicio('Comecando')

print('----------------------------------------------2-----------------------------------------')
# Exercício 2. Buscar Padrão em Qualquer Parte da Frase
# Escreva uma função que verifique se o padrão "abc" aparece em qualquer parte da frase. A função deve retornar uma mensagem informando se o padrão foi encontrado ou não.
def verificar_padrao(frase):
    padrao1 = 'apareceu'
    if re.search(padrao1,frase):
        print('A palavra apareceu sim em algum local')
    else:
        print('Ainda não apareceu')
    

verificar_padrao('A palavra ainda não apare.. mas vai aparecer')
verificar_padrao('A palavra quase aparec... mas ainda não')
verificar_padrao('Agora sim a palavra apareceu apareceu rsrsrs')
verificar_padrao('olhar, ir, palavra, aparecer, apareceu')

print('------------------------------------------------3----------------------------------------')

# Exercício 3. Encontrar Todas as Ocorrências
# Crie uma função que receba uma frase e encontre todas as ocorrências do padrão "python". A função deve retornar uma lista com todas as ocorrências encontradas.
def ocorrencia(s): 
    aparicoes = []
    padrao2 = 'python'
    resultados = re.findall(padrao2, s, re.IGNORECASE)# o IGNORECASE ele ignora as palavras maiúsculas ou minúsculas
    if resultados:
        aparicoes.extend(resultados)
        
    else:
        print('Não ouve aparicoes da palavra')
        
    return aparicoes
        
print(ocorrencia('Pensei de ter vista a palavra Pyth..'))
print(ocorrencia('Mais uma vez pensei em ter visto a palavra python, mas não era a palavra'))
print(ocorrencia('Dentro de Python, tem varias coisas, python é python, e quem domina python é fera'))

print('------------------------------------------4------------------------------------------------')


# Exercício 4. Posição das Ocorrências
# Crie uma função que retorne as posições onde o padrão "abc" aparece na frase. A função deve retornar uma lista de tuplas com as posições de início e fim de cada ocorrência.
def posicoes(s):
    aparicoes_1 = []
    padrao3 = 'abc'
    
    for match in re.finditer(padrao3,s,re.IGNORECASE):
        inicio = match.start()
        final = match.end()
        grupo = match.group()
        aparicoes_1.append((inicio,final,grupo))
        
    return aparicoes_1 
    
print(posicoes('Dentro de abc, tem muitos, abc nas palaabcvas'))
print(posicoes('abc no incio abc no fim, com muitos abcs, o abc e abcis, abc'))

print('---------------------------------------------------5-------------------------------------')

# Exercício 5. Verificar Início e Fim da Frase
# Escreva uma função que verifique se a frase começa com o padrão "abc" e termina com o padrão "xyz". A função deve retornar um dicionário indicando se a frase começa ou termina com os padrões.

def verificar(frase1):

    padrao_inicial = 'abc'
    padrao_final = 'xyz'

    aparicoes_2 = {
        
        'comeca_com_abc': frase1.startswith(padrao_inicial),
        'termina_com_xyz': frase1.endswith(padrao_inicial)
    }
    
    return aparicoes_2
    
    
print(verificar('abc algo xyz'))
print(verificar('abc algo'))
print(verificar('algo xyz'))
print(verificar('algo algo'))
print(verificar('xyz abc'))

print('')
print('-------------------------------OUtra forma-------------------------------- ')
print('')

def verificar_ancoras(frase):
    padrao_inicial = 'abc'
    padrao_fim = 'xyz'

    comeca_com_padrao = bool(re.search(f'^{padrao_inicial}', frase))
    termina_com_padrao = bool(re.search(f'{padrao_fim}$', frase))

    return {
        'começa_com_padrao':comeca_com_padrao,
        'termina_com_padrao':termina_com_padrao
        
    }


print(verificar('abc algo xyz'))
print(verificar('abc algo'))
print(verificar('algo xyz'))
print(verificar('algo algo'))
print(verificar('xyz abc'))