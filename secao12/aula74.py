arquivo = open('texto.txt', 'r', encoding='utf-8')
print(type(arquivo))
texto = arquivo.read()
print(type(texto))
print(texto)
arquivo.close()