try:
    file = open('mraia.txt', 'r')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close