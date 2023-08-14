import chardet

dir = input("파일명이 포함 된 디렉토리 입력 : ")
with open("abcdef.txt", "r") as f:
    file_data = f.readline()
print(chardet.detect(file_data.encode()))
