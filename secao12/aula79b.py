from io import StringIO

try:

    frutas = ""
    arquivo = StringIO(frutas)

    while True:
        fruta = input('Digite uma fruta: ')
        if fruta == 'sair':
            break
        elif fruta == 'batata':
            raise Exception('batata não é fruta.')
        else:
            arquivo.write(fruta)
            arquivo.write("\n")

    arquivo.seek(0)

    with open('frutas.io.txt', 'a+') as arquivo_fisico:
        for fruta in arquivo.readlines():
            arquivo_fisico.write(fruta)
                
except Exception as e:
    print(f"Exception: {e}")