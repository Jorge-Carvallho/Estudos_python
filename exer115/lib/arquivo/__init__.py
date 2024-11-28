# from sistema import *

def arquivoExiste(nome):
    # print(f'Verificando o arquivo: def----> {nome}')
    try:
        a = open(nome, 'rt') 
        a.close()
    except Exception as e:
        return False
    else:
        # print('Encontrado')
        return True
       

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # -------Teste do arquivo com rt = Texto, e rb = Binário-----------------
# ---------->Texto: Use 'rt' se o arquivo contiver apenas texto e você quiser trabalhar com strings.
# ---------->Binário: Use 'rb' se o arquivo contiver dados binários e você não deseja que o Python tente interpretá-los como texto.

    
# from sistema import *
    
# def arquivoExiste(nome):
#     print(f'Verificando o arquivo {nome}')
#     return nome
    

# print(f'Caminho absoluto do arquivo: {arq}')#mostra o caminho encontrado
# try:
#     a = open(nome, 'rt')
#     a.close()
#     print('Arquivo encontrado com rt')

# except FileNotFoundError as e:
#     print(f'Error com rt --> {e}')
#     return False
    
# try:    
#     a = open(nome, 'rb')
#     a.close()
#     print('Arquivo encontrado com rb')

# except FileNotFoundError as e:
#         print(f'ERRor com rb --> {e}')
#         return False

# except Exception as e:
#         print(f'Outro erro com rb {e}')

#     return True
        
        
        # -------------------------
        
        
