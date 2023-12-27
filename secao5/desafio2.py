altura = float(input('Altura: '))
sexo = input('Sexo: ')

if (sexo == 'm'):
    pesoIdeal = (72.7 * altura) - 58
else:
    pesoIdeal = (62.1 * altura) - 44.7

print('Altura: ', altura)
print('Sexo: ', sexo)
print("Peso Ideal: ", pesoIdeal)