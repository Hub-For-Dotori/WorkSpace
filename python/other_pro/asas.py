
'''
u_choice = 2
c_choice = 3
i = 0
j = 0
print("rhrhrh")
while(u_choice != i and c_choice != j):
    while(u_choice != i):
        i = i+1
    while(c_choice != j):
        j = j+1
    print("i값 :", i, "j값 :", j)
dec = i-j
while(u_choice == i and c_choice == j):
    while(dec == 1 and (u_choice == 2 or u_choice == 3)):
        D = "이김"
        print("i값 :", i, "j값 :", j, "//이김")
        break

    while(dec == -2 and u_choice == 1):
        D = "이김"
        print("i값 :", i, "j값 :", j, "//이김")
        break

    while(dec == -1 and (u_choice == 1 or u_choice == 2)):
        D = "짐"
        print("i값 :", i, "j값 :", j, "//짐")
        break

    while(dec == 2 and u_choice == 3):
        D = "짐"
        print("i값 :", i, "j값 :", j, "//짐")
        break

    while(dec == 0):
        D = "비김"
        print("i값 :", i, "j값 :", j, "//비김")
        break
    res = {'이김': 1, '짐': -1, '비김': 0}
    break
print(res[D])
'''


def who_win():
    u_choice = 1
    c_choice = 3
    i = 0
    j = 0

    while(u_choice != i and c_choice != j):
        while(u_choice != i):
            i = i+1
        while(c_choice != j):
            j = j+1
        print("i값 :", i, "j값 :", j)
    dec = i-j
    while(u_choice == i and c_choice == j):
        while(dec == 1 and (u_choice == 2 or u_choice == 3)):
            D = "이김"
            print("i값 :", i, "j값 :", j, "//이김")
            break

        while(dec == -2 and u_choice == 1):
            D = "이김"
            print("i값 :", i, "j값 :", j, "//이김")
            break

        while(dec == -1 and (u_choice == 1 or u_choice == 2)):
            D = "짐"
            print("i값 :", i, "j값 :", j, "//짐")
            break

        while(dec == 2 and u_choice == 3):
            D = "짐"
            print("i값 :", i, "j값 :", j, "//짐")
            break

        while(dec == 0):
            D = "비김"
            print("i값 :", i, "j값 :", j, "//비김")
            break
        win_dec = {'이김': 1, '짐': -1, '비김': 0}
        return win_dec.get(D)


print("함수 리턴 값 : ", who_win())
