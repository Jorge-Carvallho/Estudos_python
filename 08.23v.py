# Dicionários      declarado com {} dicionários não tem ordens
# para acessar a chave usa-se ['nome da cheve']

d = {'Nome': 'Henrique', 'Cidade': 'Salvador', 'Lat': 22.9, 'Long': 43.1}
print(d)
print(d['Nome']) #busca e imprime o valor da chave
d['Nome'] = 'Jorge Carvalho' #altera o contéudo da chave especificada
print(d)
print('asdf' in d)# verifica se existe uma chave em um dicionário ussar 'nome que pesquisa' in nome do dicionário retuna False ou True
print('jogando' in d.values())#verifica se existe o valor 'jogando' in d.values() (se existe o palavra jogando como valor no dicionário d) returna False ou True
print(d.get('asdf'))#verifica se existe a chave e returna None caso não existe ou returna o 2 parâmetro passado exemplo abaixo:
print(d.get('asdf','vamos criar'))# caso nao exista returna o valor passado no segundo parâmetro
print(len(d))#returna a quantidade de chaves
k = d.keys()
v = d.values()
i = d.items()
print(k)#returna apenas as chaves do dicionário
print(v)#retorna apenas os valores das chaves
print(i)#retorna os pares de chave e valor dentro de tuplas
# print(d['Nova-chave'] = 'valor-da-nova-chave')
print('---------------------------------')
d['Olá'] = 'Mundo'
print(d) # os dicionário irar adicionar ao k,v,i as alteracoes
#Dicionário é donamico, tudo ele é alterado, porém posso trasforma ele em uma tupla ou lista exemplo abaixo:
k = tuple(d.keys())
v = tuple(d.values())
i = tuple(d.items())
print(k)              
print(v)#nesse bloco de código trasformo ele em uma tuple
print(i)
print('--------------------------------------------------')
print(d)
del d['Olá']#del exclui aparti da chave passada, também é sensivel a letras maiúsculas e minúsculas
print(d)
print('--------------------------------------------')
d.update(interesses=['autonomia', 'hack'])#adiciona chave e valor no dicionário chave e o valor em lista(mutável)
print(d)
d['interesses'].append('cerveja')# acessa valor dentro da chave interreses que é imutável e adicona valor com append
print(d)
retorno = d.pop('interesses')# o pop no dicionário ele remove e retorna a chave, neste caso esta atribuido a variável retorno
print(retorno)
print(d)
print('-----------------------------------------------')
t = tuple(d.items())# aqui ele returna uma tupla de tuplas
print(t)
print(dict(t))# aqui ele trasforma o t de tupla novamente em um dicionário
print(dict(nome='jorge Carvalho', cidade='Salvador',lat=22.9, long=43.1))
print('--------------------------------------------------------------------')
# Exercício de Dicionários
# Exercício 1: Criação e Acesso
# Crie um dicionário chamado meu_dicionario com as seguintes chaves e valores:
# Nome: 'Carlos'
# Idade: 30
# Cidade: 'Rio de Janeiro'
# Acesse e imprima o valor associado à chave 'Nome'.
# Altere o valor da chave 'Idade' para 31.
# Verifique se a chave 'Profissao' existe no dicionário e imprima o resultado (True ou False).
# Adicione uma nova chave 'Profissao' com o valor 'Engenheiro'.
meu_dicionario ={'nome':'carlos','Idade': 30, 'Cidade': 'Rio de janeiro'}
print(meu_dicionario['nome'])
meu_dicionario['Idade'] = 31
print('Profissao' in meu_dicionario)
meu_dicionario['Profissao'] = 'Engenheiro'
print(meu_dicionario)
# Exercício 2: Métodos de Dicionário
# Crie um dicionário chamado pessoa com as seguintes chaves e valores:
# Nome: 'Ana'
# Idade: 28
# Hobbies: ['leitura', 'corrida', 'música']
# Use o método get para tentar acessar a chave 'Endereco' e forneça um valor padrão 'Desconhecido' para o caso de a chave não existir.
# Use o método pop para remover a chave 'Idade' e armazene o valor removido em uma variável chamada idade_removida.
pessoa={'Nome':'Ana', 'Idade': 28, 'Hobbies':['leitura', 'corrida','música']}
print(pessoa)
endereco = pessoa.get('Endereco','Desconhecido')
print(f'O endereço é {endereco}')
idade_removida = pessoa.pop('Idade')
print(f'A idade removia foi {idade_removida}')
# Exercício 3: Iteração e Conversão
# Crie um dicionário chamado estoque com as seguintes chaves e valores:
# Produto1: 50
# Produto2: 30
# Produto3: 20
# Imprima todas as chaves do dicionário usando keys().
# Imprima todos os valores do dicionário usando values().
# Imprima todos os pares chave-valor do dicionário usando items().
# Converta as chaves do dicionário em uma tupla e imprima.
# Converta os valores do dicionário em uma tupla e imprima.
# Converta os pares chave-valor do dicionário em uma tupla de tuplas e imprima.
Estoque = {'Produto1': 50,'Produto2': 30, 'Produto3': 20}
chaves = Estoque.keys()
print(tuple(chaves))
Valores = Estoque.values()
print(tuple(Valores))
Pares_e_chaves = Estoque.items()
print(tuple(Pares_e_chaves))


# Exercício 4: Manipulação e Atualização
# Crie um dicionário chamado dados com as seguintes chaves e valores:
# Nome: 'Lucas'
# Cidade: 'Fortaleza'
# Lat: -3.717
# Long: -38.543
# Adicione uma nova chave 'Estado' com o valor 'Ceará'.
# Atualize o valor da chave 'Cidade' para 'São Paulo'.
# Verifique se a chave 'Pais' existe no dicionário. Se não existir, adicione a chave 'Pais' com o valor 'Brasil'.
# Imprima o dicionário completo.
Dados = {'Nome':'lucas','Cidade':'Fortaleza', 'lat':-3.717, 'long':-38543}
print(Dados)
Dados['Estado'] = 'Ceára'
Dados['Cidade'] = 'São Paulo'
if 'Pais' not in Dados:
    Dados['Pais'] = 'Brasil'
    print(Dados)
    