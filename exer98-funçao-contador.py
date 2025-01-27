# Exercício 98
# Faça um porgrama que tenha um afunçãochamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três comtagens através da função criada
#     a)De 1 até 10, de 1 em 1
#     b)De 10 até 0, de 2 em 2
#     c)Uma contagem personalizada


from time import sleep

def linha():
    print('-='*30)

def cont_1_10():
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1,11,1):
        sleep(0.2)
        print(c, end=' ')
    print('FIM!')
    print()

def cont_10_0():
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10,-1,-2):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')
    print()


def contador(i,f ,p):
    if p < 0:
        p *=1
    if p == 0:
        p = 1
    if i <= f:
        c = 1
        while c <= f:
            c += p
            print(c,end=' ')
        print()
    else:
        c = i
        while c >= f:
            print(c,end=' ')
            c -= p
    print('FIM')

        





#Programa Principal
linha()
cont_1_10()
linha()
cont_10_0()
linha()
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(i,f,p)

# ------------------------------------------------------resolução--------------------------------------


# def contador(i,f,p):
#     if p < 0:
#         p *=1
#     if p == 0:
#         p = 1
#     print(f'A contagem de {i} até {f} de {p} em {p}.')
#     if i < f:
#         c = 1
#         while c <= f:
#             sleep(0.3)
#             print(c, end=' ')
#             c += p
#         print('FIM!')
#     else:
#         c = i
#         while c >= f:
#             sleep(0.3)
#             print(c,end=' ')
#             c -= p
#         print('FIM!')
       

    
    
# contador(1,10,1)
# contador(10,0,2)
# i = int(input('Inicio:  '))
# f = int(input('Final: '))
# p = int(input('Passo: '))
# contador(i,f,p)