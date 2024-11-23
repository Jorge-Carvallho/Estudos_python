            #------------> Falha Sintática <---------------

# É um erro no código que impede o programa de ser interpretado ou compilado. 
# Ocorre porque o código não segue as regras da linguagem de programação.
# É detectado antes da execução do programa, durante a análise do código pelo compilador ou interpretador.

            #  -----------> Exceção < -----------------

# É um problema que ocorre durante a execução do programa, mesmo que o código esteja sintaticamente correto.
# Representa situações que o programa não consegue tratar por conta própria, como operações inválidas ou recursos indisponíveis.

        
# estrutura do try/execept
# try (tente):
#     Aqui você coloca o código que quer tentar executar. É onde pode ocorrer um erro.

# except (exceção):
#     É onde você lida com os erros que podem ocorrer no bloco try. Se um erro acontecer, o código dentro do except será executado.

# else (caso funcione):
#     Opcional. Se não ocorrer nenhum erro no bloco try, o código no else será executado.

# finally (sempre execute):
#     Opcional. O código aqui será executado sempre, independente de erro ou sucesso no try. É útil para fechar arquivos, liberar recursos, etc.


#-----> exemplos abaixo:

# try:
#     n   = int(input('Digite um número: '))
#     print(n)
    
# except:
#     ValueError
#     print('Foi digitado uma palavra e não um número')
    
      #------------------------------------------------------------------------------------------#
      
try: # == tente --> dentro é a opereção
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError) as e:
    print(f'Problema com tipos de dados digitados, foi {e.__class__}')

except ZeroDivisionError as e:
    print(f'Não é possivel dividir número pelo denominador zero, --> {e}')

except KeyboardInterrupt as e:
    print(f'O usuário preferio não informa os dados --> {e} ')
    
except Exception as erro_foi:
    print(f' O erro encontrado foi { erro_foi.__cause__}')
    
    # ou 
    # ZeroDivisionError, ValueError
    # print('Erro, na matemática da erro numerador não pode ser dividido por 0, ou a entrada não foi um número ')
    
else: #== se deu certo --> aqui dentro vai acontecer se der certo
    print(f'O ressultado é {r:.1f}')
# except Exception as erro:
    
#     print(except)
# except Exception as deu_erro: # == se falhar --> busca o erro e tratar 
# # #     print('Tivemos um problema:')
# # #     print(f'O problema encontrado foi  ----> {deu_erro.__class__}')







# except Exception as deu_erro: # == se falhar --> busca o erro e tratar 
# #     print('Tivemos um problema:')
# #     print(f'O problema encontrado foi  ----> {deu_erro.__class__}')