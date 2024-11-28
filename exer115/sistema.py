#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opçoẽs:cadastrar uma nova pessoa, e listar todas as pessoas cadastradas.


import sys
sys.path.append('/home/jorge/Documentos/wttd_aulas') 
# -----> Adiciona o diretório '/home/jorge/Documentos/wttd_aulas' ao caminho de busca de pacotes do Python
# -----> (sys.path), permitindo que o Python encontre o pacote 'exer115'
# mesmo que o script esteja sendo executado de outro diretório.
import os
from exer115.lib.interface import *
from exer115.lib.arquivo import arquivoExiste, criarArquivo
from time import sleep
# import os  #retorna o caminho do arquivo
# print(f'Diretório atual: {os.getcwd()}')


nome_do_arquivo = 'exer115/cursoemvideo.txt'
arq = os.path.abspath(nome_do_arquivo)#busca o caminho e guarda na variavel.
# arq = os.path.basename(nome_do_arquivo)
#print(f'Caminho absoluto do arquivo:---> {arq}')#mostra o caminho encontrado
# print(f'Arquivo existe? ---> {arquivoExiste(arq)}')#apenas um teste pra retorno do arquivo, retorna True or False
# print(arq)
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!!')
else:
    print('Arquivo não encontrado')
    # print('Caiu no bloco do else -->')
    criarArquivo(os.path.basename(arq))
    


cabeçalho('SISTEMA ARQUIVO v1.0')

while True:
    resposta = menu(['Ver pessoas cadastadas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida! \033[m')
    sleep(0.9)



# Não esqueça mas-------------------> 

# ........O path é um módulo dentro do pacote (OS) em Python. Ele contém várias funções relacionadas a caminhos de arquivos e diretórios.
# Exemplo de funções: verificar se um arquivo existe, encontrar caminhos absolutos, etc.

 #---------------------------------->
#  abspath é uma função no módulo os.path que retorna o caminho absoluto de um arquivo ou diretório ex: import os / print(os.path.abspath('meu_arquivo.txt')).
#/home/usuario/meu_projeto/meu_arquivo.txt

# ---------------------------------->
# os.path.exists retorna:
# True (verdadeiro): Se o arquivo ou diretório existe no caminho fornecido.
# False (falso): Se o arquivo ou diretório não existe.
