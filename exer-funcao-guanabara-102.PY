#Exercício
# Crie um programa que tenha função fatorial() que receba 2 parâmetros:
# o primerio que indica o número a calcular e o outro chamado show, que será um valor lógico(opcional)
# indicando se será mostrado ou não na tela e o processo de cálculo do fatorial

def fatorial(n=1, show=False):
    '''
    --> Calcule o fatorial de um número.
    -Parâmetro n: O número a ser calculado
    -Parâmetro show: (pcional) Mostra ou não mostra a conta.
    -return: O valor do Fatorial de um número n
    '''
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print(' = ', end='')
        f *= c
        
    return f'O fatorial de {n} é {f}'
    
        
print(fatorial(4,show=True))
    
print(fatorial(5))
print(fatorial(6))
print(fatorial(7,show=False))
# help(fatorial)




assert fatorial(5) == f'O fatorial de {5} é {120}'
assert fatorial(6) == f'O fatorial de {6} é {720}'      
assert fatorial(7,show=False) == f'O fatorial de {7} é {5040}'
assert fatorial(4,show=True) == f'O fatorial de {4} é {24}'
        
    

        
  


        
    
        



       

        
       
            
            
            
        
