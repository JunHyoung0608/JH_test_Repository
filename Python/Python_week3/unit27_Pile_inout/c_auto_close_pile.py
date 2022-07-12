with open('Text/unit27/hello.txt','r') as file: #with as를 사용하면 파일 객체를 자동으로 닫아줌.
    s = file.read()
    print(s)