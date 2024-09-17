"""
Resgras do fizbuzz
01 Se a posição for multipla de 3: fale fizz
02 Se a posição for multipla de 5: fala buzz
03 Se a posição for multiplad e 3 e de 5: fale fizzbuzz
04 Para qualquer outra posição fale o próprio número
"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
# def multiple_of(base, num):
#     return num % base == 0 # a mesma expressão de cima

multiple_of_3 = partial(multiple_of, 3)
# def multiple_of_3(num): 
#     return num % 3 == 0 # a mesma expressão de cima
multiple_of_5 = partial(multiple_of, 5)
# def multiple_of_5(num):
#     return num % 5 == 0 # a mesma expressão de cima


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
    
    
"""
    1. Função multiple_of
Primeiro, você criou uma função multiple_of usando um lambda. Ela verifica se um número é múltiplo de outro. A função é simples:


multiple_of = lambda base, num: num % base == 0
Aqui, base é o número pelo qual você quer dividir, e num é o número que está sendo testado. O partial foi usado para simplificar a verificação de múltiplos de 3 e 5:

multiple_of_3 verifica se o número é múltiplo de 3.
multiple_of_5 verifica se o número é múltiplo de 5.
2. Função robot
A função robot recebe um número (pos) e retorna:
'fizzbuzz' se o número for múltiplo de 3 e de 5.
'buzz' se for múltiplo de 5.
'fizz' se for múltiplo de 3.
O próprio número como string se não for múltiplo de 3 nem de 5.
3.Os asserts são usados para testar se a função robot está retornando o resultado esperado. Se o resultado não for o esperado, o Python gera um erro (AssertionError).

Testando números comuns:
assert robot(1) == '1'
assert robot(2) == '2'
assert robot(4) == '4'
Aqui, o teste está verificando que, se o número não é múltiplo de 3 nem de 5, o retorno será o próprio número como string. Para as posições 1, 2 e 4, o retorno deve ser '1', '2' e '4'.

Testando múltiplos de 3 (fizz):
assert robot(3) == 'fizz'
assert robot(6) == 'fizz'
assert robot(9) == 'fizz'
Esses asserts verificam se a função retorna 'fizz' corretamente para múltiplos de 3 (3, 6 e 9).

Testando múltiplos de 5 (buzz):
assert robot(5) == 'buzz'
assert robot(10) == 'buzz'
assert robot(20) == 'buzz'
Aqui, os testes verificam se a função retorna 'buzz' corretamente para múltiplos de 5 (5, 10 e 20).

Testando múltiplos de 3 e 5 (fizzbuzz):
assert robot(15) == 'fizzbuzz'
assert robot(30) == 'fizzbuzz'
assert robot(45) == 'fizzbuzz'
Por fim, esses asserts verificam se a função retorna 'fizzbuzz' corretamente para números múltiplos de 3 e de 5 ao mesmo tempo (15, 30 e 45).

Resumo do processo:
Você começou com casos simples, testando números que não são múltiplos de 3 nem de 5.
Depois, testou os múltiplos de 3 e de 5 separadamente.
Por último, validou os casos especiais em que o número é múltiplo de 3 e de 5, esperando 'fizzbuzz'.
"""