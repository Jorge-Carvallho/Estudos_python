# Exercício 104
# Crie um programa que tenyha a função leiaint(), que vai funcionar de forma semelhante a 
# função input() do python, so que fazendo a validação 
# para aceitar apenas um valor numérico.
# ex.
# n = leiaint('Digite um número: ')


# def leiaint(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input('Digite um número: ')) 
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print(f'\033[0;31mErro: Digite um número inteiro válido.\033[m')
#         if ok :
#             break
#     return valor

# n = leiaint('Digite Um número: ')
# print(f'Voce acabou de digitar o número {n}')

# ------------------------------------------------------------------

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            print('Erro: Digite um número valido')
            
        if ok == True:
            break
    return valor
            
            
n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}')