def contador(max):
    cont = 1
    while cont <= max:
        yield cont
        cont += 1

gen = list(contador(10))
print(gen)

