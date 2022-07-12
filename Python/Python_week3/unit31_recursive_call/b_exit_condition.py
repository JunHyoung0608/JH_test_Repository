def hello(count):
    if count == 0: #종료 조건
        return
    
    print('Hello, world!', count)

    count -= 1
    hello(count)

hello(5)