#Funções
# def f(): # função sem argumento
#     return 42
# print(f())
from time import sleep
def f(a,b,c): # posso pasar valor default também commo c='quinto', e apagar parámetro c Abaixo
    return a,b,c # função com argumentos onde a ordens dos parametros seguem ordens dos argumentos

print(f('Primeiro','Segundo','Terceiro'))
print(f(a='Primeiro', b='Segundo', c='Terceiro'))# também posso passar padrões nomeados
print('-------------------------------------\n')

# Parámetros não nomeados com *args
def f(a,b,c,*args):# * args é opção de pasar quantidade de parámetros indefinidos 
    print(a,b,c,args)

f('01', '02','03','--->','04','05','06', 'muitos')#todos os argumentos não referenciados atrelado ao (args) ficaram numa tupla ( nome args é uma convençao mas pode ser usados qualquer nome)
print('----------------------------------------\n')

#Parámetros quantidade inderteminadas nomeados fora do corpo da função (**kwargs o nome é uma conveção e pode ser usado qualquer nome)
def f(a,b,c,**kwargs):# os nome dos parámetros referenciados ao kwargs ficaram em um dicionário, não pode esquecer a referencia de pois dentro do dicionário eles se torna chave e valor
    print(a,b,c,kwargs)

f('A','B','C',nome='01', sobrenome='Omar',idade='igreja', p=20)

# OBS: posso colocar *args e **kwargs dentro da função, resultado que os sem nomeados seram tuplas e os referenciados seram dicionários
print('----------------------------------------\n')
#no danjo a chamada é fuiter com valor **lookups, vejamos

def filtro(**lookups):# lookups é nome valor de convenção
    for k,v in lookups.items():
        print(k.split('__'), v)

print(filtro(name__stars_with= "HEN", age__lt=30,
            city__endswith= 'rói'))

print('-----------------aqui------------------')
# Atribuição 
def f (*args, **kwargs):#Função de agrupas os valores nomeados e não nomeados, os nomeados passei de ula tupla para uma dict
    print(args, kwargs)
t= 'a','b','c','d'
d = dict(z='Z', w='W')
    
f(*t,**d)
    
print('-------------------\n')

def add(a, b):
    return a + b
import dis
print(add)#Objeto função
print(type(add))
print(add.__code__)#objeto código
print(add.__code__.co_argcount)# mostra quandos argumentosna função que nesse caso é a,b
print(add.__code__.co_code)#gera os bytecode são as esturções de nivel mas baixo execultado pelo hawdware do computador
print(add.__code__.co_name)#mostra o nnome da funcão
print(add.__code__.co_varnames)# mostra os nome dos valores das variaveis internas das funções
dis.dis(add)
print('---------------------------------------------------------\n')

def add(a, b):
    'Soma a com b'
    return a + b

# print(add)
# print(add.__doc__)
# help(add)

def calc(op, a, b): # função de calculadore que ja tem como padrão operacções com 2 parametros correto
    return op(a , b)

print(calc(add, 2, 3))


def mul(a, b):
    return a * b

print(calc(mul,2, 3))
print('------------------------------------------------1------------------------------------')

# Exercícios

# Exercício 1: Função com Parâmetros
# Crie uma função chamada descricao que aceite três parâmetros: nome, idade e cidade. A função deve retornar uma string no formato "Nome: [nome], Idade: [idade], Cidade: [cidade]". Teste a função com diferentes valores para cada parâmetro.

def descricao(nome,idade,cidade):
    return f'Nome: {nome} Idade: {idade} Cidade: {cidade}'

print(descricao('Jorge', '34 anos', 'Salvador,Bahia'))
print(descricao('Lais','33 anos', 'Salvador,Bahia'))
print('------------------------------------------------2------------------------------------')

# Exercício 2: Função com *args
# Escreva uma função chamada concatena que receba uma quantidade variável de strings usando *args e retorne uma única string que é a concatenação de todas as strings fornecidas. Teste a função com diferentes números de argumentos.

def concatena(*args):
    resultado = ''.join(args)
    return resultado.upper()

print(concatena('Olá ', ' ', 'Mundo'))
print(concatena('Python', ' ', 'é ', 'uma linguagem', ' ', 'incrivel'))

print('------------------------------------------------3-------------------------------------')
# Exercício 3: Função com **kwargs
# Crie uma função chamada informacoes que aceite um número variável de parâmetros nomeados usando **kwargs. A função deve exibir cada chave e valor do dicionário resultante. Teste a função com diferentes pares chave-valor.

def informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
        
        
informacoes(nome= 'Ana', idade=30, cidade='Rio de Janeiro')
print('-'* 60)


#  Função com Parâmetros Opcionais
# Crie uma função chamada dados_pessoais que aceite três parâmetros: nome, idade, e cidade, sendo que cidade tenha um valor padrão de "Desconhecida". A função deve retornar uma string no formato "Nome: [nome], Idade: [idade], Cidade: [cidade]".

# def dados_pessoais(**kwargs):
#     return f'Retornando {kwargs}'                 # errado 

# print(dados_pessoais(nome= 'jorge', idade= '35', cidade= 'salvador'))

            # ou
            
def dados_pessoais(nome='Desconhecido', idade='Desconhecida', cidade='Desconhecida'):
    return f'Nome: {nome}, Idade: {idade}, {cidade}'


print(dados_pessoais('Jorge', 35))
print('-'* 60)




# Teste com e sem o parâmetro cidade.
# Função com *args
# Escreva uma função chamada soma_numeros que aceite uma quantidade variável de números usando *args e retorne a soma de todos os números fornecidos.
def soma_numeros(*args):
    total = 0
    
    for numero in args:
        total += numero
        
    return total

