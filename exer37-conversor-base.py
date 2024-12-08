# Exercício 37
# Escreva um programa que leia um número inteiro qualquer
# e paça para o usuário escolher qual será a base de conversão:


num = int(input('Digite um número inteiro: '))
print('''Escolha um das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O número {num} convertido para BINÀRIO é --> {bin(num)[2:]}')

elif opcao == 2:
    print(f'O número {num} convertido para OCTAL é --> {oct(num)[2:]}')

elif opcao == 3:
        print(f'O número {num} convertido para HEXADECIAML é --> {hex(num)[2:]}')

else:
    print('Opção inválida, tente novamente.')