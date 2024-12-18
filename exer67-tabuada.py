# Exercício 67
# Faça um programa que mostre uma tabuada e varios números, um de cada vez, 
# para cada valor digitado pelo usuário, o programa sera interronpido
# quando o número solicitado for negativo.

# ---------------------------usando for --------------------------------
cont = 0
num =  int(input('quer ver a tabuada de qual valor: '))
while  num > 0:
    for i in range(1,11):
        print(f'{num} x {i} = {num * i}')
    num =  int(input('Quer ver a tabuada de qual número agora: '))
    if num < 0:
        break
    
    
#  --------------------------------usando while -----------------------------
    
    

# cont = 0
# num = int(input('Digite o número da tabuada: '))
# while True:
#     if num < 0:
#         print('Programa encerrado: ')
#         break

#     cont = 0
#     while cont <= 10:
#         resultado  = num * cont
#         print(f'{num} x {cont} = {resultado}')
#         cont += 1 
#     num = int(input('Digite o número da tabuada: '))
#     print()
    
    
    
    
    
    
    
    
