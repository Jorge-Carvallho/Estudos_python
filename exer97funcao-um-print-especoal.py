# Exercício 97
# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ex: escreva('Olá, mundo!')
# saida: ~~~~~~~~~~~~
#         Olá mundo!
#        ~~~~~~~~~~~~

def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))
    


escreva('Curso em video')
escreva('Python é uma linguagem de programação legal')

# ---------------------------------------ou----------------------------------------

def escreva(msg):
    tam = len(msg)+ 4
    print('-'* tam)
    print(f'  {msg}')
    print('-'* tam)
    
    
escreva('Vamos para mas um dia de estudos')