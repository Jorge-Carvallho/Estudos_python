#Exercício
# Crie um módulo chamado moeda.py que tenha funções incorporadas aumentar(),diminuir(),
# dobro(), e metade().
# Faça também um programa principal que importe esse módulo e use algumas dessas funções

    # --------> usando import decimal < -------------#
# import decimal
# def metade(n):
#     n /= 2 
#     return f'{n:g}'


# def dobro(n):
#     n *= 2
#     return f'{n:g}'


# def aumentar(n):
#     n *= 1.40
#     return f'{n:g}'
    

# def reduzir(n):
#     n *= 0.80
#     return f'{n:g}'

     # ------------> sem o uso do decimal <-------------------#

def aumentar(preço = 0,taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato == False else converte_moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else converte_moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if not formato else converte_moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return res if not formato else converte_moeda(res)


def converte_moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


# A função converte_moeda() faz tarsforma o número float que vem com padrão o ponto tasformando em virgula como mostra no metodo acima replace
# que ---> .replace('.',',')
# Então foi criado um 3 argumento formato=False que caso o formate seja True chama a expreção 
# --> res de resposta if not formato else chama a função converte_moeda(já como res de resposta de returno)

