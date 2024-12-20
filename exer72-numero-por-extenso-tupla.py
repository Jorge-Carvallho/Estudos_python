# Exercício 72
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso de zero até vinte
# Seu programa deverar ler um número pelo teclado entre (0 até 20)e mostra-lo por extenso.


numeros_por_extenso = ('zero', 'um','dois','três','quatro','cinco','seis','sete',
                       'oito','nove','dez','onze','doze','treze','quatorze',
                       'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros_por_extenso[num]}')
        break
    else:
        print('Número fora do intervalo permitido')
        
    

