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




