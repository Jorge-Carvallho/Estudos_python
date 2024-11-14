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

def teste(b):
    a = 8 # esse A é local e vale 8, tenho a global que vale 5
    
    b+= 4  
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

# O B dentro passa  a valer 5 por que a variavel A é passada como parâmetro para B,
# se eu fizer uma mudança dentro de teste fazendo B = 6, B so vai mudar dentro da função
# teste ou seja, dentro do escopo local, pois b esta no escopo local, mas se eu não 
# atribuir nenhum valor a B e chamar A no programa principal (teste(a))---> 
# A variavel global atribui seu valor de A para como espelho para  B
# .... Os valores b B e C so funcionan sendo chamado dentro do corpo da função pois foram
# criados primeiros dentro da função, ou seja  escopo local
print('-'* 30)

def funcao():
    n1 = 4
    print(f'n1 dentro da função vale {n1}')
    global n2 +=1
    print(f'n2 busca valor de fora que é 5 e n2 dentro agora é {n2}')


n1 = 2
n2 = 5
print(f'n1 fora da função vale {n1}')
funcao()