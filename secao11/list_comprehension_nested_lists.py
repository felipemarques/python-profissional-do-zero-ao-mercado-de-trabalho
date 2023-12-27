listas = [[1,2,3],[4,5,6],[7,8,9]]

# for lista in listas:
#     for num in lista:
#         print(num)

# print([[num for num in lista] for lista in listas])

[ [print(num) for num in lista] for lista in listas]