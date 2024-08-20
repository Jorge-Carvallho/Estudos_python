
# Programação Orientada a Objeto 
#Observe que foods e bag tem o mesmo valor de objeto porém suas identidades de memórias são únicas e diferentes,ou seja ( não são o mesmo objeto)

foods = ['maçã', 'laranja', 'gato']
bag = ['maçã', 'laranja', 'gato']
print('-----------------------------------FOODS--------------------------------')
print(foods)# valor de foods
print(id(foods))#identidade de foods(endereço de memória)
print(type(foods))#tipo do dados do objeto que esta em foods que neste caso é list
print('-------------------------------------------------------------------')

print('------------------------------------BAG-----------------------------')
print(bag)# valor de bag
print(id(bag))#identidade de bag / endereco de memória
print(type(bag))#tipo de dado do objeto que esta em bag
print('---------------------------RESULTADO / COMPARADOS-------------------------------------------')

resultado = foods,bag
print(resultado)
print(foods == bag) # aqui irei saber se os objetos fodds e bag são o mesmos valor ou / equivalentes
print(foods is bag) # aqui irei saber se foods e bag são o memso objeto return falso pois são objetos diferentes
print( id(foods), '\n',id(bag))# são objetos diferentes embora são equivalentes
print('---------------------------------------------------------------------------')

print(type(foods))# retorna o tipo do objeto que nesse caso é uma lista 
#posso ussar a clase do tipo do objeto de cima e instancia um novo objeto com a mesma classe
cls = type(foods)
print(cls)
print(cls((1,2,3))) # cls agora é uma lista também com elementos 1,2,3
# Quando eu chamo  cls((1, 2, 3)),basicamente estou chamando a classe list que cls está referenciando,  com um argumento que é uma tupla (1, 2, 3). No caso de list, ao passar a tupla (1, 2, 3), a tupla é convertida em uma lista, resultando em [1, 2, 3].
