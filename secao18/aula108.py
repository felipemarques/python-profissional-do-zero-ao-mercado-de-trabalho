"""def dobro(x):
    return x * 2

print(dobro(4))

d = lambda x: x * 2
print(d(4))

print((lambda x, y, z: x + y + z)(1, 2, 3))"""

def cumprimento():
    titulo = 'Sr(a) '
    acao = (lambda x: titulo + x)
    return acao

cumprimentar = cumprimento()
print(cumprimentar('José'))


salario = lambda x: x - (x * 0.08)
print(salario(1000))