# # #classes, atributos e métodos no python

# # class Car: pass # depois do delimitador de código --> : coloquei pass ele não faz nada ainda, ele é como se fosse aguardando

# # print(Car)# a palavra Car é uma váriavel que referência o objeto da class car, ou seja um molde.  (ou tipo em memória)
# # print(Car())# cria e imprime um objeto da class Carmostrando a identidade da instancia  ou, --> aqui é um objeto com a saída de uma identidade instancianda da class Car do módulo main
# # print(type(Car()))# mostra o tipo do objeto criado oou, o que é Car ou, --> tipo do objeto da classe que é do tipo Car


# class Car:
#     print('Loanding a class...')
#     name = 'Ferrari'
#     print('Done defining a ' + name + '!'* 5)# concatena a frase com a variavel e cria 5 sinais de exclamação
#     for char in name:
#         print(char.upper())# para cada letra(char) do nome coloca maiúscula e imprime ai final cada letra
        
#     print('---------')# quebro o lop com um espaço
#     if int(len(name) % 2) == 0:# pega o indice a palavra name, transforma em inteiro e se o resto do modolo dele for 0 imprime ao final portas 2 se for 1, imprime portas  3 
#         portas = 2
#     else:
#         portas = 3 
#     print(portas)
#     print('--------------------------------------------------------------')
    
# # tenho 2 variaveis locais no corpo desse código, que são : name = ferrari e portas = 3 ou 2
# # As variaveis locais definidas dentro no corpo da classe chama-se fora de métodos pra ficar claro atibutos de classe

# c = Car()
# print(c.name, c.portas)# aqui o --> c <-- que é uma instancia de Car busca os atibutos não achando, ele busca o valores da  instancia passada que  no caso são os de Car
# # agora quando eu atribuo novos atribudos a --> c <-- que é uma instancia de Car ele passar a ser os atribudios passados 
# # quando eu atribuo valor aos atributos de uma instancia eu estou criando um atributo de instancia novo, e os atributos de uma instancia não sobrescrevem os atributos da classe
# c.name = 'BMW'
# c.portas = '2'
# print(c.name, c.portas)
# # criando agora uma isntancia de Car novamnete o --> d <-- busca atributos proprios e como não tem faz um fallback, ou seja, busca valores da intancia originaria que é Car
# d = Car()
# print(d.name, d.portas)


print('-----------------------------------------------------***------------------------------------')


class Car:
    name = 'Ferrari' # name aqui é o atibuto de class
    def __init__(self, model): # model aqui so existe na instancia, nao existe na classself dentro de uma função o que é
        
        self.model = model

c, d = Car('f50'), Car('f40')# c e d são instancia da classe Car que tem mseus proprios atributos e métodos e podem ser acessados e modificadops individualmente
print(c.name, d.name)
print(c.model, d.model)

print(hasattr(Car,'model'))# hasattr vericia se determinada clase ou método pertence a classe ou ao objeto em questão
Car.model = 'TopGear'
print(Car.model, c.model, d.model)