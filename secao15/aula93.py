class Automovel:

    contador = 0
    precisao = 0.95

    def __init__(self, placa = 'XXX-000', velocidade_max = 100) -> None:
        self.__id = Automovel.contador + 1
        self.__placa = placa
        self.__velocidade_max = velocidade_max * Automovel.precisao
        self.__velocidade_atual = 0
        Automovel.contador = self.__id

    def __str__(self):
        return f'{self.__velocidade_atual} km/h'

    def get_placa(self):
        return self.__placa
    
    def get_velocidade_max(self):
        return self.__velocidade_max
    
    def set_velocidade_max(self, nova):
        self.__velocidade_max = nova
        print(f'A nova velocidade máxima é: {nova} km/h')
    
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

carro.set_velocidade_max(200)

print(carro)
print(carro.get_velocidade_max())
print(carro.get_placa())