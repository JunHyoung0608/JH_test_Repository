#사칙연산
print('1+1=',1+1)
print('1-2=',1-2)
print('2*2=',2*2)
print('5/2=',5/2)
print('4/2=',4/2)
print('1--------------------')

# 나눗셈 후 소수점 이하를 버리는 //연산자
print('5//2=',5//2)
print('4//2=',4//2)
print('5.5//2=',5.5//2)
print('4//2.0=',4//2.0)
print('4.1//2.1=',4.1//2.1)
print('2--------------------')

#나눗셈 후 나머지를 구하는 %연산자
print('5%2=',5%2)
print('3--------------------')

#거듭제곱을 구하는 **연산자
print('2**10=',2**10)
print('4--------------------')

#값을 정수로 만들기
print('int(3.3) -> ',int(3.3))
print('int(5/2) -> ',int(5/2))
print("int('10') -> ",int('10'))
print('5--------------------')

#객체의 자료형 알아내기
print('type(10) -> ',type(10))
print('6--------------------')

#몫과 나머지르 함께 구하기
print('divmod(5,2) -> ',divmod(5,2))
quotient, remainder = divmod(5,2)
print(quotient,remainder)
print('7--------------------')

#2진수 8진수 16진수
print('0b110 -> ', 0b110) #0b를 붙이면 2진수로 읽는다.
print('0o10 -> ', 0o10) #0o을 붙이면 8진수로 읽는다.
print('0xF -> ',0xF) #0x을 붙이면 16진수로 읽는다.
print('8--------------------')

#실수 계산하기
print('3.5+2.1=',3.5+2.1)
print('4.2-2.7=',4.3-2.7) #(주의)결과값이 1.5999999999..가 나온다. 파이썬은 부동소수점을 근사값으로 계산하여 풀기 때문에 나타나는 현상이다.
print('1.5*3.1=',1.5*3.1)
print('5.5/3.1=',5.5/3.1)
print('9--------------------')

#실수와 정수를 함께 계산하면?
print('4.2+5=',4.2+5)
print('10--------------------')

#값을 실수로 만들기
print('float(5)',float(5)) #숫자
print('float(1+2)',float(1+2)) #계산식
print("float('5.3')",float('5.3')) #문자열
print('type(3.5) -> ',type(3.5)) #자료형
print('11--------------------')

#복소수
print(1.2+1.3j)
print('complex(1.2,1.3) -> ',complex(1.2,1.3))
print('12--------------------')

#괄호 사용하기
print('35+1*2=',35+1*2)
print('(35+1)*2=',(35+1)*2)
print('13--------------------')

#연습문제
print(int(0.2467*12+4.159))
print('14--------------------')

#심사문제
print(102*0.6+225)