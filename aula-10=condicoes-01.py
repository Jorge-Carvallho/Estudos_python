# Aula Condiçoẽs (parte 1)

# nome = str(input('Qual seu nome: '))
# if nome == 'Jorge':
#     print('Seu nome é bonito!')
# else:
#     print('Seu nome é tão normal')
# print(f'Bom dia, {nome}')
# --------------------------------------------------------------------------
print('-'* 20)


n1 = float(input('Digite priemrioa nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')


if m >= 6.0:
    print('Sua media foi boa!')
else:
    print('Sua média foi ruim, estude mais!')