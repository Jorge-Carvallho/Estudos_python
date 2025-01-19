# Exercício 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de um aluno
# e vai retorna um dicionário com as seguintes informações:
#     - Quantidade de notas
#     - A maior nota
#     - A menor nota
#     - A média da turma
#     - A situação (opcianal)
#     - Adicione também uma docstring



def notas(*n,situação=False):
    """
    Função para analisarnotas e situação de vários alunos:
    -param n: um aou varias notas dos aluos(aceita varias)
    -param situação: valor opcional,indicando se deve ou não adicionar situação
    -return: dicionário com varias informações sobre a situação da turma.
    """
    
    r = dict()
    r['total notas'] = len(n)
    r['maior nota'] = max(n)
    r['menor nota'] = min(n)
    r['media'] = sum(n)/len(n)
    if situação:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'          
          
    return r

# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, situação=True)
print(resp)
help(notas)

# -------------------------- Exercicio Teste ----------------------

# Faça um programa que tenha uma função chamada analisar_temperaturas() que receba várias temperaturas (em graus Celsius) como argumentos e retorne um dicionário com as seguintes informações:

# Quantidade de temperaturas recebidas.
# A temperatura mais alta.
# A temperatura mais baixa.
# A temperatura média.
# Uma análise opcional (especifique como parâmetro analise=False):
# "Muito Quente" se a média for maior ou igual a 30ºC.
# "Agradável" se a média estiver entre 20ºC e 29.9ºC.
# "Frio" se a média for menor que 20ºC.



def analisar_temperatura(*temp, situacao=False):
    t = dict()
    t['Temper. mais alta'] = max(temp)
    t['Temper. mais baixa'] = min(temp)
    t['media de temper'] = sum(temp)/ len(temp)
    if situacao:
        if t['media de temper'] > 27:
            t['situação'] = 'Já esta muito calor'
        elif t['media de temper'] >= 20:
            t['situação'] = 'Temperatura agradavel'
        else:
            t['situação'] = 'Já esfriou pra caramba'
    
    return t
    
resp = analisar_temperatura(30,20,29,24,situacao=True)
print(resp)