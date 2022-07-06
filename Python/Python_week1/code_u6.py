#변수만들기
from asyncio.proactor_events import _ProactorDuplexPipeTransport
from re import I


x=10
print(x)
print('1--------------------')

#변수 자료형 알아내기
type(x)
print('2--------------------')

#변수 여러개를 한번에 만들기
x,y,z=10,20,30
print(x,y,z)
x=y=z=10
print(x,y,z)
print('4--------------------')

#변수삭제
i=None #빈 변수
del i #print(i) -> NameError: name 'i' is not defined
print('5--------------------')

#변수로 계산하기
a=10; b=20
print('a+b=',a+b)
print('a+10=',a+10)
a+=20
print('a+=20 ->',a)
print('+a ->',+a)
print('-a ->',-a)
print('6--------------------')

#input함수 사용하기
i=input('숫자입력 :')
print('입력의 자료형:',type(i))
i=int(i)
print('int(i) -> ',type(i))
i,k=map(int,input('숫자 두개를 더 합니다. 더할 숫자를 입력하세요. ex)입력 : n1 n2 \n입력 :').split())
print(i+k)
print('7--------------------')

#연습문제
a,b,c=map(int,input().split())
print(a+b+c)
print('8--------------------')

#심사문제1
a,b,c=50,100,None
print(a)
print(b)
print(c)
print('9--------------------')

#심사문제2
a,b,c,d=map(int,input().split())
average=int((a+b+c+d)/4)
print(average)