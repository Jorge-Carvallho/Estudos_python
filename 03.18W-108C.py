#Como ler código identado

def main(): # : é delimitador de blocos, sempre esperado um novo bloco de código posterior ao :
    print('Iniciado um novo bloco de código')# os 2 pontos(:) acima indica iniciando um novo bloco de código

    def new_main(): # aqui surje uma nova ordem de prioridade a frente da antiga hierarquida dentro deste bloco
        print('Aqui posterior os : acima é uma nova hieraquia')# aqui surje mas um bloco de código com mas hierarquia do que o de cima
        
    for i in range(1,5): # a mudança de indentação acontece sempre que você tem uma nova hierarquia no código
        print(i)
        print('Aqui',)


main()
"""
Python tem o conceito de linhas fisicas e linhas logicas.
--- uma linha fisica é toda ela que termina com \n

"""
# def main(x):
#     print(F'A identação de {x}mostra a linha fisica \n'  
#           'a linha logica')
#     return x
# main(' x <--exemplo que aqui é (x) passado por função main como value--> ')

# abaixo temos 1 linha fisica que é aparti de (A identação, até a palavra  fisica) e a segunda linha (a linha, até lógica).
# a linha logica é toda expressao do print que é considerada uma unica linha

def main(x):
    print(f'A identação de {x}mostra a linha fisica '  
          'a linha logica')
    return x 
main(' x <--exemplo que aqui é (x) passado por função main como value--> ')