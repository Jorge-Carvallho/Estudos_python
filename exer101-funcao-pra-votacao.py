# Exercicio 101
# Crie um programa que tenha a função chamada voto() que vai receber como parâmetro,
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL, OBRIGATÓRIO, nas eleições.


from datetime import datetime

print('-'*50)
def voto(nasc):
    idade = datetime.now().year - nasc
    if idade < 18:
        return f'Com {idade}: Voto negado'
    elif idade >= 18 and idade <= 65:
        return f'Com {idade}: Voto obrigatório'
    else:
        return f'Com {idade}: Voto opcional'
    


ano_nasc = int(input('Em que ano você nasceu: '))

print(voto(ano_nasc))




