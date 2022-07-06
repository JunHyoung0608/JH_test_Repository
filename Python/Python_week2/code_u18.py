#break로 반복문 끝내기
from itertools import count


i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break

for i in range(10000):
    print(i)
    if i == 100:
        break
print('1--------------------')

#continue로 코드 실행 건너뛰기
for i in range(100):
    if i % 2 == 0:
        continue #continue를 실행하면 countinue 아래 코드는 실행하지 않고 건너뛴 다음 반복을 시행한다.
    print(i)

i=0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print('2--------------------')

#반복문과 pass
#for, while의 반복할 코드에서 아무 일도 하지 않지만, 반복문의 형태를 유지하고 싶다면 pass를 사용하면 된다.
'''
for i in range(10):
    pass

while True:
    pass
'''
print('3--------------------')

#입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))
i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break
print('4--------------------')

#입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요: '))
for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)
print('5--------------------')

#연습문제
i=0
while True:
    if i % 10 != 3:
            i += 1
            continue
    if i > 73:
        break
    print(i, end =' ')
    i += 1
print('\n')
print('6--------------------')

#심사문제
start, stop = map(int,input().split())
i = start
while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end =' ')
    i += 1