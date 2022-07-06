#리스트 만들기
a=[83,32,32,53,23]
print(a)
a=['jun',23,608,True]
print(a)
print('1--------------------')

#range를 사용하여 리스트 만들기
a=list(range(10))
print(a)
a=list(range(3,14,2))
print(a)
print('2--------------------')

#튜플 사용하기
b=(83,32,32,53,23)
print(b)
b=83,32,32,53,23
b=('jun',23,608,True)
print(b)
x=(38)
print(x)
print(type(x))
x=(38,)
print(x)
print(type(x))
print('3--------------------')

#range를 사용하여 튜플 만들기
b=tuple(range(10))
print(b)
b=tuple(range(3,14,2))
print(b)
print('4--------------------')

#튜플을 리스트로, 리스트를 튜플로
a=[1,2,3]
a= tuple(a)
print(a)
b=(4,5,6)
b=list(b)
print(b)
print('5--------------------')

#문자열를 리스트, 튜플에 넣으면
a=list('Hello')
print(a)
b=tuple('Hello')
print(b)
print('6--------------------')

#리스트,튜플로 변수 만들기
a,b,c=[1,2,3]
print(a,b,c)
d,e,f=(4,5,6)
print(d,e,f) #리스트(튜플) 언패킹: 다음과 같이 리스트와 튜플의 요소를 여러 개에 할당하는 것
print('7--------------------')

#연습문제
a=list(range(5,-10,-2))
print(a)
print('8--------------------')

#심사문제
num=int(input())
a=list(range(-10,10,num))
print(a)