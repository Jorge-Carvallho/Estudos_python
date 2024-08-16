#Funções
# def f(): # função sem argumento
#     return 42
# print(f())

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

print('-----------------------------------')
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

