#Manipulando indíces

nome = 'extraordinario'

print(len(nome))# retorna o tamanho da string 
print(nome[0])# acesso primeiro elemento da str atraves de indice
print(nome[-1])# acesso o último elemento da str/ se começa em 0, -1 então é o último elemento
# slice fatia a str atraves do : dentro de cochete
print(nome[0:4])# retorna do indice 0 até indice 4 apenas ou seja o indice 0,1,2,3
print(nome[1:])# retorna aparti do indice 1 até o final, está omitido o indice depois do :
print(nome[:4])# da mesma forma posso omitir o primeiro indice levando em conta que comeca pelo 0 ate o 4 nesse caso
print(nome[:])# retorna do início até o final pois foi omitido 
print(nome[1:14:2]) # segundo : significa passo, então do 1 ate o 14 letra passo de 2 em 2
print(nome[::2])# pegara do início até o final de 2 em 2 foi omitido os 2, foi omitido o inicio e o final
print(nome[::-1])# pegara do final ate o comeco, começando de de -1 ou seja do final ate a frente 
print('-----------------------------------------------------------')

#exercícios
#Crie uma variável chamada palavra e atribua a ela a string: "incrível".
palavra = 'Incrível'

#Utilize a indexação e slicing para realizar as seguintes operações:
#Imprima o comprimento da string.
#Acesse e imprima o primeiro caractere da string.
#Acesse e imprima o último caractere da string.
#Faça um slice que capture e imprima os primeiros 5 caracteres da string.
#Faça um slice que capture e imprima a string a partir do índice 3 até o final.
#Faça um slice que capture e imprima a string até o índice 4 (não incluído).
#Faça um slice que capture e imprima toda a string.
#Faça um slice que capture e imprima a string a partir do índice 2 até o índice 7, com passo de 2.
#Faça um slice que capture e imprima a string do início ao fim, com passo de 3.
#Imprima a string de trás para frente utilizando slicing.
print(len(palavra))
print(palavra[0])
print(palavra[-1])
print(palavra[:5])
print(palavra[3:])
print(palavra[:4])
print(palavra[:])
print(palavra[2:7:2])
print(palavra[::3])
print(palavra[::-1])
