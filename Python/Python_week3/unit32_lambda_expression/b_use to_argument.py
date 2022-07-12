def plus_ten(x):
    return x + 10
print(list(map(plus_ten, [1, 2, 3])))
print('------------------------')

print(list(map(lambda x: x + 10, [1, 2, 3])))