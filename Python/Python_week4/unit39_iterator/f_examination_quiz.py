class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __getitem__(self, index):
        hour = (self.start + index) // 60 // 60 % 24
        min = (self.start + index) // 60 % 60
        sec = (self.start + index) % 60
        if index < self.stop - self.start:
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour, min, sec)
        else:
            raise IndexError

start, stop, index = map(int, input().split())

for i in TimeIterator(start,stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')