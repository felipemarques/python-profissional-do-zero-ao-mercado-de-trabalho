numbers = [i for i in range(1,13)]

# with list comprehension
nova = [i * 2 for i in numbers]
print(nova)

# without list comprehension
# nova = []
# for i in range(len(numbers)):
#     nova.append(numbers[i] * 2)
# print(nova)