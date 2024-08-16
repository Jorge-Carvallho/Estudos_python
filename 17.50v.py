#Repetições
import re
# Quantidades expecificas
# reforçando o --> r <-- tem efeito de fazer o \ ser interpretado com valor literal, neste caso abaixo \d se refere a um codigo de sequência de expressões regulares 0 - 9 então :
print(re.match(r'\d{4}','1234'))# emprimir de 0 a 9 no exatamente \d(0-9), {4}(exatamente 4), padrão(1234)
# padrao = '12131415'
# resultado = re.match(r'\d{4}', padrao)# neste exemplo so retorna exatamente os primeiros 4
# print(resultado)
# a Interrogação --> ? <-- é um modificador de repetição que trasforma a busca do padrâo em preguiçosa, ou seja, ele pegarar sempre o mínimo doq ue foi pedido ex:   quero de 1 ate 4, ele trarar sempre o mínimo que é 1 por mas que tenha outros
print('----------------------------------------------------------------------------')

# Quantidade mínima na repetição
print('---------------------------------1-------------------------------------')
padrao1 = '12131415'
resultado = re.match(r'\d{2,}', padrao1)# aqui retorna no mínimo 2 números porém mas o que vinher a mais é imprimido
print(resultado)
print('----------------------------------2--------------------------------')
#  pra torna ele preguiçoso preciso colocar uma interrogação para barra ele ate apenas o mínimo, o que passar não é imprimindo
resultado1 = re.match(r'\d{2,}?', padrao1)
print(resultado1)
print('----------------------------------3-----------------------------------\n')


# Mínimo e Máximo
padrao2 = '12131415'
resultado2 = re.match(r'\d{2,5}', padrao2)# imprime apenas objetos entre os parâmetros no mínimo 2 e no máximo 5 
print(resultado2)


print('-----------------------------------4---------------------\n')
padrao3 = '12131415'
resultado3 = re.match(r'\d{,1}',padrao3)# farei o mesmo exemplo em baixo usando  a -----> ? <----
print(resultado3)

resultado4 = re.match(r'\d??', padrao3)# a primeira --> ? <--referencia ao minimo é máximo que seria 0 e 1:
# a segunda  --> ? <-- é o modificador de repetição para trasforma ele em preguiçoso
print(resultado4)


print('------------------------------------5----------------------')
padrao4 = '12131415'
resultado5 = re.match(r'\d{,}', padrao4)# padrão onde verifica e retona 0 ou mais vezes do padrão, com sempre para trasforma ele como preguiçoso e ele tazer apenas o mínimo usar a ?, 
# mas também posso omitir esse padrão usando o * segnifica também 0 ou mas vezes de aparições
print(resultado5)
resultado6 = re.match(r'\d*',padrao4)
print(resultado6)
print('------------------------------------6----------------------------')

padrao5 = '12131415'
resultado7 = re.match(r'\d{1,}',padrao5)
resultado7 = re.match(r'\d+', padrao5)# padrão usando o sinal de --> + <-- retorna pelo menos um caracter numeral 
print(resultado7)
print('------------------------------------7------------------------------')

#Extraindo todos os valores dos atributos
text = 'attr1="value1" attr2="value2"'
# resultado8 = re.findall(r'".+"', text)# aqui é busca qualquer caracter que esteja entre --> ."" que tenha pelo menos 1 ocorrência --> +
# resultado8 = re.findall(r'".+?"', text)# aqui busca a forma correta apenas com valores dos atributos, caso perfeito para o uso do modificador de repetição --> ? porem: caso de erro se alguma ocorrencia estiver vazia dara erro pois ele exige pelo menos uma ocorrencia, forma correta abaixo: pra suporta 0 ou mas ocorrencia:
text1 = 'attr3="" attr4=""'
resultado9 = re.findall(r'".*?"', text1)
print(resultado9)
print('-----------------------------------------------------------------------')

#Mactch e search object --> retorna métodos group, start, end, span
pattern = '98765'
result_pattern =re.match(r'\d+',pattern)# aqui dentro do padrão match estou retornando pelo menos um caracter numeral do codigo sequncial \d que significa de 0-9, dentro desse padrão existe métodos group, start, end, span
print(result_pattern)
print(result_pattern.group())# retorna o grupo do que foi feito match
print(result_pattern.start())# retorna o primeiro indice caracter encontrado match
print(result_pattern.end()) # retorna o ultimo indice cararcter encontado match
print(result_pattern.span())# retona o indice inicial e final em uma tupla
# 8:34\50
print(re.match(r'\s+', pattern))# nessa expressão \s busca se a algum espaco em branco e o --> + <-- se a uma ou mas ocorrencias