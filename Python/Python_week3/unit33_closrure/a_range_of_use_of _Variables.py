def foo():
    print(x) #전역변수 출력
x = 10 #전역변수

foo()
print(x) #전역변수 출력
print('------------------------')

'''
def foo1():
    x = 10
    print(x)

foo()
print(x)
'''
'''
결과
Exception has occurred: NameError
name 'x' is not defined

에러 foo의 지역변수는 출력할 수 없음
'''