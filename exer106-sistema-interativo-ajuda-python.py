# Exercício 106
# Faça um mini-sistema que utilize o interactive Help do Python.
# O usuário vai digitar o comando e o manual val aparecer.
# quando o usuário digitar a palavra 'FIM' o porgrama se encerrará


# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('  SISTEMA DE AJUDA PyHELP')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


c = ('\033[m',   # 0 sem cores
     '\033[0;30;41m', # 1 vermelha
     '\033[0;30;42m', # 2 verde
     '\033[0;30;43m', # 3 amarelo
     '\033[0;30;44m', # 4 azul
     '\033[0;30;45m', # 5 cor roxo
     '\033[7;30m'     # 6 branco
)


def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0],end='')
    
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[3],end='')
    help(com)
    print(c[3],end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',1)
    comando = str(input('Função ou blibioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÈ LOGO',1 )
        
        