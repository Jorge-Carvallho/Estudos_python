# Exercício 59
# Crie um programa que leia dois valores e mostre um menu como abaixo:
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1]Somar
# [2]Maior
# [4]Novos números
# [5]Sair do programa

# valor1 = int(input('Digite o primeiro valor: '))
# valor2 = int(input('Digite o segundo valor: '))
# opcao = int(input('''[1] Somar\n[2] Miltiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa
#                   \n>>>>> Qual é a sua opção? '''))
# while opcao != 5:
#     if opcao == 1:
#         resultado_soma = valor1 + valor2
#         print(f'A soma de {valor1} + {valor2} é {resultado_soma}')
#         print('=-='* 10)
#     elif opcao == 2:
#         resultado_multiplicacao = valor1 * valor2
#         print(f'O multiplicação de {valor1} x {valor2} é {resultado_multiplicacao}')
#     elif opcao == 3:
#         maior = 0 
#         if valor1 > valor2:
#             maior = valor1
#         else: maior = valor2
#         print(f'Entre {valor1} e {valor2} o maior valor é  {maior}')
        
    
#     elif opcao == 4:
#         print('Quais são os números novamente? ')
#         valor1 = int(input('Primeiro valor?  '))
#         valor2 = int(input('Segundo valor? '))
#     elif opcao == 5:
#         print('Saindo')
        
    
#     else:
#         print('Opcão inválida tente novamnete')
          
#     opcao = int(input('>>>> Qual é sua opção? '))
        
        
        
    # --------------------resolucão----------------------------
    
    
    
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        resultado_soma = n1 + n2
        print(f'O resultado da soma {n1} + {n2} é {resultado_soma} ')
        
    elif opcao == 2:
        resultado_multi = n1 * n2
        print(f'O resultado da multiplicação {n1} x {n2} é {resultado_multi}')
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
        
    elif opcao == 4:
        n1 = int(input('Digite um novo primerio número: '))
        n2 = int(input('Digite um novo segundo número: '))
        
    elif opcao == 5:
        print('Saindo')
    
    else:
        print('Opção Inválida >>>>>> Tente novamente: ')