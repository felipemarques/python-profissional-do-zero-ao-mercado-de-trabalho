import datetime

hoje = datetime.datetime.now()
natal = datetime.datetime(2024,12,25,0)

espera = natal - hoje

print(type(espera))
print(repr(espera))
print(espera)
print(f"Faltam {espera.days} dias para o próximo Natal")