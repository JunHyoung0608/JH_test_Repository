class Person:
    '''사람 클래스입니다.'''

    def greeting(self):
        '''인사 매서드입니다.'''
        print('Hello')

print(Person.__doc__)
print(Person.greeting.__doc__)

maria = Person()
print(maria.greeting.__doc__)