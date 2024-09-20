"""
# Desafio: Happy Number (Número Feliz)
# Objetivo:
# Desenvolver um algoritmo que determine se um número é feliz. Um número é considerado feliz se, após uma série de operações, ele se transforma no número 1. Caso contrário, ele é infeliz.

# Definição de Número Feliz:
# Dado um número inteiro positivo, você deve:
# Separar os dígitos do número.
# Elevar cada dígito ao quadrado.
# Somar os resultados desses quadrados para formar um novo número.
# Repita o processo com o novo número gerado.
# Se o resultado em algum momento for 1, o número original é considerado feliz.
# Se o processo entrar em um ciclo (ou seja, começar a repetir números já gerados anteriormente), o número é considerado infeliz.
# Regras:
# O processo termina quando:
# O número chegar a 1 (feliz).
# Um ciclo for detectado (infeliz).
# Exemplos:
# Exemplo 1: O número 19 é feliz:

# 1² + 9² = 1 + 81 = 82
# 8² + 2² = 64 + 4 = 68
# 6² + 8² = 36 + 64 = 100
# 1² + 0² + 0² = 1 (feliz!)
# Exemplo 2: O número 4 é infeliz:

# 4² = 16
# 1² + 6² = 1 + 36 = 37
# 3² + 7² = 9 + 49 = 58
# 5² + 8² = 25 + 64 = 89
# 8² + 9² = 64 + 81 = 145
# 1² + 4² + 5² = 1 + 16 + 25 = 42
# O processo eventualmente repete 4, então o número 4 é infeliz.
"""
def sum_of_squares(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)    
    

def happy(number):
    box = []
    if number ==  4:
        return False
        
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1
    

    
assert sum_of_squares(130) == 10
assert all(happy(n) for n in (1,10,100,130,97))  
assert not all(happy(n) for n in (2,3,4,5,6,8,9))
    
            
    

