with open('Text/unit28/ex_quiz.txt', 'r', encoding='UTF-8') as file:
    list_str = file.readlines()

    for i in range(len(list_str)):
        list_str[i] = list_str[i].rstrip('\n')
    
    for word in list_str:
        if word  == word[::-1]:
            print(word)
            