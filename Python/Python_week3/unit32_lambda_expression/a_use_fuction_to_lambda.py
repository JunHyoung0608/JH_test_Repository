def plus_ten(x):
    return x + 10
print(plus_ten(1))
print('-----------------------')

plus_ten2 = lambda x : x + 10 #매개변수 x를 입력 받아 x + 10을 거쳐 반환한다.
print(plus_ten2(1))
print('-----------------------')

print((lambda x : x + 10)(1))

#주의 : 람다 표현식에 새변수를 만들 수 없다.