# Exercício 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# --> Quantas vezes aparece a letra "A"
# --> Em que posição ele aparece a primeira vez
# --> Em que posição ele aparece a última vez

frase = input('Digite uma frase: ').upper().strip()
print('Quantas vezes apareceu a letra (a)--> ',frase.count('A'))
print('Retorna qual foi a primeiro indice da letra-->',frase.find('A')+1)
print('Retorna em qual posição ele apareceu por último -->',frase.rfind('A')+ 1)