#터틀 그래픽스로 그림 그리기
import turtle as t

#사각형 그리기
t.shape("turtle")

t.forward(100)
t.right(90)
t.forward(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100) #forward == fd // right == rt
t.clear() #화면을 지운다.

#다각형 그리기
for i in range(4): #사각형
    t.forward(100)
    t.right(90)
t.clear()

for i in range(5): #오각형
    t.forward(100)
    t.right(360/5)
t.clear()

n = int(input())
for i in range(n): #n각형
    t.forward(100)
    t.right(360/n)
t.clear()

#다각형 색칠하기
n = 6
t.color('red') #펜의 색을 빨간색으로 설정
t.begin_fill() #색칠할 영역 시작
for i in range(6): #n의 반복
    t.forward(100)
    t.right(360/n)
t.end_fill() #색칠할 영역 끝
t.clear()

#color에 색깔 지정하기
'''
color의 색깔을 지정할 때, 영어로 색이름을 지정한다.
더 다향한 색상을 표현 할려면, 윕 색상을 사용하면 된다.
웹 색상은 #RRGGBB형식 이며, 각 RR, GG, BB는 RGB를 의미한다.
해당 자리에 두자리 16진수를 입력하면 된다.
'''
t.color('#000000')

#원 그리기
t.circle(120)
t.clear()

#원을 반복해서 그리기
n=60
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n)
t.clear()

# 선으로 복잡한 무늬 그리기
for i in range(300):
    t.forward(i)
    t.right(91)
t.reset() #화면과 터틀을 초기화한다.
#터틀 모양 설정하기
'''
터틀의 shape에는 arrow, circle, square, triangle, classic등 
여러 가지 터틀 모양을 설정할 수 있다.
'''

#연습문제
t.speed(3)
n=5
for i in range(n):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)
t.clear()

#심사문제
n, line = map(int, input().split())
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)