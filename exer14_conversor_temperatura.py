# Exercício 14
# Escreva um programa que converta uma temperatura digitada em Cº converta para ªF.

# obs: ------> 2 fórmulas diferentes abaixo
cª = float(input('Informe a temperatura em Cª: '))
fª = ((9 * cª) / 5) + 32
# fª = cª * (9 / 5) + 32

print(f'A temperatura em {cª}ªC corresponde a {fª}ªF!')