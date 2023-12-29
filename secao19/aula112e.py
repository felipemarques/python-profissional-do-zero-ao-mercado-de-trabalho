lista = [
    {'nome': 'José', 'idade': 28},
    {'nome': 'Adriana', 'idade': 39},
    {'nome': 'Pedro', 'idade': 50},
    {'nome': 'Maria', 'idade': 23},
]

so_nomes = map(lambda p: p['nome'], lista)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista)
print(f'A somatoria das idades é {sum(so_idades)}')