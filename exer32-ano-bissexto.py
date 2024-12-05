import datetime

num = int(input('Digite um ano ou 0 para verificar o ano atual: '))

if num == 0:
    num = datetime.datetime.now().year
    
if num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
    print(f' O ano {num} é Bissexto')
elif  num % 4 == 0  and num % 100 != 0:
    print(f'O ano {num} é Bissexto')
else:
    print(f'O ano {num} não é Bissexto')

    

    