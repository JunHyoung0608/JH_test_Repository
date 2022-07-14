lines = ['안녕하세요\n', '파이썬\n', '코딩 도장입니다.\n']

with open('Text/unit27/hello_list2.txt', 'w') as file:
    file.writelines(lines)