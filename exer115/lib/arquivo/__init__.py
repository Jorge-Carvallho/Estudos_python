# def arquivoExiste(nome):
#     print(f'Verificando o arquivo: {nome}')
#     try:
#         a = open(nome, 'rt')
#         a.close()
#     except FileNotFoundError:
#         return False
#     else:
#         return True
    
    
    
def arquivoExiste(nome):
    print(f'Verificando o arquivo {nome}')

    try:
        a = open(nome, 'rt')
        a.close()
        print('Arquivo encontrado com rt')

    except FileNotFoundError as e:
        print(f'Error com rt --> {e}')
        return False
    
    try:
        a = open(nome, 'rb')
        a.close()
        print('Arquivo encontrado com rb')

    except FileNotFoundError as e:
        print(f'ERRor com rb --> {e}')
        return False

    except Exception as e:
        print(f'Outro erro com rb {e}')

    return True
        
    
