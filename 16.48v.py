# Raw String
import re
#  Raw string impedem que caracteres de controle sejam interpretados e os caracteres sejam tratados como string ex:
text = '\\section\n'
print(re.match('\\section', 'text'))# retornou None pois o \\s foi interpretado como caracter de controle
print(re.match(r'\\section', text))# agora usando o  --> r <-- a frente   --> '' <--ele é interpretado apenas como string
print(re.findall(r'\\section', text))