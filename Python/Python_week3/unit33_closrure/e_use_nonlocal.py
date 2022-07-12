def A():
    x = 10 #A의 지역변수
    def B():
        nonlocal x
        x = 20 #B의 지역변수
    
    B()
    print(x) #A의 지역변수

A()