# Exercício
# Faça um programa que tenha uma função chamada contador(), que receba três parámetros : início, fim ,e passo a realizar a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a)De 1 até 10, de 1 em 1
# b)De 10 até 0, de 2 em 2
# c)Uma contagem personalizada
# OBS: from time import sleep faz o efeito com sleep com  o tempo (sleep(1.0) ou sleep(0.5))
# para ele mostrar resultado por resultado no tempo correto usar ,flush=True antes na execulção do programa


from time import sleep
def linha():
    print('-=-'* 20)
    
    

def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ',flush=True)
            sleep(0.3)
            cont += p 
        print('Fim!')
        linha()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.3)
            cont -= p
        print('Fim!')
    
    
    
    
    
    
linha()
contador(10,100,10)
contador(100,10,10)
linha()
print('Agora é sua vez depersonalizar a contagem')
init = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(init,fim,pas)