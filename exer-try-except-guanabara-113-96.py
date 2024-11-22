# Exercício 
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaIntfloat() com a mesma funcionalidade


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError) as e:
            print(f'\033[31mError, Digite um número válido: --> {e.__class__}\033[m] ')
            continue
        except KeyboardInterrupt as e :
            print(f'\n\033[31mUsuário preferio não digitar nenhum valor --> {e.__class__}\033[m] ')
            return 0
        else:
            return n
        
def leiaFloat(msg):
    ...



# Programa Principal 
n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real')
print(f'O valor inteirio foi {n1}, e ovalor real foi { {n2}}')