#N-gram : 문자열에서 N개의 연속된 요소르 추출하는 방법
text = 'Hello'

for i in range(len(text)-1):
    print(text[i],text[i+1],sep='')