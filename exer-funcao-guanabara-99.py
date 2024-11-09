# Exercício
# Faça um, programa que tenha uma função chamada maior(), que receba varios parametros como valores inteiros.
# Seu programa tem que avaliar todos os valores e dizer qual deles é o maior
from time import sleep

def linha():
    print('-=-'* 20)


def maior(*num):
    print('-=-' * 20)
    msg = '---> Não foi informado nenhum valor <---'
    cont = maior = 0
    print('Analisando os valores passados...')
    
    if len(num) == 0:
        print(msg)            #verifica se valor não foi passado informa --> msg
        return msg
    
        
    for valor in num:
        print(f'{valor}', end=' ',flush=True)
        sleep(0.4)            # para cada valor de número
        
        if cont == 0:     
            maior = valor     
        # partindo do principio que cont e maior são zero, caso seja informado (apenas um número)
        # o maior valor passarar a ser o número informado 
        else:
        # se não...
        # se valor passsado agora for maior do que o antigo atual, o maior passarar a ser
        # o maior agora
            if valor > maior:
               maior = valor
        cont += 1
            
            
    print(f'\nForam informados --> {cont} valores ao todo')
    print(f'O maior valor é --> {maior}')
            
    return maior
        

assert maior(23,4,5,6,7,32,5) == 32
assert maior(23,1,1,6,7,31,7) == 31
assert maior(4,5,8,2,9,) == 9
assert maior(0) == 0
assert maior() == '---> Não foi informado nenhum valor <---'