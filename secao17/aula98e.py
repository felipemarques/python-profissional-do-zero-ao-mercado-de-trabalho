class Livro:
    def __init__(self, titulo, autor, editora, ano, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} - {self.autor}'

    def __str__(self):
        return f'{self.titulo}'

    def __len__(self):
        return self.paginas

    def __add__(self, other):
        return self.paginas + other.paginas

    def __del__(self):
        print("Um objeto da classe LIVRO foi deletado!")


livro1 = Livro(
    'Algoritmos e Programação de Computadores',
    'Piva Jr, et al',
    'Elsevier',
    2019,
    508
)

livro2 = Livro(
    'Estrutura de Dados e Técnicas de Programação',
    'Piva Jr, et al',
    'Elsevier',
    2014,
    399
)

print(livro1)
print(livro2)
print(len(livro1))
print(livro1 + livro2)
