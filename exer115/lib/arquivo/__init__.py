# from sistema import *
from exer115.lib.interface import *
import os

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
        print(f'Arquivo {os.path.basename(nome)} criado com sucesso!')
      
      
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
        
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as e:
        print(f'Houve um erro cadastrando um usuário --> {e}')
            
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as e:
            print(f'Houve um erro na hora de escrever os dados --> {e}')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close    
    
    
    

    
    
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
        
        
