# A essência de teste

def calc(a,b):
    return a + b

# Eu espero 3 quando calc(1, 2)

assert 3 == calc(1, 2)# sabendo que calc(1, 2) = 3 
# O assert toda vez que o valor for false ele informa mensagem de AssertionError ex:
assert 2 == calc(1, 1) # sabendo que calc(1, 1) = 2 aqui ele informa AssertionError


print('----------------------------------Exercício prátrico-------------------------------------')

'''
Exercício fizzbuzz
Regra do jogo:

Quando a posição é multipla de 3, fale fizz;
Quando a posição é multipla de 5, fale buzz;
Quando a posição for multipla de 3 e de 5, fale fizzbuzz;
Para todas as outras posições, fale o próprio número.
'''
from functools import partial

multiple_of = lambda base, num : num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of,5)


def robot(pos):
    say = str(pos)
    
    if multiple_of_3(pos) and multiple_of_5(pos):
        say =  'fizzbuzz'
    elif multiple_of_5(pos):
        say =  'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    
    return say
        



if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'
    
    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'
    
    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'
    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
    
print('-'* 60)
print('------------------------------------------Exercício prático------------------------------------')
'''
Exercício: Divisor Game
Regras do jogo:

Quando a posição é múltipla de 4, diga "quad".
Quando a posição é múltipla de 6, diga "hex".
Quando a posição é múltipla de 4 e 6, diga "quadhex".
Para todas as outras posições, diga o próprio número.
'''



