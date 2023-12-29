from time import time

t_inicio = time()
g = sum((num for num in range(1, 1000000000)))
t_final = time()
tempo_gen = t_final - t_inicio

t_inicio = time()
l = sum([num for num in range(1, 1000000000)])
t_final = time()
tempo_lis = t_final - t_inicio

print(f'Tempo com generator: {tempo_gen}')
print(f'Tempo com lista....: {tempo_lis}')