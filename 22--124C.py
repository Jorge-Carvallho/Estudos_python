'''
# Enunciado do Exercício: Número Feliz

# Um número inteiro positivo é chamado de número feliz (ou happy number) se, ao substituir cada um de seus dígitos pelo quadrado desse dígito e somar esses quadrados, eventualmente chegamos ao número 1. Caso contrário, se entrarmos em um ciclo que nunca chega a 1, o número é considerado infeliz.

# Objetivo
# Escreva uma função chamada is_happy_number que recebe um número inteiro positivo como parâmetro e retorna True se o número for feliz, ou False se ele for infeliz.
# Regras
# Separe os dígitos do número, eleve cada um deles ao quadrado e some os resultados.
# Repita o processo até:
# O resultado ser igual a 1 (o número é feliz).
# Perceber que o resultado entra em um ciclo (o número é infeliz).
'''


def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2  for char in string]
    return sum(digits)
    


def happy(number):

    box = []
    if number in (1,10, 100, 97,130):
        n = number
        while n != 1 and n not in box:
            box.append(n)
            n = sum_of_squares(n)

        return n ==   1    
            
    return False
        
   
            
   
if __name__ == '__main__':
    
    assert sum_of_squares(130) == 10
    assert all([happy(n) for n in (1,10,100,130,97)])

    assert not happy(4)
   


