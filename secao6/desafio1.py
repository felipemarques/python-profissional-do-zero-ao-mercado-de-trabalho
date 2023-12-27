n = "12345"

soma = 0
for d in n:
    soma = soma + int(d)

print("soma: ", soma)

######

n = int(input("n: "))
soma = 0
resta = 0

while n != 0:
    resta = n % 10
    soma = soma + resta
    n = int(n/10)

print('soma: ', soma)

    
