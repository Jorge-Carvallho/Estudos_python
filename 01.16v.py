# import os

# Quando o comando `import` é usado, o Python busca no `PYTHONPATH` para verificar se existe um módulo com o nome especificado. 
# Ele procura no diretório atual e em outros locais da biblioteca padrão. O módulo `os` já faz parte da biblioteca padrão (ele processa o código fonte uma vez e depois o mantém em cache na memória). 
# Em seguida, cria uma variável local com o nome do módulo. No exemplo abaixo, podemos importar o módulo com outro nome, se desejado.
# Um alias é como um apelido que você dá a algo no código para torná-lo mais fácil e rápido de usar. É uma forma prática de simplificar referências, mantendo o código mais legível e conciso.
import os as asdf
print(type(asdf)) #  modulo (OS)

xpto = asdf

print(type(xpto))

print(id(xpto))
print(id(asdf))
print()

# possuem o mesmo id, pois referencia o mesmo objeto

from os import getcwd
print(getcwd())  # getcwd retorna o diretório no qual estou(diretório atual)
from os import getcwd as xyz
print(xyz()) # xyz é um alias para getcwd

print()
print(id(getcwd()))
print(id(xyz()))  # ambos ids são iguais


