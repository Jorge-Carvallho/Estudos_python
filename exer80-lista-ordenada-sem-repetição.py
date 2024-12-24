# Exercício 80
# Crie um programa onde o usuário possa digitar cinco valores numnéricos e cadastra-0s em uma lista
# já na posição correta de inserção(sem usar o sort().
# No final mostre uma a lista ordenada na tela.


lista = []

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1 

  
        
print(lista)




        
        
        
# valores = list()
# for valor in range(0,5):
#     valores.append(int(input('Digite um valor: ')))  





# print(valores)