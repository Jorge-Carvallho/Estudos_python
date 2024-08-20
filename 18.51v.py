#Named Groups
import re

html1 = '<input type="text"id="id_cpf"name="cpf">'
html2 = '<input id="id_cpf" name="cpf" type="text">'

patterns = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(?P<id>.+?)"|name="(?P<name>.+?)")?)*'
# print(patterns)

m = re.match(patterns,html1)
s = m.groups()
d = m.groupdict()
print(m)
print(s)
print(d)