class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점관리')

class Undergradute(Person, University):
    def study(self):
        print('공부하기')

james = Undergradute()
james.greeting()
james.manage_credit()
james.study()
