class Casa:
    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0 and isinstance(novo_preco, float):
            self.__preco = novo_preco
        else:
            print("Insira um valor válido!")

    @preco.deleter
    def preco(self):
        del self.__preco


minha_casa = Casa(450000)
print(minha_casa.preco)
minha_casa.preco = 500000.0
print(minha_casa.preco)
