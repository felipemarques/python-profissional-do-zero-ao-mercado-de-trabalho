# numeros = {1,2,3,4,5}
# print(numeros)

numeros = {num for num in range(1,7)}
print(numeros)

quadrado = {pow(num, 2) for num in numeros}
print(sorted(list(quadrado)))


frase = 'pyPro - seja um profissional Python'
letras = {letra for letra in frase}
print(letras)