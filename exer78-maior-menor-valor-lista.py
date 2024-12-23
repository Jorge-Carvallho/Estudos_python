# Exercício 78
# Faca um programa que leia 5 valores númericos e guarde-os em uma lista
# No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for v in range(0,8):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    f'Posição {c}, número {v}'       
        
        
maior_valor = max(valores)
posição_maior = valores.index(maior_valor)       


menor_valor = min(valores)
posição_menor = valores.index(menor_valor) 
        
print(f'O maior valor é {maior_valor} na posição {posição_maior} ')


print(f'O menor valor é {menor_valor} na posição {posição_menor}')