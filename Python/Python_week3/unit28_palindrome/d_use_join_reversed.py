word = input('단어를 입력하세요: ')
print(''.join(reversed(word)))
print(word == ''.join(reversed(word))) #리스트의 요소들의 문자열를 잇는다.