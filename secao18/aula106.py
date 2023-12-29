def dobro(x):
    return x * 2

def quadrado(x):
    return x * x

def calcular(operacao, lista, funcao):
    print(f'Calculando: {operacao}')
    for x in lista:
        print(x, '->', funcao(x))

calcular('dobro', [2,4], dobro)