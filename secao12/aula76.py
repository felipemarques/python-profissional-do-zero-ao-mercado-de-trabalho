arquivo = open('texto.txt', 'r')
print(arquivo.read())
arquivo.seek(20)

print(arquivo.read())
arquivo.close()