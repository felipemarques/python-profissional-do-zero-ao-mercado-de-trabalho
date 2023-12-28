class Automovel:

    def __init__(self, placa = 'XXX-000', velocidade_max = 100) -> None:
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def __str__(self):
        return f'{self.__velocidade_atual} km/h'

    def get_placa(self):
        return self.__placa
    
    def dirigir(self, velocidade):
        print(f'Estou digirindo a {velocidade} km/h')

    def acelerar(self):
        maxima = self.__velocidade_max
        nova = self.__velocidade_atual + 10
        self.__velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        nova = self.__velocidade_atual - 10
        self.__velocidade_atual = nova if nova >= 0 else 0

carro = Automovel(placa='ABC-123', velocidade_max=180)

# violacao do principio de encapsulamento
carro.__placa = 'XXX0000'
carro.__velocidade_max = 1000
carro.__velocidade_atual = 200

print(carro)
print(carro.__velocidade_max)
print(carro.get_placa())