pessoas = []

class Pessoa:
    def __init__(self, data) -> None:
        self.nome = data["nome"]
        self.idade = data["idade"]
        self.calcado = data["calcado"]

while True:
    nome = input('Nome: ')

    if nome == "-1":
        break

    idade = int(input('Idade: '))
    calcado = int(input('N. do calçado: '))

    pessoas.append(
        Pessoa({
            "nome": nome,
            "idade": idade,
            "calcado": calcado
        })
    )

print("=====================")
print("Relação das pessoas")
print("=====================")

total_idades = 0
total_calcados = 0

for pessoa in pessoas:
    total_idades += pessoa.idade
    total_calcados += pessoa.calcado
    print(
        "Pessoa: ", pessoa.nome, 
        " Idade: ", pessoa.idade, 
        " Calçado: ", pessoa.calcado
    )
    print("===========")

total_pessoas = len(pessoas)
mediaIdade = int(total_idades / total_pessoas)
numeroMedioCalcado = int(total_calcados / total_pessoas)

print("Media de idade: ", mediaIdade)
print("Numero medio de calçado: ", numeroMedioCalcado)