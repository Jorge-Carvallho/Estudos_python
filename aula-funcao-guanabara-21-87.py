# ----------------->Docstrings<-------------------

def contador(i,f,p):
    '''
    Função criado por professor Guanabara apresentando uma Docstring
    Faz uma contagem e mostra na tela
    param --> i: início da contagem
    param --> f: fim da contagem
    param --> p: passo da contagem
    return --> sem retorno
    '''
    c = i
    while c <=f:
        print(f'{c} ',end='')
        c += p 
    print('Fim')
    
# contador(1,10,2)
# help(contador)

    #Parametro opcional

def somar(a,b,c=1):
    s = a+b+c
    print(f'A soma vale {s}')
    
somar(2,2,2)
somar(2,1)
print('-'* 30)

#--------------------------> Escopo de variáveis <---------------------------



# exemplo 1
def teste():
    x = 8
    print(f'Na função teste, (n) vale {n}')
    print(f'Na função teste (x) vale {x}')
    
    

n = 5  #mesmo n sendo definido fora do corpo da funcão, n esta no escopo global
print(f'No programa principal n vale {n}')
teste()
# print(f'No programa princial (x) vale {x}')----> a variavel x foi declarada no escopo local da função, então ela funcionara somente no escopo local da função
print('-'* 30)
# -------------------------------------------------------------------------------------------------

#exemplo 2
# caso eu precise ussar avariável de fora A como global, passo pra função global A
# com no exemplo comentado abaixo
def teste(b):
    global a 
    # a = 8 # esse A é local e vale 8, tenho a global que vale 5
    
    b+= 4  
    c = 2
    d = c + a
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')
    print(f'D dentro vale {d}, é soma de A global mas C local.')

a = 5
teste(a)
print(f'A fora vale {a}.')

# O B dentro passa  a valer 5 por que a variavel A é passada como parâmetro para B,
# se eu fizer uma mudança dentro de teste fazendo B = 6, B so vai mudar dentro da função
# teste ou seja, dentro do escopo local, pois b esta no escopo local, mas se eu não 
# atribuir nenhum valor a B e chamar A no programa principal (teste(a))---> 
# A variavel global atribui seu valor de A para como espelho para  B
# .... Os valores b B e C so funcionan sendo chamado dentro do corpo da função pois foram
# criados primeiros dentro da função, ou seja  escopo local
print('-'* 30)

def funcao():
    n1 = 4  # se não teclarra value sera n1 do escopo global = de fora
    print(f'N1 dentro da função vale {n1}, mas se não ouvesse atribuição aqui dentro, ' 
          'N1 seria uma copia de N1 de fora')
    
    print(f'n2 busca valor de fora que é 5 e n2 dentro agora é {n2}')


n1 = 2
n2 = 5
print(f'N1 fora da função vale {n1}.')
funcao()
print('-'* 30)
# ------------------------------------Retorno de valores-----------------------------------

# caso na chamada da função nao seja passado o valor, sera padrão zero como mostra a função
# estou returnando a soma dos valores e guadando em S, e retornando S, chamando a função somar que estar
# retornando S e guardando o valor em uma variável global r1,r2,r3, cada uma com seu próprio argumento
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(2,3,5)
r2 = somar(3)
r3 = somar(6)

print(f'Os resultados foram, {r1} para r1, {r2} para r2, {r3} para r3 ')
print('-' * 30)

# ----------------------------------Exercício prático da aula --------------------------------------

def fatorial(num=1):
    f = 1
    for c in range(num, 0 , -1):
        print(f'{c}x', end='')
        f *= c 
        
    return f

# n = int(input('Digite u número: '))
# print(f'O fatorial de {n} é {fatorial(n)}')

print(f' O fatorial de 5 é {fatorial(5)}')
print(f'O fatorial de 4 é {fatorial(5)} ')
print(f'O fatorial de 0 número é {fatorial(0)}')
# fatorial(5)
# fatorial(4)
# fatorial()
print('-'* 30)
# -----------------------------------------------------------------------------------------------

def par(num=0):
    if num % 2 == 0:
        return True
    else: 
       return False
   
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')


    






















