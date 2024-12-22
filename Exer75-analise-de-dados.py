# Exercício 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
#     a) Quantas vezes apareceu o valor 9
#     b)Em que posição foi digitado o primeiro valor 3 
#     c)Quais foram os números pares

numero = (
    int(input('Digite primerio número: ')),
    int(input('Digite segundo número: ')),
    int(input('digite o terceiro valor: ')),
    int(input('Digite o quarto valor: '))
)

print(f'Você digitou os valores {numero}')

print(f'O número 9 apareceu, {numero.count(9)} vezes')
if 3 in numero:
    print(f'O número 3 apareceu na {numero.index(3)}ª posição')
else:
    print('Valor 3 não foi digitado')
print(f'Os números pares foram: ',end = '') 
for c in numero:
  if c % 2 == 0:
    print(c,end=' ')
print()


    


    
