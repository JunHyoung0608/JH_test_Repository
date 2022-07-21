try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else: #try문에서 에러가 나지않으면 실행
    print(y)
finally: #예외 발생 여부와 상관없이 항상 실행
    print('코드 실행이 끝났습니다.')