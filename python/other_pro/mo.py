txt_data = list()
txt_data = """김 수학 kim@gmail.com
건 영문 kun@gmail.com
권 컴퓨터공 kwon@gmail.com
서 경영 kim@gmail.com
황 게임 kim@gmail.com
박 법학 kim@gmail.com
차 기계공학 kim@gmail.com
여기에는 아무거나 써도 됌
"""

print(txt_data)

f = open("C:/Users/Kor_SW_Developer/Desktop/꿀팁/test/re.txt",  # 앞에 있는 건 파일 위치 주소로 변경해야함.물론 파일도 미리 만들어야 함.
         'a', -1, 'utf-8', 'w')

for i in range(0, len(txt_data)):  # 요거는 쓰기 위해서 한줄 한줄 작성하는 반복문
    txt_data1 = str(txt_data[i])
    f.write(txt_data1)

for i in range(0, len(txt_data)):
    print(txt_data[i])
    data = list()
    x1 = txt_data[i].split('\n')
    data.append(x1)
    print(data[i])
