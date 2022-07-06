#for와 range 사용하기
for i in range(100):
    print('Hello, world!', i)
print('1--------------------')

#for와 range 응용하기
for i in range(5,12):
    print('Hello, world', i)

for i in range(0,10,2):
    print('Hello, world!', i)

for i in range(10, 0, -1):
    print('Hello, world!', i)

for i in reversed(range(10)):
    print('Hello, world!', i) #reversed()는 숫자의 순서를 뒤집을 수 있다.
print('2--------------------')

#반복문의 변수 i를 변경할 수 있을까?
for i in range(10):
    print(i, end=' ')
    i=10 #변수 i는 반복할 때마다 다음 값으로 덮어써지기 떄문에 값을 할당해도 변수에 영향을 주지 못 한다.
print('\n')
print('3--------------------')

#입력한 횟수대로 반복하기
count=int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print('Hello, world!', i)
print('4--------------------')

#시퀀스 객체로 반복하기
a=[10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits=('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end='')
print('\n')

for letter in reversed('Python'):
    print(letter, end=' ')
print('\n')
print('5--------------------')

#연습문제
x=[49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')
print('\n')
print('6--------------------')

#심사문제
num=int(input())
for i in range(1,10):
    print('%d * %d = %d' %(num, i, num*i))
