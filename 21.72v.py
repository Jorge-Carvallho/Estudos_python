# A essência de teste

def calc(a,b):
    return a + b

# Eu espero 3 quando calc(1, 2)
assert 3 == calc(1, 2)# sabendo que calc(1,2) = 3 
# O assert toda vez que o valor for false ele informa mensagem de AssertionError ex:
assert 2 == calc(1,1) # sabendo que cacl(1, 1) = 2 aqui ele informa AssertionError