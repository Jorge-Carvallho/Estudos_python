#Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel.
def msg():
    print('Hoje foi show, amanhã tem muito mais!!')
    
def escreva():
   texto = input('Digite o texto: ')
   tamanho_do_texto = len(texto)

   print('-'* (tamanho_do_texto + 7))
   print(f'   {texto}    ')
   print('-' * (tamanho_do_texto + 7))
    
    
escreva()
msg()

