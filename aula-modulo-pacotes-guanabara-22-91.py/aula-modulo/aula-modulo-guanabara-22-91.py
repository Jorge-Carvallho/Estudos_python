#Módulos e Pacotes
 
# caso 1--> (import uteis): --> preciso chamar uteis.fatorial,uteis.dobro,uteis.triplo
    #ou --> Neste caso, você importa o módulo inteiro, e para acessar as funções, 
        # você precisa referenciá-las com o nome do módulo: Essa abordagem é útil se você quer manter o código organizado e deixar claro que as funções pertencem ao módulo uteis. Também evita conflitos de nomes caso existam funções com os mesmos nomes em outros módulos.
              #------------------------------------------------------------------    
    
# caso 2--> (from uteis import fatorial,dobro,triplo): --> #--> as funcões ja foram chamadas pelo import,
    #ou --> Aqui, você está importando diretamente as funções específicas. Com isso, pode chamá-las 
        # diretamente pelo nome, sem precisar prefixar com uteis: Essa abordagem é prática quando você sabe exatamente quais funções vai usar e quer evitar escrever o nome do módulo repetidamente. Porém, tenha cuidado com possíveis conflitos de nomes.


        #obs: primerio nome é o nome do módulo, o segundo nome é o nome da função



import uteis1 #                      ----> mas recomendada

# from uteis import fatorial, dobro, triplo # ---> menos recomendada


num= int(input('Digite em valor '))
fat= uteis1.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {uteis1.dobro(num)}')
print(f'O Triplo de {num} é {uteis1.triplo(num)}')

#----------------------------------------- Pacotes --------------------------------------------

 