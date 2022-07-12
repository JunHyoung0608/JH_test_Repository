lines = ['안녕하세요\n', '파이썬\n', '코딩 도장입니다.\n']

with open('Text/unit27/hello_list1.txt', 'w', encoding='UTF-8') as file:
    file.writelines(lines)