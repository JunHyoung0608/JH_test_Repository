#불과 비교 연산자 사용하기
print(True)
print(False)
print('--------------------')

#연산자의 판단결과
print(3>1)
print(10==10)
print(10 != 5)
print('Python'=='Python')
print('Python'=='python')
print('Python'!='python')
print(10>20)
print(10>=10)
print('--------------------')

#객체 비교하기
print(1==1.0)
print(1 is 1.0)
print(1 is not 1.0)
print('--------------------')

#정수 객체와 실수 객체가 서로 다른 것은 어떨게 확인하나요?
print(id(1))
print(id(1.0))
print(id(1)==id(1.0))#id(): 객체의 메모리 주소를 구한다.(파이썬을 실행하는 동안 고유 값을 유지하며 재실행 시 달라진다.)
print('--------------------')

#값 비교에 is를 쓰지 않기
a=-5
print(a is -5)
print(id(a),id(-5))
a=-6
print(a is -6)
print(id(a),id(-6)) 
#교재 내용) 변수a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 떄문이다. 따라서 다른 객체가 되므로 값이 같더라도 is로 비교하면 False가 나온다.
print('--------------------')

#논리 연산자 사용하기
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
print(not False)
print(not False and False or not False)
print(10 == 10 and 10 != 5)
print(10 > 5 or 10 < 3)
print(not 10 > 5)
print(not 1 is 1.0)
print('--------------------')

#bool() 사용
print(bool(1))
print(bool(0.0))
print(bool('False'))
print('--------------------')

#연습문제
korean=92
english=47
mathmatics=86
science=81

print(korean >= 50 and english >= 50 and mathmatics >= 50 and science >= 50)
print('--------------------')

#심사문제
korean,english,mathmatics,science=map(int,input().split())
print(korean >= 90 and english > 80 and mathmatics > 85 and science >= 80)