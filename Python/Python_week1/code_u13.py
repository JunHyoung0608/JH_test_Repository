#if조건문 시용하기
x=10
if x == 10:
    print('10입니다.')
print('1--------------------')

#if 조건문에서 코드를 생략하기
x=10
if x ==10:
    pass #아무일도 일어나지 않고 넘어간다는 의미
print('2--------------------')

#TODO
x=10
if x==10:
    pass #TODO:x가10일떄 해야할일
#####TODO는 헤야할일이라는 뜻으로 주석에 넣어 놓는다. 이런 방식으로 넣어 두면 검색으로 찾기 쉽다. 프로그래머들은 주석에 TODO 외 FIXME, BUG, NOTE 등 같이 코드는 아니지만 일관된 주석을 사용한다.
print('3--------------------')

#중첩 if 조건문 사용하기
x=15
if x >= 10:
    print('10 이상입니다.')
    if x == 15:
        print('15입니다.')
    if x == 20:
        print('20입니다.')
print('4--------------------')

#사용자가 입력한 값에 if 조건문 사용하기
x=int(input())

if x == 10:
    print('10입니다.')

if x == 20:
    print('20입니다.')
print('5--------------------')

#연습문제
x=5

if x != 10:
    print('ok')
print('6--------------------')

#심사문제
price=int(input())
coupon=input()
if coupon == 'Cash3000':
    print(price-3000)
if coupon == 'Cash5000':
    print(price-5000)