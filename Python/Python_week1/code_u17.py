import random

#while 반복문 사용하기
i=1
while i < 100:
    print('Hello, world!', i)
    i += 1

i=100
while i > 0:
    print('hello, world!', i)
    i -= 1
print('1--------------------')

#입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))
i = 0
while i < count:
    print('Hello, world!', i)
    i += 1

count = int(input('반복할 횟수를 입력하세요: '))
while count > 0:
    print('Hello, world!', count)
    count -= 1
print('2--------------------')

#반복 횟수를 지정하지 않을 경우
i=0
while i != 3:
    i = random.randint(1,6)
    print(i)
print('3--------------------')

#random.choice(시퀀스 객체)
dice=[1, 2, 3, 4, 5, 6]
for i in range(5):
    print(random.choice(dice)) #리스트에서 요소를 무작위로 선택
print('4--------------------')

#while 반복문으로 무한 루프 만들기
'''
while True:
    print('hello, world!') 
''' #while에 True를 지정하면 무한 루프
print('5--------------------')

#연습문제
i = 2
j = 5
while i <= 32 or j >= i:
    print(i, j)
    i *= 2
    j -= 1
print('6--------------------')

#심사문제
money = int(input())
money -= 1350
while money >= 0:
    print(money)
    money -= 1350