# Exercício 13
# Faça um algoritimo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento.

# obs: ------> 2 formas de do cálculo

salario = float(input('Qual o salário do Funcionário? '))

novo_salario = salario + (salario * 15 / 100)
noov_salario = salario * (1 - 15 / 100)
print(f'O funcionario que ganahva R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}')



