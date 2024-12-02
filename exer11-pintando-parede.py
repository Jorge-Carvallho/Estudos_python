# Exercício 11
# Faça um programa que leia a largura e altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area_tinta = 2

tamanho_area = largura * altura
sera_pintada = tamanho_area /  area_tinta

print(f'A sua parede tem a dimenção de {largura}x{altura}, e sua área é de {tamanho_area}.\n',
      f'Para pintar essa parede você precisará de {sera_pintada}L de tinta' )


