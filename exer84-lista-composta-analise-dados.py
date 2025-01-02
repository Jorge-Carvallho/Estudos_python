# Exercício 84
# Faça um programa que leia nome,e peso de Várias pessoas guardando tudo em uma lista,
# no final mostre:
#     a)Quantas pessoas foram cadastradas
#     b)Uma listagem com pessoas mais pesadas
#     c) uma listagem com as pessoas mas leves


galera = []
cont = 0
pesomaior = pesomenor = pesonormal = 0
listapesomaior = []
listapesomenor = []


while True:
    lista = []
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    galera.append(lista[:])
    cont+=1
    continuar = input('Deseja continuar [S/N]').strip().upper()
    if continuar != 'S':
        break
for p in galera:
    if p[1] >=  85:
        pesomaior +=1
        listapesomaior.append(p[0])
        
    elif p[1] <= 70:
        pesomenor += 1
        listapesomenor.append(p[0])
    else:
        pesonormal += 1


print(f'A quantidade de pessoas cadastradas foram {cont}') 
    
print(f'As pessoas mas pesadas foram {pesomaior} e foram {listapesomaior}')

print(f'As pessoas mas leves  foram {pesomenor} e foram {listapesomenor}')


# ---------------------------------------resolução--------------------------------------------


temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1] # se não tem niguem guardado em peso maior e menor passa a ser zero
    else:
        if temp[1] > maior:
            maior = temp[1]
            
        if temp[1] < menor:
            menor = temp[1]
            
            
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar [S/N]: ').strip().upper()
    if resp != 'S':
        break
    
print('-='*25)
print(f'A quantidade de pessoas cadastradas foram {len(princ)}')
print(f'O maior peso foi de {maior} kg. Peso de ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print()

print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')        

print()





    
    



