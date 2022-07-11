def personal_info(name, age, address='비공개'): #초기값이 지정된 매개뱐수 다음에는 초깃값이 없는 매개변수가 올 수 없다.
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)
personal_info('홍길동', 30, '서울시 용산구 이촌동')