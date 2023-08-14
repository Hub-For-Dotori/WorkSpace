'''
숫자 여부를 알려주는 함수 is_number() 작성
1. 정수 포함한 실수 여부를 알려주는 함수 작성
2. try except 구문 활용 가능
3. 숫자면 True 아니면 False 반환
'''


def is_number(num):
    data = bool()
    b = num
    try:
        if float(num) == float(b):
            data = True
            pass
    except:
        data = False
    return data


num = input("숫자 판별기 입니다. 아무거나 입력하세요.. ")
print(is_number(num))
