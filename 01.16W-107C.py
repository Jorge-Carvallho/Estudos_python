"""# import os

# Quando o comando `import` é usado, o Python busca no `PYTHONPATH` para verificar se existe um módulo com o nome especificado. 
# Ele procura no diretório atual e em outros locais da biblioteca padrão. O módulo `os` já faz parte da biblioteca padrão (ele processa o código fonte uma vez e depois o mantém em cache na memória). 
# Em seguida, cria uma variável local com o nome do módulo. No exemplo abaixo, podemos importar o módulo com outro nome, se desejado.
# Um alias é como um apelido que você dá a algo no código para torná-lo mais fácil e rápido de usar. É uma forma prática de simplificar referências, mantendo o código mais legível e conciso.
import os as asdf
---quando coloco import (os)  o python carrega o código do módulo (os) na memória e cria uma referencia global com o nome (os) no namespace, e posso mudar o nome da referencia em vezde os qualer outro nome como exemplo, --> import os as asdf --> o (as) aqui está significando (alias) que é o memso de atribuindo um novo nome:
print(type(asdf)) #  modulo (OS)

--- registrar que o alias pode ser usado como palavra chave em outros aspectos com por exemplo renomear um comando ex: alias ls= 'ls -lh' ---> significa que estou atribuindo o ls -lh ao ls


"""
import os as asdf #asdf é um apelido para os e abaixo xpto é um apelido para asdf que por sua vez um apelido para os
#ou seja tenho 3 variaveis (os) (asdf) (xpto) referenciando o memso objeto 
# possuem o mesmo id, pois referencia o mesmo objeto
xpto = asdf
print(type(xpto))
print(id(xpto))
print(id(asdf))
print()


"""
Quando eu coloco: 
from os import getcwd --> significa que estou importando apenas o recurso getcwd de dentro do código e não o módulo (os) inteiro
 getcwd retorna o diretório no qual estou; o (diretório atual)

"""

from os import getcwd
print(getcwd())  # getcwd retorna o diretório no qual estou; o (diretório atual)
from os import getcwd as xyz # auqi com a (as) estou mudando o nome do getcwd para xyz
print(xyz()) # xyz é um alias para getcwd


import os
print()
print(id(getcwd))
print(id(xyz)) 
print(id(os.getcwd))# ambos ids são iguais
# possuem o mesmo id, pois referencia o mesmo objeto

