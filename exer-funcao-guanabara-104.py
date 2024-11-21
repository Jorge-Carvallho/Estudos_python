# Exercício
# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do python
# Só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:




def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido')
        if ok:
            break 
            
    return valor




n = leiaInt('Digite um número ')
print(f'Você acabou de digitar o número {n}')