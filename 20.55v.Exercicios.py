# #Exercício 1: Classe Livro de Receita
# Crie uma classe chamada LivroReceitas com os seguintes atributos:
# nome
# receitas (uma lista de receitas)
# Inclua um método adicionar_receita que adiciona uma receita à lista e um método listar_receitas que imprime todas as receitas.
class LivroReceitas:
    def __init__(self, nome):
        self.nome = nome
        self.receitas = []

    def adicionar_receitas(self, receita):
        self.receitas.append(receita)
    
    def listar_receitas(self):
        if not self.receitas:
            print('Nenhumareceita cadastrada.')
        else:
            print(f'Receitas do livro: "{self.nome}"')
            for receita in self.receitas:
                print(f'{receita}')


livro = LivroReceitas('Culinaria Brasileira')
livro.adicionar_receitas('Bolo de chocolate')
livro.adicionar_receitas('Feijoada')
livro.listar_receitas()
print('-----------------------------------------------2-----------------------------------------------------')




# Exercício 2: Classe ContaCorrente com Limite
# Crie uma classe chamada ContaCorrente com os seguintes atributos:

# titular
# saldo
# limite
# Inclua métodos depositar, sacar, e exibir_saldo. O método sacar deve considerar o limite disponível para permitir saques além do saldo, se aplicável.

class ContaCorrente:
    def __init__(self,titular,saldo,limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de {valor} realizado. Saldo atual: {self.saldo}')
        
    def sacar(self, valor):
        if valor <= self.saldo + self.limite  :
            self.saldo -= valor
            print(f'Saque de {valor} realizado. Saldo atual: {self.saldo }')
        else:
            print(f'Saldo insuficiente considerando limite de crédito')
        
        
    def exibir_saldo(self):
        print(f'Titular: {self.titular}')
        print(f'Saldo atual: {self.saldo}')
        print(f'limite disponível: {self.limite}')
        
        
pessoa1 = ContaCorrente('Jorge', 1000, 500)
pessoa1.depositar(200)
pessoa1.sacar(1100)
pessoa1.sacar(600)
pessoa1.exibir_saldo()

print('--------------------------------------------------------------3-------------------------------------------------------------')

# Exercício 3: Classe Produto
# Crie uma classe chamada Produto com os seguintes atributos:

# nome
# preco
# quantidade
# Inclua um método atualizar_quantidade que modifica a quantidade do produto e um método descricao que imprime "Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}".
class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        
    def descricao(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}')
        
produto1 = Produto('jorge', 300, 100)
produto1.atualizar_quantidade(120)
produto1.descricao()

produto2 = Produto('Luis', 20, 100)
produto2.atualizar_quantidade(21)
produto2.descricao()

print('--------------------------------------------4------------------------------------------------------')

# Exercício 4: Classe Pessoa com Endereço
# Crie uma classe chamada Pessoa com os seguintes atributos:

# nome
# idade
# endereco
# Inclua um método alterar_endereco que atualiza o endereço da pessoa e um método informacoes que imprime "Nome: {nome}, Idade: {idade}, Endereço: {endereco}".
class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        
    def atualizar_idade(self, idade_atualizada):
        self.idade = idade_atualizada
        
        
    def alterar_endereço(self, novo_endereco):
        self.endereco = novo_endereco

    def informaçoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}')
        
        
pessoa1 = Pessoa('Jorginho', 34, 'Rua cristovão ferreira 73')
pessoa1.atualizar_idade(35)
pessoa1.alterar_endereço('rua do norte')
pessoa1.informaçoes()

pessoa2 = Pessoa('Lais', 33, 'Rua cristovão ferreira 73')
pessoa2.atualizar_idade(34)
pessoa2.alterar_endereço('rua do norte')
pessoa2.informaçoes()
print('----------------------------------------------------5---------------------------------')


# Exercício 5: Classe Circulo
# Crie uma classe chamada Circulo com o seguinte atributo:

# raio
# Inclua métodos area e circunferencia que retornam a área e a circunferência do círculo, respectivamente.
import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def circunferencia(self):
        return 2 * math.pi * self.raio
    def area(self):
        return math.pi * (self.raio ** 2 )
        
        
    def imprimir(self):
        print(f'Raio do circulo: {self.raio}')
        print(f'Circunferencia do circulo : {self.circunferencia()}')
        print(f'A area do circulo : {self.area()}')

circulo1 = Circulo(5)
circulo1.imprimir()
print('-------------------------------------------6-----------------------------------------')

# Exercício 6: Classe Estudante
# Crie uma classe chamada Estudante com os seguintes atributos:

# nome
# matricula
# curso
# Inclua um método alterar_curso que modifica o curso do estudante e um método informacoes que imprime "Nome: {nome}, Matrícula: {matricula}, Curso: {curso}".
class Estudante:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def alterar_curso(self,curso_novo):
        self.curso = curso_novo

    def informaçoes(self):
        print(f'Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso} ')


aluno1 = Estudante('Jorge', 8743,'Analise de Sistema')
aluno1.alterar_curso('Direito')
aluno1.informaçoes()

aluno2 = Estudante('Lais',8733,'Psicologia')
# aluno2.alterar_curso('Desing')
aluno2.informaçoes()
print('--------------------------------------------7--------------------------------------------')

# Exercício 7: Classe Jogo
# Crie uma classe chamada Jogo com os seguintes atributos:

# titulo
# genero
# ano_lancamento
# Inclua um método descricao que imprime "Título: {titulo}, Gênero: {genero}, Ano de Lançamento: {ano_lancamento}" e um método atraso que indica se o jogo é mais antigo que 5 anos.
import datetime
class Jogo:
    def __init__(self, titulo,genero, ano_de_lancamento):
         
        self.titulo = titulo
        self.genero = genero
        self.ano_de_lancamento = ano_de_lancamento
        
        
    def descrição(self):
        print(f'Título: {self.titulo}, Gênero: {self.genero}, Ano de Lançamento: {self.ano_de_lancamento}')

    def atraso(self):
        ano_atual = datetime.datetime.now().year
        if ano_atual - self.ano_de_lancamento > 5:
            print('Jogo antigo')
        else:
            print('Jogo atual')
        
        
jogo1 = Jogo('BahiaxVitoria',' futbol', 2015)
jogo1.descrição()
jogo1.atraso()





# Exercício 8: Classe Telefone
# Crie uma classe chamada Telefone com os seguintes atributos:

# modelo
# numero
# fabricante
# Inclua um método alterar_numero que atualiza o número de telefone e um método informacoes que imprime "Modelo: {modelo}, Número: {numero}, Fabricante: {fabricante}".

# Exercício 9: Classe Tarefa
# Crie uma classe chamada Tarefa com os seguintes atributos:

# descricao
# concluida (booleano)
# Inclua métodos marcar_concluida para definir a tarefa como concluída e status que imprime "Descrição: {descricao}, Concluída: {concluida}".

# Exercício 10: Classe Agenda
# Crie uma classe chamada Agenda com o seguinte atributo:

# contatos (uma lista de tuplas com nome e telefone)
# Inclua métodos adicionar_contato para adicionar um novo contato e listar_contatos para imprimir todos os contatos da agenda.

# Esses exercícios foram criados para cobrir uma variedade de situações e funcionalidades diferentes, ajudando você a praticar e entender melhor como trabalhar com classes em Python. Boa sorte e divirta-se praticando!