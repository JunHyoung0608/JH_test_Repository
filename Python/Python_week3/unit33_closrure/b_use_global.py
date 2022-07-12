def foo():
    global x
    x = 20
    print(x)
x=10

foo()
print(x) #전역변수x가 10에서 foo의 전역변수 x에 의해 다시 정의되었음.
print('------------------------')

y = 1
def A():
    y = 10
    def B():
        y = 20
        def C():
            global y
            y = y + 30
            print(y)
        C()
    B()
A()
