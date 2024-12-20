# Exercício 73
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela
# do Campeonato Brasileiro de futebol, na ordem da colocação, depois mostre:
# Apenas os 5 primerios colocados
# Os últimos 4 colocados da tabela
# Uma lista com os times em ordem alfabética
# Em que posição na tabela o time esta o time do Bahia

times = ('Botafogo','Palmeiras','Flamengo','Fortaleza',
         'Internacional','São Paulo','Corinthins','Bahia','Cruzeiro',
         'Vasco da Gama','Ec Vitória','Atlético-MG','Fluminense','Grêmio',
         'Juventude','Bragantino', 'Athetico-PR','Criciuma','Atlético_GO','Cuiabá')


print(f'Os Primerios 5 colocados são {times[0:5]}')
print(f'Os ultimos 4 colocados são {times[-1:-5:-1]}')
print(f' A lista dos times em ordem alfabetica é {sorted(times)}')
print(f'O time do Bahia na posição {times.index('Bahia')} da tabela')