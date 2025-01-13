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