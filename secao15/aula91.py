class Automovel:
    def __init__(self, placa = 'XXX-000', velocidade_max = 100) -> None:
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):
        return f'{self.velocidade_atual} km/h'

    def get_placa(self):
        return self.placa
    
    def dirigir(self, velocidade):
        print(f'Estou digirindo a {velocidade} km/h')

    def acelerar(self):
        maxima = self.velocidade_max
        nova = self.velocidade_atual + 10
        self.velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        nova = self.velocidade_atual - 10
        self.velocidade_atual = nova if nova >= 0 else 0

carro = Automovel(placa='ABC-123', velocidade_max=180)

print(carro.get_placa())
carro.dirigir(100)
print(carro)

for _ in range(20):
    carro.acelerar()
    print('acelerando: ', carro)

for _ in range(20):
    carro.frear()
    print('freando: ',carro)