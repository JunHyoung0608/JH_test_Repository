class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    
    def __iter__(self): #현재 인스턴스를 반환
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end=' ')