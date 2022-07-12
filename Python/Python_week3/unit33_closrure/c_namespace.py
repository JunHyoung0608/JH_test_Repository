'''
파이썬에서 변수는 네임스페이스(namespcae, 이름공간)에 저장된다.
'''
def foo():
    x=10
    print(locals())

foo()