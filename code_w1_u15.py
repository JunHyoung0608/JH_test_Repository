#elif 사용하기
x=20
if x==10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

x=30
if x==10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')
print('1--------------------')

#음료수 자판기 만들기
button=int(input())
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')
print('2--------------------')

#연습문제
x=int(input())

if 10 < x <= 20:
    print('11~20')
elif 20 < x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')
print('3--------------------')

#심사문제
age=int(input())
cash=9000
if 7 <= age <= 12:
    print(cash-650)
elif 13 <= age <= 18:
    print(cash-1050)
elif 19 <= age:
    print(cash-1250)