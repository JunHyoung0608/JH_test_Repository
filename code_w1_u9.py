#문자열 사용하기
hello='Hello, world!'
print(hello)
hello='''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)
print('--------------------')

#문자열 안에 작은따옴표나 큰따옴표 포함하기
print("Python isn't difficult") #큰(작은) 따옴표로 묶면 작은(큰) 따옴표를 쓸 수 있다.
print('Python isn\'t difficult') #문자열 안에 따옴표 안에 \를 넣은 이스케이프를 활용한다.
print('--------------------')

#연습문제
s='''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)
print('--------------------')

#심사문제
s='''\'Python\' is a "programming language" 
that lets you work quickly
and
integrate systems more effectively.'''
print(s)