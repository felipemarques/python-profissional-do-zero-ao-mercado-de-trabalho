class Automovel:
    def __init__(self, placa = 'XXX-000') -> None:
        self.placa = placa

    def get_placa(self):
        return self.placa
    
    def dirigir(self, velocidade):
        print(f'Estou digirindo a {velocidade} km/h')

carro = Automovel(placa='ABC-123')

print(carro.get_placa())
carro.dirigir(100)
