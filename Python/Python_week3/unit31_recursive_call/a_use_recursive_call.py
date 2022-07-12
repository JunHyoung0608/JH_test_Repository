def hello():
    print('Hello,world!')
    hello()

hello() #결과 : hello,world! x 804개
'''
RecursionError: maximum recursion depth exceeded in comparison
재귀 오류: 최대 재귀 깊이가 비교에서 초과되었습니다.
'''