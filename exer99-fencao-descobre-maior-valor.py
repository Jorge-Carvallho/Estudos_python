# Exercício 99
# Faça um porgrama que tenha uma função chamada maior(), que receba varios parâmetros
# como valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior


def maior(*num):
    msg = '---> Não foi informado nunhum valor <---'
    cont = maior = 0
    print('Analisando valores passados...')

    if len(num) == 0:
        print(msg)
        return msg
    for valor in num:
        print(f'{valor}',end=' ')

    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    cont +=1
    print(f'{cont}')
    print(f'{maior}')
    
    return maior
        

        
        

maior(1,2,7,3,6,3,5,7)