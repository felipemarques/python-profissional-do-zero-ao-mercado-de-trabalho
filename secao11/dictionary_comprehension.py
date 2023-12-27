dicio = {'a': 1, 'b': 2, 'c': 3, 'd': int('4')}

quadrado = {chave: pow(valor, 2) for chave, valor in dicio.items() if not(valor % 2)}

print(quadrado)