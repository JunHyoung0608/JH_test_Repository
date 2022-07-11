with open('Text/hello_3line.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))