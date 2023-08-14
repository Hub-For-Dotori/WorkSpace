def class_name_fee(name,fee):
    na = list(name)
    fe = list(fee)
    list_len = len(na)
i = 0
err_try_set = 3 #일정 횟수 틀릴 시 문구 출력을 위한 변수
my_class = {'영어회화':'30만원','영어작문':'25만원','일본어회화':'24만원','중국어회화':'25만원'}
i = int(input("입력 오류 허용 횟수를 지정해주세요 : "))
r = i
while i:
    class_name_fee(my_class.keys(), my_class.items())  # 딕셔너리 수강반, 수강료 인수 넘김
    name = input("수강 강의 입력하시오 : ")
    i = i if name in my_class.keys() else i - 1
    print("" if r == i else "{0}회만큼 틀렸습니다.\n".format(err_try_set) if i % err_try_set == 0 else "")
    print(f'입력 수강반 : {name} || 수강료 : {my_class.get(name, "입력한 수강반이 없습니다.")}\n입력가능한 횟수는 {i}번 남았습니다.\n')