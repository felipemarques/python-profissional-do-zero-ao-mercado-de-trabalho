
soma = 0
i = 0
for i in range(1, 6):
    idade = int(input("idade: " + str(i) +":"))
    soma = soma + idade
    i = i + 1

media = soma / 5
print("media: ", media)