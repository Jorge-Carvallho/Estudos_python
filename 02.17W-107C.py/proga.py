"""
A grande sacada do Módulo
"""

# print('Begin', __name__)

# print('Define fa')
# def fa():
#     print('dentro de fa')
    
# if __name__ == '__main__': # verifica se o entrepoint(chamado como programa principal)
#     print('CHama fa')
#     fa()
    

# print('End', __name__)
# # dessa forma ele execulta simutaneamente como programa principal e biblioteca:
# # Essa estrutura garante que a função main() seja chamada quando o script for executado diretamente, mas não quando o script é importado como um módulo em outro script.

# # teste que verifica se é um módulo atual é entrepoin ou blibioteca 
# print(70*'-')


def fa():
    print(' Aqui dentro sera executado pela importação !')

    print('Aqui é a execução no momento da importação!')



if __name__ == '__main__':
    print('Executando como programa principal')
    print(fa())
    
    
