# Exercício 77
# Crie um programa que tenha uma tupla com vários palavras
# (Não usar acentos).Depois disso você deve mostrar,paara cada palavra,
# quais são as suas vogais.


# palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 
#             'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
#             'TRABALHAR', 'MERCADO', 'ROGRAMADOR', 'FUTURO')

# vogais = 'aeiou'

# for pos in range(0, len(palavras)):
#     print(f'\nA palavra {palavras[pos]} temos --> ',end='')
    
#     for letra in palavras[pos].lower():
#         if letra  in vogais:
#             print(letra, end='')
# print()
        
        # --------------------------------------
    
# for palavra in palavras:
#     print(f'\nNa palavra {palavra} temos as vogais',end=' ' )
#     for letra in palavra.lower():
#         if letra in vogais:
#             print(letra,end= ' ')

# -----------------------------resolução------------------------------------------


palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'ROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'\nA palavra {p} temos --> ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(),end='')
    
print()