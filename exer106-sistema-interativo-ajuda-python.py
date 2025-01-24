# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('  SISTEMA DE AJUDA PyHELP')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


c = ('\033[m',   # 0 sem cores
     '\033[0;30;41m', # 1 cor vermelha
     '\033[0;30;45m', # 5 cor roxo
     '\033[7;30m' #6 cos branco
)


def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0])
    
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',5)
    help(com)



comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',1)
    comando = str(input('Função ou blibioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÈ LOGO',1 )
        
        