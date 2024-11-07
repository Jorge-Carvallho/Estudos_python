# def calc(a,b):
#     return a + b

# calc(2,3)





# # eu espero 4 quando execultar calc(2,2)
# # assert 4 == calc(2,2)

# # try:
# assert calc(2,2) == 4
# # except AssertionError:
# #     print('errou')

print('-------------Teste prático, desenvolvimento guiado pelo teste----------------')

'''
Exercício fizzbuzz
Regra do jogo:

Quando a posição é multipla de 3, fale fizz;
Quando a posição é multipla de 5, fale buzz;
Quando a posição for multipla de 3 e de 5, fale fizzbuzz;
Para todas as outras posições, fale o próprio número.
obs:--------- ''''-------------'''''----------------------''''''''
Quebra no Código e na Lógica: Quando um código falha em um teste, ele gera uma "quebra" (ou erro) que interrompe a execução, indicando que algo não corresponde ao esperado.

Falha no Teste: A falha significa que o valor retornado pela função não atendeu à expectativa que foi definida para aquele teste.

Importância do AssertionError: Esse erro indica que o código não está funcionando conforme esperado. Ele ajuda a identificar onde a lógica ou os argumentos estão incorretos, permitindo que você faça ajustes antes de usar o código em um contexto maior

'''



def robot(pos):
    return  '1'

if __name__ == '__main__':
    assert robot(1) == '1'
    
    
    
