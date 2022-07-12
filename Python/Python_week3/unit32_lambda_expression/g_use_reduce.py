'''
from functools import reduce
reduce(함수, 반복가능한객체)
반복 가능한 객체의 각 요소를 지정된 하무로 처리한 뒤 이전 결과와 누적하는 함수
'''

from functools import reduce

def f(x, y):
    print(x,y)
    return x + y

a = [1, 2, 3, 4, 5]
print(reduce(f, a))
print('------------------------')

print(reduce(lambda x, y : x + y, a))