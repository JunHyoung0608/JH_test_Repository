def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:
        raise Exception('3의 배수가 아닙니다.') #raise : 따로 예외를 발생시킨다.
    print(x)



try:
    three_multiple()
except Exception as e:
    print('예와가 발생했습니다.', e)