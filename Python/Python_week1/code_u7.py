#값을 여러개 출력하기
print(1,2,3)
print('Hello','Python')
print('1--------------------')

#sep로 값 사이에 문자 넣기
print(1,2,3, sep=', ')
print(4,5,6, sep=',')
print('Hello','Python', sep='')
print(1920,1080, sep='X')
print('2--------------------')

#줄바꿈 활용하기
print(1,2,3, sep='\n')
print('1\t2\t3\t') #제어문자\n,\t,... -> 이스케이프 시퀀스:\뒤에 문자나 숫자의 조합을 부른다.
print('3--------------------')

#end 사용하기
print(1, end='')
print(2, end='')
print(3)
print('4--------------------')

#연습문제
year=2000
month=10
day=27
hour=11
minute=43
second=59

print(year,month,day, sep='/', end=' ')
print(hour,minute,second, sep=':')
print('5--------------------')

#심사문제
year,month,day,hour,minute,second=map(int,input().split())
print(year,month,day, sep='-', end='')
print('T', end='')
print(hour,minute,second, sep=':')