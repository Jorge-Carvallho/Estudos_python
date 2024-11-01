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

def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1,7) if number < 10 else happy(next_)
    
     
     
     
assert all(happy(n) for n in (1,10,100,130,97))
assert not all(happy(n) for n in (2,3,4,5,6,8,9))
#    Esse teste importo a function happy e no console testo quais números são felizes
# >>> from happy_functions import happy
# >>> [(n,happy(n)) for n in range(1,10)]
# [(1, True), (2, False), (3, False), (4, False), (5, False), (6, False), (7, True), (8, False), (9, False)]