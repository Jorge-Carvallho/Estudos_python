# Aula 12 Condicionais Alinhnadas 
nome  = str(input('Qual seu nome: '))
if nome == 'Jorge':    # ---------------> estrutura condicional simples
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #----> com elif vira uma estrutura alinhada
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Lais Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.') #-----> estrutura composta

print(f'Tenha um bom dia, {nome}!')