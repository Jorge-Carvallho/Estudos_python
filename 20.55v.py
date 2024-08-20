# #classes, atributos e métodos no python

# class Car: pass # depois do delimitador de código --> : coloquei pass ele não faz nada ainda, ele é como se fosse aguardando

# print(Car)# a palavra Car é uma váriavel que referência o objeto da class car, ou seja um molde.  (ou tipo em memória)
# print(Car())# cria e imprime um objeto da class Carmostrando a identidade da instancia  ou, --> aqui é um objeto com a saída de uma identidade instancianda da class Car do módulo main
# print(type(Car()))# mostra o tipo do objeto criado oou, o que é Car ou, --> tipo do objeto da classe que é do tipo Car


class Car:
    print('Loanding a class...')
    name = 'Ferrari'
    print('Done defining a ' + name + '!'* 5)# concatena a frase com a variavel e cria 5 sinais de exclamação
    for char in name:
        print(char.upper())# para cada letra(char) do nome coloca maiúscula e imprime ai final cada letra
        
    print('---------')# quebro o lop com um espaço
    if int(len(name) % 2) == 0:# pega o indice a palavra name, transforma em inteiro e se o resto do modolo dele for 0 imprime ao final portas 2 se for 1, imprime portas  3 
        portas = 2
    else:
        portas = 3 
    print(portas)
    
# tenho 2 variaveis locais no corpo desse código, que são : name = ferrari e portas = 3 
# As variaveis locais definidas dentro no corpo da classe chama-se fora de metodos pra ficar claro atibutos de classe
5m/55