
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError) as e:
            print(f'\033[31mError, Digite um número válido: \033[m ')
            # print(f'\033[31mError, Digite um número válido: --> {e.__class__}\033[m] ')
            continue
        except KeyboardInterrupt as e :
            print(f'\n\033[31mUsuário preferio não digitar nenhum valor: \033[m ')
            # print(f'\n\033[31mUsuário preferio não digitar nenhum valor --> {e.__class__}\033[m] ')
            return 0
        else:
            return n
        
        
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc








         #------------------------ teste----------------------------------- #

# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError) as e:
#             print('ERROR, Digite um número válido')
#             continue
#         except KeyboardInterrupt as e:
#             print('Usuário preferio não digitar nenhum valor')
#             return 0 
#         else:
#             return n 
        
        
# def linha():
#     return '-'* 42


# def cabeçalho(txt):
#     print(linha())
#     print(txt.center(42))
#     print(linha())


# def menu(lista):
#     cabeçalho('Menu principal')
#     c = 1
#     for item in lista:
#         print(f'{c} {item}')
#         c +=1
#     print(linha())
#     opc = leiaInt('Sua opção: ')
#     return opc


# cabeçalho('SISTEMA DE')

# while True:
#     resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pesoas', 'Sair do sistema'])
#     if resposta == 1:
#         cabeçalho('opcão 1')
#     elif resposta == 2:
#         cabeçalho('opcao 2')
#     elif resposta == 3:
#         cabeçalho('Saindo do sistema, até logo')
#         break
#     else:
#         print('Digite uma opção válida')