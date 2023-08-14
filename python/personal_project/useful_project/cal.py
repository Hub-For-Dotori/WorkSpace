class cal:
    def plus(x, y):
        res = x + y
        return res

    def minus(x, y):
        res = x - y
        return res

    def divide(x, y):
        res = x / y
        return res

    def multiply(x, y):
        res = x * y
        return res


save_data = 0
re = 1

while re:
    if save_data == 0:
        cur_res = 0
        x = float(input("x값 입력 : "))
    else:
        x = cur_res
    symbol = input("연산 기호 입력 : ")
    y = float(input("y값 입력 : "))
    if symbol == "+":
        cur_res = cal.plus(x, y)
        print(cur_res)
    elif symbol == "-":
        cur_res = cal.minus(x, y)
        print(cur_res)
    elif symbol == "/":
        cur_res = cal.divide(x, y)
        print(cur_res)
    elif symbol == "*" or symbol == 'x':
        cur_res = cal.multiply(x, y)
        print(cur_res)
    else:
        print("계산 불능!!")
    re = int(input("프로그램을 종료하시겠습니까? (예:0 아니오:1): "))
    save_data = int(input("계산 값을 유지하여 계산합니까? (예:1 아니오:0): "))
