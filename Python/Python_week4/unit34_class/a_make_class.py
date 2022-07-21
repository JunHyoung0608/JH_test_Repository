class Person:
    def __init__(self): #매서드
        self.hello = '안녕하세요.'

    def greeting(self): #매서드
        print(self.hello)


james = Person()
james.greeting()