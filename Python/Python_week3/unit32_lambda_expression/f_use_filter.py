'''
filter(함수, 반복가능한객체)
반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데 지정된 함수의 반환값이 True일 때만 해당 요소를 가져옴
'''

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f,a)))
print('------------------------')

print(list(filter(lambda x : x > 5 and x < 10, a)))