#else 이용하기
x=5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')
print('1--------------------')

#변수에 값 할당을 if, else로 축약하기
x=5
if x == 10:
    y=x
else:
    y=0

x=5
y=x if x == 10 else 0 #변수 = 값 if 조건문 else 값으로 축약할 수 있다.
print('2--------------------')

#if 조건문의 동작 방식 알아보기
if True:
    print('참')
else:
    print('거짓') #True는 참

if False:
    print('참')
else:
    print('거짓') #False는 거짓 

if None:
    print('참')
else:
    print('거짓') #None는 거짖
print('3--------------------')

#if 조건문에 숫자 지정하기
if 0:
    print('참')
else:
    print('거짓') #0은 거짓

if 1:
    print('참')
else:
    print('거짓') #1은 참

if 0x1F:
    print('참')
else:
    print('거짓') #0x1F는 참

if 0b1000:
    print('참')
else:
    print('거짓') #0b1000은 참

if 1.35:
    print('참')
else:
    print('거짓') #13.5는 참
print('4--------------------')

#if 조건문에 문자열 지정하기
if 'Hello':
    print('참')
else:
    print('거짓') #문자열은 참

if '':
    print('참')
else:
    print('거짓') #문자열은 거짓
""" 
파이썬 문법중에서 False로 취급하는것
-None -False -0인 숫자들:0, 0.0, 0kj -빈 문자열, 리스트, 튜플, 딕셔너리, 세트 -클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때
"""
print('5--------------------')

#조건 여려 개 지정하기
x=10
y=20
if x == 10 and y == 20:
    print('참')
else:
    print('거짓')
print('6--------------------')

#중첩 if 조건문과 논리 연산자
x=10
if x > 0:
    if x < 20:
        print('20보다 작은 양수 입니다.')

if x > 0 and x < 20:
    print('20보다 작은 양수 입니다.')

if 0 < x < 20:
    print('20보다 작은 양수 입니다.')
print('7--------------------')

#연습묹제
written_test=75
coding_test=True
if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')
print('8--------------------')

#심사문제
num=0
score=list(map(int,input().split()))
for i in score:
    if i > 100:
        print('잘못된 점수')
        break
    else:
        num=i+num
num=int(num/len(score))
if num >= 80:
    print('합격')
else:
    print('불합격')