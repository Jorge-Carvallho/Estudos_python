#Atribuições
# 
# row = 'Henrique', 'Noterói', 22.9, 43.1

# def f(t):# função f com valor de t atrabuido a variavel row fora da função chamando
#     # nome = t[0]
#     # cidade = t[1]# valores de nome, cidade lad, long, atribuidos aos valores t[indices] fora do escopo da função
#     # lat = t[2]
#     # long = t[3]
# #poderia ser formas abaixo ---v: 
#     # nome,cidade,lat,long = t[0], t[1],t[2],t[3]
#     nome,cidade,lat,long = t
#     print(nome, cidade, lat, long)
    
# if __name__ == '__main__':
#     f(row) # função f aqui chamando row passado como valor t para dentro da função
print('---------------------------------')
#Usando andescor
# def f(t):
#     nome, *_, long = t # o underscore aqui guarda todo o resto no *_ ( o modificador é o *  para testar os resultados so movimentar)
#     print(nome, long, _)# o underscore aqui passa todo o resto para uma lista 

# if __name__ == '__main__':
#     f(row)
#     print('----------------------------------------')

table = (('Henrique', 'Noterói', 22.9, 43.1),
         ('Vinicius', 'Santarém', 2.4, 54.7))

for row in table:
#     nome = row[0]
#     cidade = row[1]
#     lat = row[2]
#     long = row[3]
# #forma simplificada
    nome,cidade,lat,long = row
    print(nome, cidade, lat, long)
# posso fazer dentro do for abaixio exemplo:
print('-------------------------------------')

# for nome,cidade,lat,long in table:# aqui também posso usar underscore ( *_)
for name, *_, in table:# esse underscore agrupa os valores a lista 
    print(nome,_, long) # o que tiver agrupado no underscore de cima mostra a lista com a declaração deste 

