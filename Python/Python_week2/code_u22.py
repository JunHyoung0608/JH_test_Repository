#리스트에 요소  추가하기
'''
append : 요소 하나를 추가
extend : 리스트를 연결하여 확장
insert : 특정 인덱스에 요소 추가
'''

#append 사용하기
a = [10, 20, 300]
a.append(500)
print(a)

a = []
a.append(10)
print(a)
print('1--------------------')

#리스트 안에 일스트 추가하기
a = [10 , 20, 30]
a.append([500, 600])
print(a)
print(len(a))
print('2--------------------')

#리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))
print('3--------------------')

#리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(0, 500)
print(a)

a= [10, 20, 30]
a.insert(len(a), 500)
print(a)

a=[10, 20, 30]
a.insert(1, [500, 600])
print(a)

a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)
print('4--------------------')

#리스트에서 요소삭제하기
'''
pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제
remove : 특정 값을 찾아서 삭제
'''

# 리스트에서 특정 인덱스의 요소를 삭제하기
a = [10, 20, 30]
print(a.pop())
print(a)
print('5--------------------')
#리스트로 스택과 큐 만들기
'''
스택 : 리스트를 그래로 활용하여 apppend(), pop()을 사용한다.
큐(리스트) : apppend(), pop(0)이거나 insert(0,요소), pop()을 사용해서 추가/삭제를 방향을 조절하여 큐를 만들 수 있다.
큐(덱) : 덱은 양쪽 끝에 추가/삭제가 가능한 자료 구조이다.
'''
from collections import deque
a = deque([10, 20, 30])
print(a)
a.append(500)
print(a)
a.popleft()
print(a)
print('6--------------------')

#리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) #같은 값이 여러 개일 경우 처음 찾은 인덱스를 구합니다.
print('7--------------------')

#특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
a.count(20)
print('8--------------------')

#리스트으 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)
print('9--------------------')

#리스트의 요소를 정렬하기
a = [10, 20, 30, 15, 20, 40]
a.sort() #매서드를 사용한 리스트 변경
print(a)
b = [10, 20, 30, 15, 20, 40] 
print(sorted(b)) #정렬된 새 리스트를 생성

#리스트의 모든 요소를 삭제하기
a = [10, 20, 30]
a.clear()
print(a)

a = [10, 20, 30]
del a[:]
print(a)
print('10--------------------')

#리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

a = [10, 20, 30]
a[len(a):] = [500, 600]
print(a)
print('11--------------------')

#리스트가 비어 있는지 확인하기
seq=[]
if not len(seq):
    print('True')

if not seq:
    print('True')

if seq:
    print(seq[-1]) #요소가 있을 떄만 마지막 요소를 가져옴
print('12--------------------')

#리스트의 할당과 복사 알아보기
a = [0, 0, 0, 0, 0]
b = a #b=a와 같이 리스트를 다른 변수에 할당하면 리스트는 두 개가 될 것 같지만 실제로는 리스트가 한 개이다.
print(a is b)
print(id(a))
print(id(b))

b[2] = 99
print(a)
print(b)

a = [0, 0, 0, 0, 0]
b = a.copy() #리스트a의 요소가 모두 b에 복사 된다. 할당과 다르게 복사는 다른 객체를 가진다.
print(a is b)
print(a == b)

b[2] = 99
print(a)
print(b)
print('13--------------------')

#for 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

for i in [38, 21, 53, 62, 19]:
    print(i)
print('14--------------------')

#인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a):
    print(index + 1, value)

for index, value in enumerate(a, start=1):
    print(index, value)

for index, value in enumerate(a,1):
    print(index, value)
print('15--------------------')

#반복문에서 인덱스 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])
print('16--------------------')

#while 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1
print('17--------------------')

#가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i

a = [38, 21, 53, 62, 19]
a.sort()
print(a[0])

a.sort(reverse=True)
print(a[0])

a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))
