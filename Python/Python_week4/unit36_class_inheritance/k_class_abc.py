from abc import * #추상 메서드 : 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해서 사용

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    
    def go_to_school(self):
        print('학교가기')

james = Student()
james.study()
james.go_to_school()