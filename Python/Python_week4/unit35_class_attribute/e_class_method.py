class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod #cls로 클래스 속성count에 접근할 수 있다.
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()