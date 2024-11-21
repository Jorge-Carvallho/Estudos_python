#Exercício 
# Adapte o código do desafio 107 criando uma função adicional chamada moeda()
# que consiga mostrar os valores como valor monetário formatado.

            # -------------->obs<-----------------#
# caso queria importa so apenas algumas funcionalidades, colocar:
# from arq_moeda import metade, dobro etc.. assim so importa o que é nescesario
# ou import arq_moeda que importa todo o módulo

import arq_moeda

# pre = float(input('Digite um preço: R$'))
pre = 100
print(f' A metade do R${arq_moeda.converte_moeda(pre)} é R${arq_moeda.converte_moeda(arq_moeda.metade(pre))}')
print(f' O dobro de R${arq_moeda.converte_moeda(pre)} é R${arq_moeda.converte_moeda(arq_moeda.dobro(pre))}')
print(f' Aumentando 10% em cima de R${arq_moeda.converte_moeda(pre)} temos R${arq_moeda.converte_moeda(arq_moeda.aumentar(pre,10))}')
print(f' Reduzindo 20% em cima de R${arq_moeda.converte_moeda(pre)} temos R${arq_moeda.converte_moeda(arq_moeda.diminuir(pre,20))}')


