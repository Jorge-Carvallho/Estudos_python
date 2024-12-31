

galera = []

cont = 0

while True:
    lista = []
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    galera.append(lista[:])
    cont+=1
    continuar = input('Deseja continuar [S/N]').strip().upper()
    if continuar != 'S':
        break
    

    
print(f'A quantidade de pessoas cadastradas foram {cont}') 
    

print(galera)