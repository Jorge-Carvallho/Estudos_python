#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opçoẽs:cadastrar uma nova pessoa, e listar todas as pessoas cadastradas.


import sys
sys.path.append('/home/jorge/Documentos/wttd_aulas') 
# Adiciona o diretório '/home/jorge/Documentos/wttd_aulas' ao caminho de busca de pacotes do Python
# (sys.path), permitindo que o Python encontre o pacote 'exer115'
# mesmo que o script esteja sendo executado de outro diretório.
import os
from exer115.lib.interface import *
from exer115.lib.arquivo import arquivoExiste
from time import sleep
# arq = os.path.abspath('exer115/cursoemvideo.txt')
# print(f'Caminho absoluto do arquivo:{arq}')

arq_absoluto = os.path.abspath('exer115/cursoemvideo.txt')
print(f'Caminho absoluto do arquivo: {arq_absoluto}')
print(f'Arquivo existe? {arquivoExiste(arq_absoluto)}')
print('aqui')




print(arquivoExiste('cursoemvideo.txt'))

# # arq = 'cursoemvideo.txt'
if arquivoExiste(arq_absoluto):
    print('Arquivo encontrado com sucesso!!')
else:
    print('Arquivo não encontrado')
    print('Caiu no bloco do else -->')


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
