#중첩 루프 사용하기
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')
print('1--------------------')

#사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
print('2--------------------')

#사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()
print('3--------------------')

#계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()
print('4--------------------')

#대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
    print()
print('5--------------------')

#연습문제
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
print('6--------------------')

#심사문제
num = int(input())
bottom = num+num-1
mid = int((bottom)/2)
for i in range(num):
    for j in range(bottom):
        if j < mid - i or j > mid + i:
            print(end=' 3')
        else :
            print('*', end='')
    print()