class Mamifero:
    def __init__(self, pelo, mamas, idade) -> None:
        self.__pelo = pelo
        self.__mamas = mamas
        self.__idade = idade

    def comunicar(self):
        pass


class Chachorro(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo) -> None:
        super().__init__(pelo, mamas, idade)
        self.__rabo = rabo

    def latir(self):
        pass

class Gato(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo) -> None:
        super().__init__(pelo, mamas, idade)
        self.__rabo = rabo

    def miar(self):
        pass


gato = Gato()
