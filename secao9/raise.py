def fruta(n):
    lista = ['abacaxi','pera','banana','abacate']

    if (n > 3):
        raise IndexError("O valor excede o numero de elementos da lista")
    else:
        return lista[n]
    

print(fruta(3))
    
