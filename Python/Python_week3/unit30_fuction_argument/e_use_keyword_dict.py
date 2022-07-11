def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info(**{'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}) 