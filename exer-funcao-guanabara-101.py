#Exercício
#Crie um programa que tem uma função chamada voto() que vai receber um parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGATÓRIO,nas eleições

def voto(ano_de_nasciemnto):
    ano_atual = 2024
    idade = ano_atual - ano_de_nasciemnto
    if idade >= 18 and idade <=69:
        print(f'Com {idade} anos, meu VOTO É OBRIGATÓRIO')
    elif idade >= 16 and idade >69:
        print(f'Com {idade} anos, meu VOTO É OPCIONAL')
    else:
        print(f'Com {idade} anos, NÃO VOTA')
 
    
ano = int(input('Digite seu ano de nascimento: ')) # solicita do usúario ou,  da forma direta abaixo
voto(ano)




# voto(2015)
# voto(1990)
# voto(1950)
    

    