print(soma_numeros(1,2,3,4))
print(soma_numeros(22,33))



# Teste a função com diferentes quantidades de números.
#Função com **kwargs
# Crie uma função chamada detalhes_produto que aceite um número variável de parâmetros nomeados usando **kwargs. A função deve exibir cada chave e valor do dicionário resultante, seguido da mensagem "Detalhes do produto:".
def detalhes_produto(**kwargs):
    for chave, valor in kwargs.items():
        
        print(f'Chave: {chave},  Valor: {valor}')
    
detalhes_produto(Arroz= 42, Melão=5.50, laranja=1.29)
print('-'* 60)
   


# Combinação de *args e **kwargs
# Escreva uma função chamada informacoes_completas que aceite três parâmetros obrigatórios nome, idade, cidade, e também permita passar parâmetros adicionais via *args e **kwargs. A função deve exibir o nome, idade, cidade, as informações adicionais e os parâmetros nomeados extras.

def informacoes_completas(nome, idade, cidade,* args, **kwargs):
    # sleep(0.9)
    print(f'Nome {nome}')
    print(f'Idade {idade}')
    print(f'Cidade {cidade}')

    if args:
        print(f'Informaçoes adicionais (args) {args}')

    if kwargs:
        print(f'Parâmetros nomeados (extras) {kwargs}')

informacoes_completas('Jorge',35,'Salvador', 'nenhuma informação', 'Nenhuma inforção01',  Animal='cahcorro', Lazer='Surf', Trabalho='motorista')
print('-'* 60)




# Função com Retorno Condicional
# Crie uma função chamada maior_menor que receba dois números como parâmetros e retorne qual número é maior ou se são iguais.
def maior_menor(numero1, numero2):
    valor_1 = int(numero1)
    valor_2 = int((numero2))
    if valor_1 > valor_2:
        return f'O valor 1ª que é, ({valor_1}) é maior que o valor 2ª que é ({valor_2})'
    elif valor_2 > valor_1:
        return f'O valor 2ª que é  ({valor_2}) é maior que o valor 1ª que é {valor_1}'
    else:
        return f'Os valor 1ª que é, ({valor_1}) e valor 2ª que é, ({valor_2}) são iguais'
        
print(maior_menor(2,4))
print(maior_menor(6,8))
print(maior_menor(6,6))
        
        
        

# Função com Operações
# Escreva uma função chamada operacao que receba dois números e uma operação aritmética (como string: '+', '-', '*' ou '/') e retorne o resultado da operação entre os dois números. Use uma função anônima lambda dentro da função principal para realizar as operações.


                    # falta resolver



# Função com Ordenação
# Crie uma função chamada ordena_strings que aceite uma quantidade variável de strings usando *args e retorne uma lista dessas strings ordenadas em ordem alfabética.

def ordena_Strings(*args):
    lista_ordenada = list(args)
    lista_ordenada.sort()
    return print(lista_ordenada)

ordena_Strings('h','a','b','e')


# Função com Filtros
# Escreva uma função chamada filtro_pessoas que aceite um número variável de parâmetros nomeados usando **kwargs. A função deve filtrar e exibir pessoas que têm idade maior que 18 anos.
def filtro_pessoas(**kwargs):
    for nome, idade in kwargs.items():
        try:
            idade = int(idade)
            if idade >= 18:
                print(f'Nome é {nome},  a idade é {idade}')
        
        except ValueError:
            print(f'Idade nao possivel converter {idade}')   

       


filtro_pessoas(evandro=33, Isa=18, carlos=16)
filtro_pessoas(jorge=22, maria=17, pedro=25)
print('-'* 60)




# Função com Contagem
# Crie uma função chamada conta_vogais que aceite uma string como parâmetro e retorne a quantidade de vogais (a, e, i, o, u) que aparecem na string.
texto = 'inconstitucionalissimamente'
def conta_vogais(palavra):
    vogais = 0
    for letra in palavra:
        if letra.lower() in ('aeiou'):
            vogais += 1 
    return vogais
        
        
print(conta_vogais(texto))

# Função Recursiva
# Escreva uma função recursiva chamada fatorial que receba um número como parâmetro e retorne o fatorial desse número.

def fatorial(valor):
    if valor == 0 or valor == 1:
        return 1
    else:
        return valor * fatorial(valor -1)
    
print(fatorial(5))
print('-'* 60)

# Soma de Dois Números
# Crie uma função chamada soma que aceite dois números como parâmetros e retorne a soma deles.
def soma(valor1,valor2):
    resultado = valor1 + valor2 
    return f'A soma de {valor1} mais {valor2} é: {resultado}'


print(soma(1,2))






# Verificar Número Par
# Crie uma função chamada eh_par que aceite um número como parâmetro e retorne True se o número for par e False caso contrário.
def sera_que_e_par(numero):
    if numero % 2 == 0:
        print('Numero par ---> True')
    else:
        print('Numero impar ---> False')
        
        
        
sera_que_e_par(56)
sera_que_e_par(55)
sera_que_e_par(1)
print('-'* 60)


# Calcular Fatorial
# Crie uma função chamada fatorial que calcule o fatorial de um número. Lembre-se que o fatorial de 0 e 1 é 1.
def fatorial1(valor):
    if valor == 0 or valor == 1:
        return 1 
    else:
        return valor * fatorial(valor -1)
        
    
    
print(fatorial(5))





# Inverter uma String

# Crie uma função chamada inverter_string que aceite uma string como parâmetro e retorne a string invertida.
# Contar Vogais em uma String

# Crie uma função chamada contar_vogais que aceite uma string e conte quantas vogais (a, e, i, o, u) estão presentes.
