def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
    
def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def reduzir(preco=0, taxa=0):
    res = preco - (preco * 13 / 100)
    return res

def aumentar(preco=0, taxa=0):
    res = preco + (preco * 10 / 100)
    return res
    
  
    