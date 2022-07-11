with open('Text/u27_ex_quiz2.txt', 'r', encoding='UTF-8') as file:
    string = file.readline()
    list_str = string.split(' ')
    for word in list_str:
        for letter in word:
            if letter == 'c':
                word=word.replace(',','')
                word=word.replace('.','')
                print(word)
                break
                