# Exercício 79

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre_os em uma lista
# Caso o número já exista lá dentro, ele nã́o será adicionado
# No final serão exibidos todos os valores únicos digitados em ordem crescente.


valores = []                                 # lista

valor = int(input('Digite um valor: '))      # recebe valor do usuário
valores.append(valor)                        # adiciona valor do usúario a lista
print('Valor adicionado com sucesso...')
while True:                                   
    vamos_continuar = input('Deseja continuar [S/N]').strip().upper() # enquanto resposta for S continua
    if vamos_continuar != 'S':
        break
    valor = int(input('Digite um valor: ')) # aparti daqui recebe valor e se valor ja existir não adiciona
    if valor in valores:
        print('Valores já existe na lista')
    else:
        valores.append(valor)     # se valor nao exister la em cima ele adiciona aqui 
        print('Valor adicionado com sucesso...')











print(valores)




















