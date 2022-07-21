class Person:
    bag = [] #클래스의 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유한다.

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)