#Decisões e Expressôes Lógicas if/else
nome = 'Henrique'
for c in nome:
    # if c in ('e','i','u'): # As 3 formas estão corretas 
    # if c in 'eiu':
    if c == 'e' or c == 'i' or c == 'u':# caso tenha as letras da condição estou colocando elas em maiúsculas
        print(c.upper())
    elif c == 'q':# coloquei outra condição que caso tenha a letra (q) irar trocar po @
        print('@')
    else:
        print(c)
print('------------------------------------------------')
        
        
        
#No python tudo que for vazio ou 0 é falso, exemplos:
print(bool(0))
print('dicionário',{})# dicionario vazio é falso
print('tupla',())# tupla vazia é falso
print('lista',[])#  lista vazia é falso


# No and retorna o último avaliado 
True and 'abc'# retorna 'abc'
'abc' and True # retorna True 
False and 'abc'# qualquer verificação and que tenha False o retorno séra False

# No or retorna o primeiro avaliado
# O operador (or) umas das expressões tem que ser verdadeiro, ou seja caso apenas uma seja verdadeiro ele retorna
True or 'abc'# retorna True
'abc' or True# retorna abc
False or 'abc'# retorna abc //// aqui como a primeiro é falso ele vai conferir se a segunda é verdadeira e retorna caso seja
'abc' or False# retorna abc //// aqui a primerio ja é verdadeira então ele já retorna sem necessariamente avaliar a segunda
print('-----------------------------------------')
# Exercício de Fixação
#Verificar Vogais:

#Verifique cada letra da palavra e, se for uma vogal (a, e, i, o, u), troque-a por maiúscula. Caso seja uma consoante, troque por um símbolo específico (@ para consoante).
palavra = 'endometriose'
for letra in palavra:
    if letra in 'aeiou':
        print(letra.upper(), end='-')# end= a '' por padrão é \n, então ele sem espaço não pula linha ou posso adicionar algum caracter pra ser imprimido após cada execulção como acima
    else:
        print('@', end='-')
        
   
print()
print('----------------')
        
        
#Verificação de Paridade:
#Verifique se o número é par ou ímpar usando if/else.
#Verificação de Entrada:
numero = 2
if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')
    
print('---------------------')
    
     

#Verifique se a entrada é um número positivo, negativo ou zero.
entrada = 0
if entrada > 0:
    print('número positivo')
elif entrada < 0:
    print('número negativo')
else:
    print('Número é zero')

print('--------------------')


#Validação de Senha:
#Peça ao usuário para inserir uma senha.
#Verifique se a senha contém pelo menos um número, uma letra maiúscula e uma letra minúscula.
#Verificação de Vazio:
import re
senha = ' coiSa2'
if (re.search(r'[A-Z]', senha) and
    re.search(r'[a-z]', senha) and
    re.search(r'[0-9]', senha)):
    print('A senha é valida')
else:import re
senha = 'elemento'
if (re.search(r'[A-Z]', senha) and
    re.search(r'[a-z]', senha) and
    re.search(r'[0-9]'), senha):
    print('A senha é valida')
else:
    print('A senha não atende  os requisitos')
   
print('---------------------------------')
    

#Insera três valores: um número, uma lista e uma string.
#Verifique se cada um desses valores é vazio ou não usando a função bool.
valores = 2,['listinha'],'string'

numer = 2
lista = []
letra = 'd'
print(f'Número {'vazio' if not numer else 'Não está vazio'}')
print(f'A lista  {'vazia' if not lista else'Não está vazia'}')
print(f'A letra  {'vazia'if not letra else 'Não está vazia'}')
#Expressões Lógicas:
#Insira dois valores booleanos (True ou False).
#Avalie expressões usando and e or e mostre os resultados.
valor1 = True
valor2 = False
#and
resultaddo_and_1 = valor1 and valor2
resultaddo_and_2 = valor1 and valor1
#or
resultaddo_or_1 = valor1 or valor2
resultado_or_2  = valor2 or valor2

print(f'Resultado de {valor1} and {valor2} é {resultaddo_and_1}')
print(f'Resultado de {valor1} and {valor1} é { resultaddo_and_2}')
print(f'Resultado de {valor1} or {valor2} é {resultaddo_or_1}')
print(f'Resultado de {valor2} or { valor2} é { resultaddo_and_1}')