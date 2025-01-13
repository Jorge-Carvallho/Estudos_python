# Aula Funçôes

# def linha():
#     print('-='*12)


# linha()
# print('     Curso em Vídeo     ')
# linha()

# linha()
# print('     Aprenda Python     ')
# linha()

# linha()
# print('     Jorge carvalho     ')
# linha()
# # -------------------------------------------------------------------------------

# def mensagem(msg):
#     print('-='* 9)
#     print(msg)
#     print('-='* 9)
    
# mensagem('SISTEMA DE ALUNOS')
# -----------------------------------------------------------------------------------

# def soma(a,b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de {a} + {b} = {s}')


# soma(2,4)
# ----------------------------------------------------------------------------------

def contador(*num):                  # * significa desempacotar, onde será passado varis parâmetros
    for valor in num:               #-----------------------> retorna uma tupla
        print(f'{valor}', end=' ')
    print('Fim!')
    

    
# contador(2,3,5,67,7)
# contador(22,2,22,4,5)
# contador(2,4,3,6,)
# -------------------------------------------------------------------------------------------------

# def contador(*num):                  # * significa desempacotar, onde será passado varis parâmetros
#    tam = len(num)
#    print(f'Recebi os valores {num} e o tamonho são {tam}')

    
# contador(2,3,5,67,7)
# contador(22,2,22,4,5)
# contador(2,4,3,6,)

# --------------------------------------------------------------------------------------
# valores = [2,7,8,4,5,1,7,]

# def dobra(lts):
#     pos = 0
#     while pos < len(lts):
#         lts[pos] *=2
#         pos +=1


# dobra(valores)
# print(f'A lista dobrada é {valores} ')
# -------------------------------------------------------------------------------------------

# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f' A soma dos valores {valores} é --> {s}')


# soma(2,3,5,3,5,3,2,)