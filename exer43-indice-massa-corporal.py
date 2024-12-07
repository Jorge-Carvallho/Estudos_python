# Exercício 45
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu imc e mostre seu status,
# de acordo com a tabela abaixo:

# -Abaixo de 18.5: Abaixo do peso         - Entre 30 até 40: Obesidade
# -Entre 18.5 e 25: Peso ideal            - Acima de 40: Obesidade Mórbida
# -Entre 25 até 30: Sobrepeso


peso = float(input('Inforrme seu peso atual: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura **2)
if imc <= 18.5:
    print(f'Seu imc está em {imc:.2f} --> Abaixo do peso')
    
elif imc <= 25:
    print(f'Seu imc está em {imc:.2f} --> Ideal')

elif imc < 30:
    print(f'Seu imc está em {imc:.2f} --> Sobrepeso') 
    
elif imc <= 40:
    print(f'Seu imc está em {imc:.2f} --> Obesidade')

else:
    print('Obesidade Mórbida')