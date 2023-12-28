try:

    with open('frutas.txt', 'a+') as arquivo:
        while True:
            fruta = input('Digite uma fruta: ')
            if fruta == 'sair':
                break
            elif fruta == 'batata':
                raise Exception('batata não é fruta.')
            else:
                arquivo.write(fruta)
                arquivo.write("\n")
                
except Exception as e:
    print(f"Exception: {e}")