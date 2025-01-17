#Dockstrings
# def contador(i,f,p):
#     """Faz uma contagem e mostra na tela:
#     -i : inicio da contagem
#     -f : fim da contagem
#     -p : passo da contagem
#     return: sem retorno/com impressão
#     """
#     print(f'De {i} até {f} de {p} em {p} resulta em, ',end=' ')
#     c = i
#     while c <=f:
#         print(c,end=' ')    
#         c +=p
#     print('Fim!')
    
    
# i = int(input('Inicio: '))
# f = int(input('Fim: ' ))
# p = int(input('Passo: '))


# contador(i,f,p)

# help(contador)# chamada da dockstring com help(nome a def ou outros)

# -------------------------------------------------------------------------------------------------------
                                    # parametros opcionais
# def somar(a,b,c=0):   
#     s = a+ b+ c
#     print(f'a soma é {s}')

# somar(1,3,2)
# somar(2,8)# 3ª parametro esta opcional da definição da def, c=0

# --------------------------------------------------------------------------------------------------------------

# Escopô de variavel
# def teste():
#     x = 8  # -----------------------------------> (x) tem escopo local, so funciona dentro da função
#     print(f'Na funçao teste n vae {n}')
#     print(f'Na função teste x vale {x}')

# # Programa principal
# n = 2    #------------------------------------> (n) esta no escopo global
# teste()

# ------------------------------------------------------------------------------------------------------------

# def teste(b):
#     a = 8
#     b += 4  #como (b) não tem definição a variável global de a passo pra (b) também copiada
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'A dentro vale {b}')                     
#     print(f'A dentro vale {c}')


# a = 5 
# teste(a)
# print(f'a fora vale{a}')

# print('-------')
# -------
# usando variavel a como global

# def teste(b):
#     global a
#     b += 4  #como (b) não tem definição a variável global de a passo pra (b) também copiada
#     c = 2
#     print(f'A dentro vale {a} por que usa a variavel global, ou seja de fora')
#     print(f'A dentro vale {b}')                     
#     print(f'A dentro vale {c}')


# a = 5 
# teste(a)
# print(f'a fora vale{a}')
# --------------------------------------------------------------------------------------------------

# def funcao():
#     n1 = 4
#     print(f'n1 dentro vale, {n1}')

# n1 = 2
# funcao()
# print(f'n1 fora vale, {n1}')
# ------------------------------------------------------------------------------

# Retorno de valores

# def somar(a=3,b=4,c=2):
#     s = a+ b+ c
#     return s

# r1 = somar(2,1,5)
# r2 = somar(2,1)
# r3 = somar(2)
# print(f'Meus calculos deram {r1}, {r2}, {r3}')
# -----------------------------------------------------------------------------------------

# def fatorial(num=1):
#     f = 1
#     for c in range(num,0,-1):
#         f*=c
#     return f

# # n = int(input('Digite um Número: '))
# # print(fatorial(n))
# # print(f'O fatorial de {n} é {fatorial(n)}')
# # ------------ou-----------------

# f1 = fatorial(5)
# f2 = fatorial(7)
# f3 = fatorial()

# print(f'Os resultados são {f1}, {f2}, {f3}')
# ----------------------------------------------------

def par(n = 0):
    if n% 2 == 0:
        return True
    return False
    
num = int(input('Digite um número: '))
if par(num):
    print('E par')
else:
    print('Não é par')


