with open('Text/unit27/hello_list1.txt', 'r', encoding='UTF-8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))