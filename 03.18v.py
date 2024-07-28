# indentação

def main(): # : é delimitador de blocos, sempre esperado um novo bloco de código posterior ao :
    print('Iniciado um novo bloco de código')

    def new_main(): # aqui surje uma nova ordem de prioridade a frente da antiga hierarquida dentro deste bloco
        print('Aqui podsterior os : acima é uma nova hieraquia')
        
    for i in range(1,5):
        print(i)
        print('Aqui',)


main()
