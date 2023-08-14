hours1 = 0
hours2 = 0
min1 = 0
min2 = 0
re_sel =1
re = True
re2 = True
sum_hour = 0
sum_min = 0
while(re):
    mode = 3
    print("시 분을 입력할땐 스페이스로 구분하여 입력해주십시오")
    startvalue = input("시작 시간을 시 분으로 적어주십시오... ")
    startvalue = startvalue.split(' ')
    hours1 = int(startvalue[0])
    min1 = int(startvalue[1])
    endvalue = input("종료 시간을 시 분으로 적어주십시오... ")
    endvalue = endvalue.split(' ')
    hours2 = int(endvalue[0])
    min2 = int(endvalue[1])
    calhour = hours2 - hours1
    calmin = min2 - min1
    sum_hour = calhour 
    sum_min = calmin
    if calmin < 0:
        calhour = calhour - 1
        calmin = 60 + calmin
        print(str(sum_hour)+":"+str(sum_min))
    else :
        print(str(sum_hour)+":"+str(sum_min)) #1:44 /
    re2 = True    
    while(re2):    
        if mode != 1 and mode != 0:
            re_sel = int(input("계속 할 생각이시면 1, 아닌 경우 0을 넣어주십시오. : "))      
        if re_sel == 1:
            re = True
            mode = int(input("계산 결과를 이어 연산 하시겠습니까? Y = 1 / N = 0 : "))
            if mode == 1 :
                sum_hour = calhour 
                sum_min = calmin
                re2 = False
            elif mode == 0 : 
                sum_hour = 0
                sum_min = 0
                re2 = False
        elif re_sel == 0 :   
            re = False
            re2 = False
        else:
            print("다시 입력하세요!")
            