with open('Text/unit27/pr_quiz1.txt', 'r', encoding='UTF-8') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word) <= 11:
            count += 1
    print(count)