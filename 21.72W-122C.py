# A essência de teste

from functools import partial


def calc(a, b):
    return a + b

# Eu espero 3 quando calc(1, 2)


assert 3 == calc(1, 2)  # sabendo que calc(1, 2) = 3
# O assert toda vez que o valor for false ele informa mensagem de AssertionError ex:
# sabendo que calc(1, 1) = 2 aqui ele informa AssertionError
assert 2 == calc(1, 1)


# print('----------------------------------Exercício prátrico-------------------------------------')

'''
Exercício fizzbuzz
Regra do jogo:

Quando a posição é multipla de 3, fale fizz;
Quando a posição é multipla de 5, fale buzz;
Quando a posição for multipla de 3 e de 5, fale fizzbuzz;
Para todas as outras posições, fale o próprio número.
'''

# multiple_of = lambda base, num : num % base == 0
# multiple_of_3 = partial(multiple_of, 3)
# multiple_of_5 = partial(multiple_of,5)


# def robot(pos):
#     say = str(pos)

#     if multiple_of_3(pos) and multiple_of_5(pos):
#         say =  'fizzbuzz'
#     elif multiple_of_5(pos):
#         say =  'buzz'
#     elif multiple_of_3(pos):
#         say = 'fizz'

#     return say


# if __name__ == '__main__':
#     assert robot(1) == '1'
#     assert robot(2) == '2'
#     assert robot(4) == '4'

#     assert robot(3) == 'fizz'
#     assert robot(6) == 'fizz'
#     assert robot(9) == 'fizz'

#     assert robot(5) == 'buzz'
#     assert robot(10) == 'buzz'
#     assert robot(20) == 'buzz'
#     assert robot(15) == 'fizzbuzz'
#     assert robot(30) == 'fizzbuzz'
#     assert robot(45) == 'fizzbuzz'

print('-' * 60)
# print('------------------------------------------Exercício prático------------------------------------')
'''
Exercício: Divisor Game
Regras do jogo:

Quando a posição é múltipla de 4, diga "quad".
Quando a posição é múltipla de 6, diga "hex".
Quando a posição é múltipla de 4 e 6, diga "quadhex".
Para todas as outras posições, diga o próprio número.
'''


def multiple_of(base, num): return num % base == 0


multiple_of_4 = partial(multiple_of, 4)
multiple_of_6 = partial(multiple_of, 6)


# def multiple_of_4(num):
#     return num % 4 == 0
# a mesma função usando partial da from functools
# def multiple_of_6(num):
#     return num % 6 == 0


def robot1(pos):
    volt = str(pos)

    if multiple_of_4(pos) and multiple_of_6(pos):
        volt = 'quadhex'

    elif multiple_of_4(pos):
        volt = 'quad'

    elif multiple_of_6(pos):
        volt = 'hex'

    return volt


if __name__ == '__main__':
    assert robot1(1) == '1'
    assert robot1(2) == '2'  # sem multiplos
    assert robot1(5) == '5'

    assert robot1(4) == 'quad'
    assert robot1(8) == 'quad'  # multiplos de 4
    assert robot1(20) == 'quad'

    assert robot1(6) == 'hex'
    assert robot1(18) == 'hex'  # multiplos de 6
    assert robot1(18) == 'hex'

    assert robot1(12) == 'quadhex'
    assert robot1(24) == 'quadhex'  # multiplos de 4 e 6
    assert robot1(36) == 'quadhex'

# print('------------------------------------------Exercício prático------------------------------------')

                            # adicionado Try: except no começo depois progredir para _get_frame
# Exercício fizzbuzz
# Regra do jogo:

# Quando a posição é multipla de 3, fale fizz;
# Quando a posição é multipla de 5, fale buzz;
# Quando a posição for multipla de 3 e de 5, fale fizzbuzz;
# Para todas as outras posições, fale o próprio número.

# from functools import partial

                    
# def multiple_of(base, num): return num % base == 0


# multiple_of_3 = partial(multiple_of, 3)
# multiple_of_5 = partial(multiple_of, 5)


# def robot(pos):
#     say = str(pos)

#     if multiple_of_3(pos) and multiple_of_5(pos):
#         say = 'fizzbuzz'
#     elif multiple_of_5(pos):
#         say = 'buzz'
#     elif multiple_of_3(pos):
#         say = 'fizz'

#     return say


# def assert_equal(result,expected):
#     from sys import _getframe
    
#     msg = 'Fail: line {} got {} expecting {}'
    
#     if not result == expected:
#         current = _getframe()
#         caller = current.f_back
#         line_no = caller.f_lineno
#         print(msg.format(line_no, result, expected))
    
    


# if __name__ == '__main__':
#     assert_equal(robot(2), '2')
#     assert_equal(robot(1), '1')
#     assert_equal(robot(4), '4')

#     assert_equal(robot(3), 'fizz')

#     assert_equal(robot(6), 'fizz')
#     assert_equal(robot(9), 'fizz')

#     assert_equal(robot(5), 'buzz')
#     assert_equal(robot(10), 'buzz')
#     assert_equal(robot(20), 'buzz')
#     assert_equal(robot(15), 'fizzbuzz')
#     assert_equal(robot(30), 'fizzbuzz')
#     assert_equal(robot(45), 'fizzbuzz')

# print('--------------------Adicionando relatório-----aparti do 17:00----------------------------------------------------')

import unittest
from functools import partial





    
def multiple_of(base, num): return num % base == 0


multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(pos):
    say = str(pos)
    

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say



class FizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')
    
    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')
        
    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')
    
    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')
    
    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')
        
    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')

    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20),'buzz')
        
    def test_say_buzz_when_15(self):
        self.assertEqual(robot(15),'fizzbuzz')

    def test_say_buzz_when_30(self):
        self.assertEqual(robot(30),'fizzbuzz')

    def test_say_buzz_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')
        
if __name__ == '__main__':
    unittest.main()
    
    
        
        
        
        
 # -------- ESTE É O MESMO TEST DO TESTE-CLASS ACIMA POREM SEM USAR O IMPORT UNITTEST -----------

# def assert_equal(result,expected):
#     from sys import _getframe
    
#     msg = 'Fail: line {} got {} expecting {}'
    
#     if not result == expected:
#         current = _getframe()
#         caller = current.f_back
#         line_no = caller.f_lineno
#         print(msg.format(line_no, result, expected))
    
    


# if __name__ == '__main__':
#     assert_equal(robot(2), '2')
#     assert_equal(robot(1), '1')
#     assert_equal(robot(4), '4')

#     assert_equal(robot(3), 'fizz')

#     assert_equal(robot(6), 'fizz')
#     assert_equal(robot(9), 'fizz')

#     assert_equal(robot(5), 'buzz')
#     assert_equal(robot(10), 'buzz')
#     assert_equal(robot(20), 'buzz')
#     assert_equal(robot(15), 'fizzbuzz')
#     assert_equal(robot(30), 'fizzbuzz')
#     assert_equal(robot(45), 'fizzbuzz')

