# Exercício 48
# Faça um programa que calcule a soma entre todos os números impares
# que sao multiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range(1,500):
    if c % 2 != 0  and c % 3 == 0:# se número mod 2 diferente de 0,(ou seja impar) e mod 3 igual a 0
        #ou seja(que são divisiveis por 3  e o resto é zero, mostre)
        soma += c
        print(c)# aqui mostra apoenas os numeros impares multiplos de 3
print(f'total dos multipliplos por 3 no intervalo de 1 até 500 é {soma}')
        