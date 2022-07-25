def file_read():
    with open('Python/Text/unit40/pr_quiz.txt', 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')


for i in file_read():
    print(i)