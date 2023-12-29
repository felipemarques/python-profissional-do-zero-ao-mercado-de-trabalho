def fibonacci(final):
    f = []
    a, b = 0, 1
    while len(f) < final:
        f.append(b)
        a, b = b, a+b
    return f

def fibonacci_g(final):
    a, b, contador = 0, 1, 0
    while contador < final:
        a, b = b, a+b
        yield a
        contador += 1

for n in fibonacci(100):
    print(n, end=' ')

print(' ')

for n in fibonacci_g(100):
    print(n, end=' ')
