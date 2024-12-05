# Exercício 34
# Escreva um progrma que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# para os inferiores ou iguais o aumento é de 15%


salario_base = 1250
seu_salario = float(input('Qual o salário do funcionário: '))


if seu_salario <= salario_base:
    salario_atualizado =  seu_salario +(seu_salario * 15 / 100)
    print(f'Quem ganhava R${seu_salario:.2f} teve um aumento de 15%, passa a ganhar R${salario_atualizado:.2f}')
else:
    salario_atualizado = seu_salario + (seu_salario * 10 / 100)
    print(f'Quem ganhava R${seu_salario:.2f} teve um aumento de 10%, passa a ganhar R${salario_atualizado:.2f}')
    