# Operações Aritiméticas

soma = 5 + 2                    # soma ------> 7
subtração = 5 - 2               # diminui ---> 3
multiplicação = 5 * 2           # multiplica-->10
divisão = 5 / 2                 # dividi ---->2.5

expónenciação = 5 ** 2          # número multiplicado por ele mesmo 2 vezes ---> 25
divisão_inteira = 5 // 2        # resultado da divisao interia --------------->  2
modulo = 5 % 2                  # resto da divisão ----------------------------> 1

#Ordem de Precedência
# 1 ()
# 2 **
# 3 *, /, //, %
# 4 +, -

calculo1 = 5 + 3 * 2 #--> resolve 3 * 2 = 6, depois 6 + 5 
print('Calculo1 é --> 5 + 3 * 2')
print(f'Resultado de calculo1 é { calculo1}\n')

calculo2 = 3 * 5 + 4 ** 2 #-->resolve 4 ** 2 = 16, depois 3 * 5 = 15, depois 15 + 16 = 31
print('Calculo2 é --> 3 * 5 + 4 ** 2')
print(f'Resultado de calculo1 é { calculo2}\n')


calculo3 = 3 * (5 + 4) ** 2 # --> resolve (5 + 4) = 9, depois 9 ** 2 = 81, depois 3 * 81 = 243
print('Calculo3 é --> 3 * (5 + 4) ** 2')
print(f'Resultado de calculo1 é { calculo3}')

# obs: posso fazer potencia usando função pow(), --> perco a orden de procedência
potencia = pow(4,3)
print(f' --> {potencia}')
print('='* 60)


#Centralizar strings -------->

nome =  'Gustavo' #  poderia ser um ----> input('Qaul o seu nome: ')
print(f'Prazer em te conhecer {nome}')
print(f'Prazer em te conhecer {nome:>20}')# alinhado com 20 caracteres a esquerda
print(f'Prazer em te conhecer {nome:<20}')# alinhado com 20 caracteres a direita
print(f'Prazer em te conhecer {nome:^20}')# alinhado com 20 caracteres ao centro
print('='* 60)
print(f'Prazer em te conhecer {nome:=>20}')# alinhado com 20 caracteres a esquerda completando com =
print(f'Prazer em te conhecer {nome:=<20}')# alinhado com 20 caracteres a direita completando com =
print(f'Prazer em te conhecer {nome:=^20}')# alinhado com 20 caracteres ao centro completamdo com =

print('='* 60)

# n1 = int(input('Digite um valor: '))
# n2 = int(input('Outro valor: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2

# print('A soma vale {}, a multiplicação vale {}, e a divisão vale {:.3f}'.format(s, m, d))
# print('Divisão inteira {}, a potência {}'.format(di, e))

# obs: ---> 
#           {:.3f} significa quando numeros terei depoiius da virgula, neste caso 3 --> 1.555
#           {:.2f}------> terei 2 números depois da virgula --> 1.34
# -----------------------------------------------------------------------------------
# --> \n = pula de linha ou quebra a linha dentro do print
print('A soma,\n a multiplicação\n e a divisão')
# --> ,end='' --> da seguimento a conteudo da linha.
print('A soma, a multiplicação e a divisao',end=' ')