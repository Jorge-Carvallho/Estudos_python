#Exercício
#Crie um código em python quew teste se o site (pudim) está acessivel pelo computador usado.


# import urllib.request
# import ssl

# try:
#     # Cria um contexto SSL que ignora os certificados
#     context = ssl._create_unverified_context()
#     site = urllib.request.urlopen('https://www.pudim.com.br/', context=context)
# except urllib.error.URLError as e:
#     print(f'Erro: {e.reason}')  # Mostra detalhes do erro
# else:
#     print('Sistema ok','\nConseguir acessar o site pudim con sucesso!')
# # finally:
# #     print('rodando')

# --------------------------------------------------------------------------------
import requests # -----> é uma biblioteca usada para fazer requisições HTTP em PYTHON, ela simplifica o processo de enviar basicamente masi não apenas
 
try: # tentar execultar
    response = requests.get('https://www.pudim.com.br/', verify=False) # Requisição GET, que solicita informações de uma URL. 
    #No caso, estamos pedindo informações do endereço
    print('Sistema ok')
    print(response)
    
except requests.exceptions.RequestException as e:
    print(f'Error, {e}')
        # requests: É a biblioteca que estamos usando para fazer requisições HTTP (como no caso do requests.get(...)).
        # exceptions: Dentro da biblioteca requests, todos os erros gerados por ela estão na parte chamada exceptions.
        # RequestException: É a classe de erro principal para todos os tipos de erro que podem ocorrer ao fazer uma requisição com o requests.
        # Ou seja, ele captura qualquer tipo de erro que possa ocorrer durante a requisição 
        # (como problemas de rede, URL inválida, tempo de espera excedido, etc.).
else:
    print('Conseguir acessar o site pudim com sucesso!')
# obs:Exception é a classe base de todas as exceções no Python, então captura todos os erros.
#     Exception captura qualquer erro em qualquer parte do código.
#     requests.exceptions.RequestException captura somente erros específicos da biblioteca requests, como erros de conexão, timeout, ou erro de URL.