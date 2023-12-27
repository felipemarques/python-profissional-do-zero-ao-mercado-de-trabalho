idades = []

while True:
    idade = int(input("Idade: "))
    if (idade == -1):
        break

    idades.append(idade)

idadesT = tuple(idades)
totalIdades = len(idadesT)
print("Quantidade de idades: ", totalIdades)
print("Média das idades: ", (sum(idadesT) / totalIdades))