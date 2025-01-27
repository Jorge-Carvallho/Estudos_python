# Exercício 102
# Crie um programa que tenha a função fatorial() que receba dois parâmetros:
#     - o primeiro que indica o número a calcular e o outro chamado show
#     - indique se será mostrado ou não na tela o processo de cálculo do fatorial


def fatorial(num=1,show=False):
    f = 1
    for c in range(num, 0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print( 'x',end='')
            else: 
                print(' = ', end='')
        f*= c
    return f'O fatorial de {num} é {f}'


print(fatorial(4,show=True))
print(fatorial(5))
print(fatorial(6))
print(fatorial(6,show=False))
print(fatorial(6,show=True))