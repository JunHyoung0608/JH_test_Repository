def number_generator(): #제너레이터는 이터레이터를 생성해주는 함수
    yield 0 #yield를  사용하면 함수는 제너레이터가 된다.
    yield 1
    yield 2

for i in number_generator():
    print(i)