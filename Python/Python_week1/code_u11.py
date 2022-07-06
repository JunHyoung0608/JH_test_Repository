#시퀀스 자료형
a=[1,2,3,4,5]
b=(1,2,3,4,5)
c=range(1,6)
d=str(5)
e=bytes(10)
f=bytearray(10) 
print('1--------------------')

#bytes, bytearray
#####bytes는 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형이다. (1바이트는 8비트로 정의하며 0~255(0x00~0xFF)까지 정수를 사용한다.)
print(bytes(10)) #0이 10개들어있는 바이트 객체 생성
print([10,20,30,40,50]) #리스트로 바이트 개체 생성
print(b'hello') #바이트 객체로 바이트 객체 생성
#####bytearray는 bytes와 기능은 동일 하나, bytes는 요소를 변경 못 하지만 byearray는 가능하다.
x=bytearray(b'hello')
x[0]=ord('a') #bytearry의 요소에 값을 할당할 때는 정수 값을 할당해야 한다. 문자를 넣고 싶으면 아스키코드로 넣어준다.
print(x)
print('2--------------------')

#바이트 자료형과 인코딩
#####문자열의 기본 인코딩은 'UTF-8'인데 b'hello'와 같이 문자열을 바이트 객체로 만들면 각준자를 아스키코드로 저장한다.
print('hello'.encode()) #str -> bytes
#####한글 문자열을 EUC-KR 인코딩과 UTF-8 인코딩으로 된 바이트 객체로 만든다.
print('안녕'.encode('euc-kr')) 
print('안녕'.encode('utf-8'))
print(b'hello'.decode()) #bytes -> str
#####바이트 객체가 특정 인코딩으로 되어 있으면 decode에 인코딩을 지정해주면 된다.
x='안녕'.encode('euc-kr')
print(x.decode('euc-kr'))
x='안녕'.encode('utf-8')
print(x.decode('utf-8'))
#####바이트 자료형은 인코딩을 지정하여 객체를 생성할 수 있다
print(bytes('안녕',encoding='euc-kr'))
print(bytearray('안녕',encoding='cp949'))
print('3--------------------')

#특정한 값이 있는지 확인하기
a=[10,20,30,40,50,60,70,80,90]
print(30 in a)
print(100 in a)
print(100 not in a)
print('4--------------------')

#시퀀스 객체 연결하기
a=[0,10,20,30]
b=[9,8,7,6]
print(a+b) #range는 지원하지 않음. 리스트나 튜플로 변환하여 연결함.
print('5--------------------')

#스퀀스 객체의 반복
print([0,10,20,30]*3) #range는 지원하지 않음.
print('6--------------------')

#시퀀스 객체의 요소 개수 구하기
a=[10,20,30,40,50,60,70,80,90]
print(len(a))
b='Hello, world!'
print(len(b))
c='안녕하세요'
print(len(c))
print(len(c.encode('utf-8'))) #UTF-8 문자열의 바이트 수 구하기
print('7--------------------')

#인덱스 사용하기
a=[38,21,53,62,19]
print(a[3])
b=(38,21,53,62,19)
print(b[3])
c=range(10)
print(c[3])
print(c.__getitem__(3)) #시퀀스 객체에서 []를 사용하면 __getitem__메서드를 호출하여 요소를 가저오는 방식이다.
print(c[-1])
print(c[-10]) #인덱스 범위는 음수와 양수 범위가 정해저 있으면 범위를 넘길시 에러 발생
print('8--------------------')

#마지막 요소 접근하기
a=[38,21,53,62,19]
print(a[len(a)-1])
print('9--------------------')

#요소에 값 할당하기
a=[0,0,0,0,0]
a[0]=1
a[1]=2
a[2]=3
a[3]=4
a[4]=5
print(a) #range, tuple 객체는 값 할당 지원하지 않음
print('10--------------------')

#del로 요소 삭제하기
a=[38,21,53,62,19]
del a[2]
print(a) #range, tuple, str 객체는 삭제를 지원하지 않음
print('11--------------------')

#슬라이스 사용하기
a=[10,20,30,40,50,60,70,80,90]
print(a[0:4])
print(a[1:1])
print(a[1:2])
print(a[2:8:3])
print(a[:7])
print(a[7:])
print(a[::2])
print(a[::])
print(a[::-1])
print(a[:len(a)])
print('11--------------------')

#tulpe, rangen str에 스라이스 사용하기
b=(10,20,30,40,50,60,70,80,90)
print(b[4:7])
print(b[:7:2])
c=range(10)
print(c[4:7])
print(c[:7:2])
d='Hello, world!'
print(d[2:9])
print(d[:9:2])
print('12--------------------')

#slice 객체 사용하기
print(range(10)[slice(4,7,2)])
print(range(10).__getitem__(slice(4,7,2))) #시퀀스 객체의 [] 또는 __getitem__메서드에 slice 객체를 넣어주면 지정된 범위만큼 잘라내서 객체 만든다.
a=[10,20,30,40,50,60,70,80,90]
s=slice(4,7)
print(a[s])
b=range(10)
print(b[s])
c='Hello, world!'
print(c[s])
print('13--------------------')

#슬라이스 요소 할당하기
a=[10,20,30,40,50,60,70,80,90]
a[2:5]=['a','b','c']
print(a)
a=[10,20,30,40,50,60,70,80,90]
a[2:5]=['a']
print(a)
a=[10,20,30,40,50,60,70,80,90]
a[2:8:2]=['a','b','c']
print(a) #증가폭을 지정할 때는 슬라이스 범위의 요소와 할당할 요소 개수가 일치해야 함.
print('14--------------------')

#del로 슬라이스 삭제하기
a=[10,20,30,40,50,60,70,80,90]
del a[2:5]
print(a) #range, tuple, str은 del로 슬라이스를 삭제할 수 없다.
print('15--------------------')

#연습문제
year=[2011,2012,2013,2014,2015,2016,2017,2018]
population=[10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]

print(year[5:])
print(population[5:])
print('16--------------------')

#연습문제
n=-32,75,97,-10,9,32,4,-15,0,76,14,2

print(n[1::2])
print('17--------------------')

#심사문제
x=input().split()

del x[-5:]
x=tuple(x)
print(x)
print('18--------------------')

#심사문제
a=input()
b=input()

print(a[1::2],end=''); print(b[::2])