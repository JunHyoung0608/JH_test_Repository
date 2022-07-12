'''
pickle 모듈 : 파이썬에서 객체를 파일에 저장하는 모듈
pickling : 객체를 저장하는 과정 // 메서드 : dump
unpickling : 파일에서 객체를 읽어 오는 과정 // 매서드 : load
'''
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean':90, 'english':95, 'mathmatics':85, 'science':82}

#pickling-save
with open('Text/unit27/james.txt', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

#pickling-load
with open('Text/unit27/james.txt', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
