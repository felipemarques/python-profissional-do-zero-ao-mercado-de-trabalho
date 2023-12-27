nums = [i for i in range(1,13)]

# nova = [x * 2 for x in nums if x < 10]
# print(nova)

nova = [int(x/2) for x in nums if not(x%2)]
print(nova)