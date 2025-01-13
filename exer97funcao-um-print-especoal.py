# def escreva(txt):
#     print('-'*len(txt))
#     print(txt)
#     print('-'*len(txt))
    


# escreva('Curso em video')
# escreva('Python é um aliguagem de programação legal')

# ---------------------------------------ou----------------------------------------

def escreva(msg):
    tam = len(msg)+ 4
    print('-'* tam)
    print(f'  {msg}')
    print('-'* tam)
    
    
escreva('Vamos para mas um dia de estudos')