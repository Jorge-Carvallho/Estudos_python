# Escreva um programa pra aprovar um empréstimo bancário para a compra de uma casa
# O programam vai perguntar o valor da casa, o salário do comprador e em quantas anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado

valor_casa = float(input('Qual o valor do imóvel: '))
salario = float(input('Qual o salário do comprador: '))
anos_a_pagar = float(input('Quantos anos ele vai pagar: '))

anos_a_pagar = anos_a_pagar * 12 # converte anos em meses
valor_da_parcela = valor_casa / anos_a_pagar # gera valor da parcela
salario_ate = salario * 30/100 # retorna valor do salário

if valor_da_parcela > salario_ate:
    print('Exedeu o limite de 30% do salário')
    print(f'Valor da parcela ficou R${valor_da_parcela:.2f}')
    print(f'Sua parcela limite é R${salario_ate}')
else:
    print(f'Compra aprovada, sua parcela ficou R${valor_da_parcela:.2f} de máximo R${salario_ate}')





