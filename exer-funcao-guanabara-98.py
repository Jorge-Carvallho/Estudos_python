# Exercício
# Faça um programa que tenha uma função chamada contador(), que receba três parámetros : início, fim ,e passo a realizar a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a)De 1 até 10, de 1 em 1
# b)De 10 até 0, de 2 em 2
# c)Uma contagem personalizada


from time import sleep
def linha():
    print('-=-'* 20)
    
def contador(i,f,p):
    if p == 0:
        p = 1
    elif p < 0:
        p = abs(p)   #Função abs() retorna valor positivo ex. abs(-5) = 5 
        
    resultado = []

    if i < f:
        while i <= f:
            resultado.append(i)
            i += p
            
    else:
        while i >= f:
            resultado.append(i)
            i -= p
            
            
    return resultado
        

assert contador(1, 10, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert contador(1,5,1) == [1,2,3,4,5]
assert contador(10,50,10) == [10,20,30,40,50]

assert contador(50,10,-10)
    

# --------------------Já resolvido sem assert---------------------

# def contador(i,f,p):
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     if p < 0:
#         p*= -1
#     if p == 0:
#         p = 1
#     cont = i
#     if i < f:
#         while cont <= f:
#             print(f'{cont}', end=' ',flush=True)
#             sleep(0.3)
#             cont += p 
#         print('Fim!')
#         linha()
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont}',end=' ',flush=True)
#             sleep(0.3)
#             cont -= p
#         print('Fim!')
    

    
# linha()
# contador(10,100,10)
# contador(100,10,10)
# linha()
# print('Agora é sua vez de personalizar a contagem')
# init = int(input('Inicio: '))
# fim = int(input('Fim:    '))
# pas = int(input('Passo:  '))
# contador(init,fim,pas)