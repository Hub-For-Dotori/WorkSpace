def match():
    # 초기설정 수행
    u_choice, c_choice = 0, 0
    match_score = 0
    choice_dic = {1: "가위", 2: "바위", 3: "보"}
    result_dic = {0: "결과는 무승부입니다.",
                  1: "결과는 사용자의 승리입니다.", -1: "결과는 컴퓨터의 승리입니다."}

    # 사용자 선택 가져오기
    u_choice = user_choice()

    # 컴퓨터 선택 가져오기
    c_choice = com_choice()

    # 승부 결과 가져오기
    match_score = who_win(u_choice, c_choice)
    # 승부 결과 출력
    print(
        f"\n사용자 {choice_dic[u_choice]} vs 컴퓨터 {choice_dic[c_choice]} 입니다. {result_dic[match_score]}\n")
    return match_score


def user_choice():
    re = 1
    i = float(input("// 가위 : 1 바위 : 2 보 : 3 // : "))
    while re:
        if i > 3 or i < 0:
            i = int(input("//다시 입력!!!//\n //가위 : 1 바위 : 2 보 : 3 // : "))
        elif i % 1 != 0:
            i = int(input("//다시 입력!!!//\n //가위 : 1 바위 : 2 보 : 3 // : "))
        else:
            re = 0
            break
    return i


def com_choice():
    import random as r
    return r.randint(1, 3)


def who_win(u_choice, c_choice):
    if u_choice == "1":  # 참가자가 가위를 냈을 때
        if c_choice == "1":  # 컴퓨터가 가위를 냈을 때
            return 0
        elif c_choice == "2":  # 컴퓨터가 바위를 냈을 때
            return -1
        else:
            return 1  # 컴퓨터가 보를 냈을 때
    elif u_choice == "2":  # 참가자가 바위를 냈을 때
        if c_choice == "1":
            return 1
        elif c_choice == "2":
            return 0
        else:
            return -1
    else:  # 참가자가 보를 냈을 때
        if c_choice == "1":
            return -1
        elif c_choice == "2":
            return 1
        else:
            return 0


def again_fn():
    again = int(input("재대결 : 1 , 끝내기 : 0    : "))
    while True:
        if again == 1:
            v = True
            break
        elif again == 0:
            v = False
            break
        else:
            again = int(input("//다시 입력!!!//\n재대결 : 1 , 끝내기 : 0"))
    return again


u_score = 0
c_score = 0
v = True
match_cnt = 1
while(v):
    if match_cnt == 5:
        print("마지막 매치 입니다!")
    else:
        print(f"{match_cnt}번째 매치 입니다!")
    score_dec = match()
    if score_dec == 1:
        u_score = u_score+1
    elif score_dec == -1:
        c_score = c_score+1
    else:
        u_score = u_score+1
        c_score = c_score+1

    if match == 5:
        if u_score > c_score:
            print("최종 승리자는 유저 입니다!")
        elif u_score < c_score:
            print("최종 승리자는 컴퓨터 입니다!")
        else:
            print("최종 게임 결과는 무승부 입니다!")
        v = again_fn()
        if v == True:
            u_score = 0
            c_score = 0
            match_cnt = 0
    else:
        if u_score == c_score and match_cnt == 3:
            print("최종 게임 결과는 무승부 입니다!\n")
            v = again_fn()
            if v == True:
                u_score = 0
                c_score = 0
                match_cnt = 0
        elif u_score >= 3:
            print("최종 승리자는 유저 입니다!")
            v = again_fn()
            if v == True:
                u_score = 0
                c_score = 0
                match_cnt = 0
        elif u_score >= 3:
            print("최종 승리자는 컴퓨터 입니다!")
            v = again_fn()
            if v == True:
                u_score = 0
                c_score = 0
                match_cnt = 0
    match_cnt = match_cnt+1
