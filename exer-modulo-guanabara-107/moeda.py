#Exercício
# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(),diminuir(),
# dobro(), e metade().
# Faça também um programa principal que importe esse módulo e use algumas dessas funções
import decimal
def metade(n):
    n /= 2 
    return f'{n:g}'


def dobro(n):
    n *= 2
    return f'{n:g}'


def aumentar(n):
    n *= 1.40
    return f'{n:g}'
    

def reduzir(n):
    n *= 0.80
    return f'{n:g}'






