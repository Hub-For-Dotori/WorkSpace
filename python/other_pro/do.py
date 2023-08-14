'''
문제 1 
오늘의 운세 함수 수정하기 (40점)
아래의 미니프로그램 오늘의 운세 함수 myFotune()을 if()문을 사용하지 않고 
리스트 자료형을 사용하여 동일하게 동작하도록 myFortune2() 함수를 작성하세요.
myFortune2() 함수는 인수를 하나 이상 가질 수 있습니다.
오늘의 운세 문구를 현재의 9개에서 12개로 추가 한 후 
코드의 수정 없이 작동하도록 만들어보세요(가산점 10점)
'''

import random

num = int(random.randint(1, 12))

def myFortune2(num):
    i = ["오늘은 일이 잘 풀릴 것 입니다.",
        "오늘은 좋아하는 사람한테 연락이 올 것 입니다.",
        "오늘은 행복한 일이 가득 할 것입니다.",
        "오늘은 운이 좋지 않으니 위험이 있는 일을 삼가하십시오.",
        "오늘은 먹을 운이 없으니 미리 배를 채워두시기 바랍니다.",
        "오늘은 몸 상태가 좋지 않을 것이니, 무리한 움직임은 삼가하십시오.",
        "오늘은 돈이 들어올 것 입니다.",
        "오늘은 최고의 운이 들어옵니다. 원하는 걸 자유롭게 해보시길 바랍니다.",
        "오늘은 머리가 잘 돌아가는 날입니다. 공부를 하셔야 한다면 오늘 집중해서 공부하세요.",
        "오늘은 대인운이 좋지 않습니다. 가능한 지인들이나, 새로 만나는 사람이 있다면, 신중하게 다가가세요.",
        "오늘은 몸 컨디션이 좋을테니, 밖에 나가서 활동적으로 보내세요.",
        "오늘은 운이 좋을 것 입니다."]
    num = num - 1
    print(i[num])

myFortune2(num)

'''
문제 2. 
딕셔너리를 이용한 학원 수강료 안내 프로그램 작성 (60점)
A 외국어학원은 영어회화, 영어작문, 일본어회화, 중국어회화의 4개 반을 
운영하고 있다. 각 반의 수강료는 30만원, 25만원, 24만원, 25만원이다. 
수강을 원하는 반의 이름을 입력하면 수강료를 알려주는 코드를 작성하라. 
위의 4개 반 이외의 이름을 입력하면 “입력한 수강반이 없습니다”라는 
문구를 출력하여 해당 반이 없음을 사용자에게 알려주어야 한다.
수강반과 수강료를 저장할 my_class 딕셔너리를 만드세요.
과목별 수강료를 알아내기 위해 if() 함수를 사용하면 안됩니다.
수강반 이름이 있는지 in 함수와 keys() 매서드를 사용하세요.
수강료를 가져오기위해 get()매서드를 사용하세요.
print 함수에 f 포매팅을 사용해보세요.
'''

i = 0
err_try_set = 3 #일정 횟수 틀릴 시 문구 출력을 위한 변수
my_class = {'영어회화':'30만원','영어작문':'25만원','일본어회화':'24만원','중국어회화':'25만원'}

na = list(my_class.keys())
fe = list(my_class.items())
list_len = len(na)

name = input("수강 강의 입력하시오 : ")
print(f'수강반 : {name} 수강료 : {my_class.get(name)}' if name in my_class.keys() else "입력한 수강반이 없습니다.")

'''
문제 2 개선(가산점 20점)
일정 횟수 이상 수강반 이름 입력을 틀릴 경우 적절한 메시지를 출력하고 
수강료 안내프로그램을 종료하도록 코드를 수정하세요. 
입력 오류 허용 횟수는 실행시에 임의로 정해 줄 수 있어야 합니다(10점).
참고) 수강료 안내 프로그램을 함수로 작성 후 인수로 수강반과 수강료 
딕셔너리를 인수로 넘기는 형태로 코드를 작성할 수 있습니다(10점).

print(f'{my_class[x]}만원')
print(f'{my_class.get(x,"입력한 수강반이 없습니다.")}만원')
'''
def class_name_fee(name,fee):
    na = list(name)
    fe = list(fee)
    list_len = len(na)
    for z in range(0,list_len):
        print("수강반 : {0} 수강료 : {1}".format(na[z],fe[z]))
i = 0
err_try_set = 3 #일정 횟수 틀릴 시 문구 출력을 위한 변수
my_class = {'영어회화':'30만원','영어작문':'25만원','일본어회화':'24만원','중국어회화':'25만원'}
i = int(input("입력 오류 허용 횟수를 지정해주세요 : "))
r = i
while i:
    class_name_fee(my_class.keys(), my_class.items())  # 딕셔너리 수강반, 수강료 인수 넘김
    name = input("수강 강의 입력하시오 : ")
    i = i if name in my_class.keys() else i - 1
    print(" " if r == i else "{0}회만큼 틀렸습니다.\n".format(err_try_set) if i % err_try_set == 0 else " ")
    print(f'{my_class.get(name, "입력한 수강반이 없습니다.")}', "입력가능한 횟수는 {0}번 남았습니다.".format(i))
