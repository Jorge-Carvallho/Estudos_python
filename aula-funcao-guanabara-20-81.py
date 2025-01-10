



#Função Guanabara

def linha():
    print('-'* 30)

def msg():
    print('       Bem vindo')
    print('    Vamos estudar Python')


linha()
msg()
#-----------------------------------------------------------------------------------------------------------------------------

linha()
def soma(a,b):
    s = a + b
    print(s)

soma(1,2)
soma(2,3)                                   # ambas são as mesmas função de forma diferentes
soma(4,4)
soma(b=3,a=1)

linha()
# ou 

soma_lambda = lambda a,b: print(f'A soma de {a} + {b} é:  {a + b}')
soma_lambda(1,2)
soma_lambda(2,2)
linha()
#------------------------------------------------------------------------------------------------------------------------------

#Empacotamento returna uma tupla:
# O (*num) recebe argumentos indica que a função pode receber um número variável de argumentos. Todos esses argumentos são empacotados em uma tupla chamada num.......quando chamada irar desempacotar  varios valores,e retorna como uma tupla
# def contador(*num):
#     for valor in num:
#         print(f'{valor}', end=' ')
#     print('Fim')
      #ou
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores de {num} e são ao todo {tam} números')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
linha()

#ou

contador1 = lambda *x: print(x)

(2,1,7)
contador1(8,0)
contador1(4,4,7,6,2)
linha()

# --------------------------------------------------------------------------------------------------------------

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+= 1
    return lst
        
        
valores = [2,3,4,2,5,7]
print(dobra(valores))







