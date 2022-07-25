import random

for i in iter(lambda : random.randint(0, 5), 2): #iter : 특정한 값이 나올때 반복을 끝냄
    print(i, end =' ')


'''
import random

while Ture:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')

'''