class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)
    
Calc.add(10, 20) #정적 메서드 : 인스턴스에서의 호출이 아닌 클래스에서 바로 호출 할 수 있다.
Calc.mul(10, 20)