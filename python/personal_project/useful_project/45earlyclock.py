hours1 = 0
min1 = 0

#print("45분전에 알람을 맞춰주는 프로그램 입니다. 시와 분을 틀릴 시 둘다 다시 입력해야 합니다.")
value = input()
value = value.split(' ')
hours1 = int(value[0])
min1 = int(value[1])
min1 = min1 - 45
if min1 < 0:
    hours1 = hours1 - 1
    min1 = 60 + min1        #print("알람 설정 시간 ",hours1,":",min1)
    print(str(hours1)+" "+str(min1))
    if hours1 < 0:
        hours1 = 23
else :
    print(str(hours1)+" "+str(min1))