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


# print('-----------------------------------------------------***------------------------------------')


# class Car:
#     name = 'Ferrari' # name aqui é o atibuto de class
#     def __init__(self, model): # model aqui so existe na instancia, nao existe na classself dentro de uma função o que é
        
#         self.model = model

# c, d = Car('f50'), Car('f40')# c e d são instancia da classe Car que tem mseus proprios atributos e métodos e podem ser acessados e modificadops individualmente
# print(c.name, d.name)
# print(c.model, d.model)

# print(hasattr(Car,'model'))# hasattr vericia se determinada clase ou método pertence a classe ou ao objeto em questão
# Car.model = 'TopGear'
# print(Car.model, c.model, d.model)



# class Vendedor():
#     def __init__(self, nome):
#         self.nome = nome 
#         self.vendas = 0

#     def vendeu(self, vendas):
#         self.vendas = vendas

#     def bateu_meta(self, meta):
#         if self.vendas > meta:
#             print(self.nome,' Bateu a meta')
#         else:
#             print(self.nome, ' Não bateu meta')


# vendedor1 = Vendedor('Jorge')
# vendedor1.vendeu(1000)
# vendedor1.bateu_meta(100)
# print()

print('----------------------------------------exercicios-------------------------------------------')

# Exercício 1: Criando sua primeira classe
# Tarefa: Crie uma classe chamada Animal. Esta classe deve ter um atributo de classe especie e um método chamado emitir_som que simplesmente imprime "Som do animal".
# Crie uma instância da classe Animal.
# Acesse o atributo especie e o método emitir_som.

# class Animal:
#    especie = 'desconhecida'
#    def emitir_som(self):
#        print('Som do animal')
       
       
       
# animal1 = Animal()
# print(animal1. especie)
# animal1.emitir_som()

print('------------------------------------------2-------------------------------------------------')

# Exercício 2: Atributos de instância
# Tarefa: Modifique a classe Animal para que tenha um atributo de instância nome que seja definido pelo método __init__. Adicione também um método descrever que imprime o nome do animal.

# Crie duas instâncias da classe Animal com nomes diferentes.
# Use o método descrever para imprimir os nomes dos animais.

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def descrever(self, som):
        print(f'O nome do animal é {self.nome} e faz o som de {som}')
       


# animal1 = Animal('Leão')
# animal2 = Animal('Tigre')

# animal1.descrever('rallll')
# animal2.descrever('Meeealll')

print('--------------------------------------------------3------------------------------------')

# Exercício 3: Classe Carro com métodos
# Tarefa: Crie uma classe Carro que tenha os seguintes atributos de instância:

# marca
# modelo
# ano
# E os seguintes métodos:

# ligar que imprime "O carro está ligado."
# desligar que imprime "O carro está desligado."
# info que imprime "Marca: {marca}, Modelo: {modelo}, Ano: {ano}"
# Crie uma instância de Carro e use os métodos para ligar, desligar e obter as informações do carro.


class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def ligar(self):
        print('O veiculo esta ligando')

    def desligar(self):
        print('O veiculo esta desligando')

    def info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

carro1 = Carro('Argo', 'Fiat', 2020)
carro1.ligar()
carro1.desligar()
carro1.info()


print('------------------------------------------------4------------------------------------')


# Exercício 4: Métodos para alterar atributos
# Tarefa: Na classe Vendedor que você criou, adicione um método chamado alterar_vendas que permita alterar o número de vendas para um novo valor. Teste o método para verificar se ele altera corretamente o valor de vendas.

# Crie uma instância da classe Vendedor.
# Altere o valor de vendas usando o novo método e verifique se foi alterado corretamente.


class Vendedor:
    def __init__(self,nome):
        self.nome = nome
        self.vendas = 0
    def vendeu(self, vendas):
        self.vendas = vendas

    def alterar_vendas(self, novas_vendas):
      self.vendas = novas_vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f'{self.nome}, bateu meta')

        else:
            print(f'{self.nome}, não bateu meta')

    
vendedor1 = Vendedor('Jorge')
vendedor1.vendeu(1000)
vendedor1.alterar_vendas(2000)
print(vendedor1.vendas)

print('----------------------------------5--------------------------------------------')

# Exercício 5: Classe com método condicional
# Tarefa: Crie uma classe ContaBancaria que tenha os seguintes atributos de instância:

# saldo
# titular
# Adicione os seguintes métodos:

