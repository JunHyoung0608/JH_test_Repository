class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입나다.')

james = Student()
james.greeting()

#overriding을 무시하다, 우선하다 : 기반클래스의 메서드를 무시하고 새로운 매서드를 만든다.