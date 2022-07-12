def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello) #바깥쪽 함수의 지역변수를 사용
    print_message()

print_hello()