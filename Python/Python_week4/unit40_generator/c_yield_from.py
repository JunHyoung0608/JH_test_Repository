def number_generator():
    x = [1, 2, 3]
    yield from x
    
for i in number_generator():
    print(i)