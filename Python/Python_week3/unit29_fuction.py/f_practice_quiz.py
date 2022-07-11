def get_quotient_remainder(x, y):
    quitient = int(x / y)
    remainder = x % y
    return quitient, remainder 
x = 10
y = 3

quitient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quitient, remainder ))
