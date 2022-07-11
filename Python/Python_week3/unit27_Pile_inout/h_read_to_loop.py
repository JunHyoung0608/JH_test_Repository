with open('hello.txt', 'r', encoding='UTF-8') as file: 
    for line in file: #for에 파일 객체를 지정하면 파일의 내용 한 줄씩 읽어서 변구에 저장함
        print(line.strip('\n'))