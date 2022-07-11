def personal_info(**kwargs):
    for kw, agr in kwargs.items():
        print(kw, ': ', agr, sep='')

x={'name':'홍길동'}
personal_info(**x)
y={'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**y)