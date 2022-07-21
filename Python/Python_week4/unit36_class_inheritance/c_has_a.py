class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonLsit:
    def __init__(self):
        self.person_list = []

    def appenf_person(self, person):
        self.person_list.append(person)