class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() #super로 기반 클래스의 메서드를 호출한다.
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)