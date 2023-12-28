import os

arquivos = list(os.scandir())

print(arquivos[1].name)
print(arquivos[1].inode())
print(arquivos[1].is_dir())
print(arquivos[1].is_file())
print(arquivos[1].path)
print(arquivos[1].stat())