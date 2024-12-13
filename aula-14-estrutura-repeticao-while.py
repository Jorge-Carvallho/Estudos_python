# Estrutura de repetição while(enquanto), estrutura(Teste lógico)

# for c in range(1,10):
#     print(c,end='')               # feito com for se souber limite
# print('FIM')


# c = 1
# while c < 10:
#     print(c,end='')               # feito com while se souber ou não souber limite
#     c +=1
# print('FIM')

# --------------------------------------------------------------------------------------

# for c in range(1,5):
#     n = int(input('Digite um valor: '))
# print('FIm')

# # --------------------------------------------
# n = 1
# while n != 0:       #--> flag = ponto de parada
#     n = int(input('Digite um valor: '))
# print('FIM')


# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continumar [S/n]: ')).upper()
# print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'números pares {par}, e números impares {impar}')
print('Acabou')