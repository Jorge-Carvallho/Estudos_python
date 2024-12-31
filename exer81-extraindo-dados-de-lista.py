# Exercicio 81

# Crie um programa que vai ler Vários números e colocar em uma lista.depois disso mostre:
#     a)Quantos números froam digitados
#     b)A listas de valores, em ordem decrecente
#     c)Se o valor 5 foi digitado e está ou não na lista


lista= []


valor = int(input('Digite um valor: '))
lista.append(valor)
while True:
    continuar = input('Quer continuar [S/N]').strip().upper()

    if continuar != 'S':
        break
    else:
        valor = int(input('Digite um valor: '))
        lista.append(valor)
        
    

# quat_valores = len(lista)
# lista_reversa = lista.sort(reverse=True)
lista.sort(reverse=True) # modifica a lista original
print('=-'* 40)



print(f'Você digitou {len(lista)} elementos')
# print(f'Os valores em Orden decrescente são {sorted(lista, reverse=True)}') #cria uma nova lista
print(f'Os valores em Orden decrecente são {lista}')

if 5 in lista:
    print(f'O Valor 5 faz parte da lista')       
else:
    print('O valor 5 Não faz parte da lista')