# depositar que aumenta o saldo da conta.
# sacar que diminui o saldo da conta se o valor do saque for menor ou igual ao saldo disponível.
# exibir_saldo que imprime o saldo atual da conta.
# Crie uma instância de ContaBancaria e realize algumas operações de depósito e saque.
# Exiba o saldo após cada operação.

class ContaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
        print(f'Depositado: {valor}. Saldo atual: {self.saldo}')
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Sacado: {valor}, Saldo atual: {self.saldo}')
        else:
            print('Saldo insuficiente')
        
        
    def exibir_saldo(self):
        print(f'Saldo atual : {self.saldo}')

conta1 = ContaBancaria('João')
conta1.depositar(500)
conta1.sacar(200)
conta1.exibir_saldo()




print('--------------------------------------6----------------------------------------------')

# Exercício 6: Classe Livro
# Tarefa: Crie uma classe chamada Livro que tenha os seguintes atributos:

# titulo
# autor
# numero_paginas
# E os seguintes métodos:

# descricao que imprime a descrição do livro no formato: "Titulo: {titulo}, Autor: {autor}, Páginas: {numero_paginas}".
class Livro:
    def __init__(self,titulo, autor,numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
    
    def descricao(self):
        print(f'Titulo: {self.titulo}, Autor: {self.autor}, Páginas: {self.numero_de_paginas}')




livro1 = Livro('Python para iniciantes ','João', 320 )
livro1.descricao




# Crie uma instância da classe Livro com os valores:
# titulo: "Python para Iniciantes"
# autor: "João Silva"
# numero_paginas: 350
# Use o método descricao para imprimir a descrição do livro.
# python
# Copiar código
# # Seu código aqui
# Exercício 2: Classe Pessoa
# Tarefa: Crie uma classe chamada Pessoa com os seguintes atributos:

# nome
# idade
# cidade
# E os seguintes métodos:

# cumprimentar que imprime "Olá, meu nome é {nome} e tenho {idade} anos!".
# mudar_cidade que atualiza o atributo cidade e imprime "Agora moro em {cidade}".
# Passos:

# Crie uma instância da classe Pessoa com os valores:
# nome: "Maria"
# idade: 28
# cidade: "São Paulo"
# Use o método cumprimentar.
# Mude a cidade da Pessoa para "Rio de Janeiro" e use o método mudar_cidade para exibir a nova cidade.
# python
# Copiar código
# # Seu código aqui
# Exercício 3: Classe ContaCorrente
# Tarefa: Crie uma classe chamada ContaCorrente com os seguintes atributos:

# titular
# saldo
# E os seguintes métodos:

# depositar que aumenta o saldo da conta e imprime "Depósito de {valor} realizado. Saldo atual: {saldo}".
# sacar que diminui o saldo da conta se houver saldo suficiente e imprime "Saque de {valor} realizado. Saldo atual: {saldo}". Se não houver saldo suficiente, imprime "Saldo insuficiente!".
# exibir_saldo que imprime o saldo atual.
# Passos:

# Crie uma instância de ContaCorrente com os valores:
# titular: "Carlos"
# saldo: 1000
# Deposite 500 na conta.
# Saque 300 e depois tente sacar 1500 (deve mostrar "Saldo insuficiente!").
# Exiba o saldo final da conta.
# python
# Copiar código
# # Seu código aqui
# Exercício 4: Classe Cachorro
# Tarefa: Crie uma classe chamada Cachorro com os seguintes atributos:

# nome
# raca
# idade
# E os seguintes métodos:

# latir que imprime "Au au!".
# descrição que imprime "Meu nome é {nome}, sou da raça {raca} e tenho {idade} anos.".
# Passos:

# Crie uma instância da classe Cachorro com os valores:
# nome: "Rex"
# raca: "Labrador"
# idade: 3
# Use o método latir e o método descrição para descrever o cachorro.
# python
# Copiar código
# # Seu código aqui
# Exercício 5: Classe Aluno
# Tarefa: Crie uma classe chamada Aluno com os seguintes atributos:

# nome
# matricula
# notas (uma lista de notas)
# E os seguintes métodos:

# adicionar_nota que adiciona uma nota à lista de notas.
# media que calcula e retorna a média das notas.
# situacao que imprime "Aprovado" se a média for maior ou igual a 7 e "Reprovado" caso contrário.
# Passos:

# Crie uma instância de Aluno com os valores:
# nome: "Ana"
# matricula: 12345
# Adicione três notas: 8.0, 6.5, 7.5.
# Calcule e exiba a média das notas.
# Verifique a situação do aluno (Aprovado ou Reprovado).