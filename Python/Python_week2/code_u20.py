#1부터 100까지 숫자 출력하기
for i in range(1, 101):
    print(i)
print('1--------------------')

#3의 배수일 때와 5의 배수일 때 처리하기
for i in range(1,101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('2--------------------')

#3과 5의 공배수 처리하기
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('3--------------------')

#논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
for i in range(1,10):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('4--------------------')

#코드 단축하기
for i in range(1,101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i) #'Fizz' * True -> 'Fizz' // 'Fizz' * False -> '' // '' or i -> i
print('5--------------------')

#연습문제
for i in range(1,101):
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)
print('6--------------------')

#심사문제
start, stop = map(int, input().split())
for i in range(start, stop+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
