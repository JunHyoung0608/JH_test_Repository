class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet #변수 앞에 __를 붙여서 비공개 속성으로 만듦 ex) maria.wallet=-10000같이 밖에서 클래스의 비공개 속성을 직접적으로 접근시 애러 발생

    def pay(self, amount): #함수로 우회해서 비공개 속성의 변화를 줄 수 있다.
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)