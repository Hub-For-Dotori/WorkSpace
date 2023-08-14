import pandas as pd

# 인사고과 데이터 프레임 작성하기
df_PE = pd.DataFrame(
    columns=["사번", "이름", "부서", "직무", "근무태도", "업무효율", "업무성과",
             "업무지식", "대인관계", "상사평가종합", " 동료_업무역량", "동료_업무성과",
             "동료_대인관계", "동료_평가종합", "평가종합", "평가등급"]
)


# 동료평가 데이터 프레임 작성하기

df_GR = pd.DataFrame(
    columns=["피평가자 사번", "평가자 사번", "업무역량", "업무성과", "대인관계"]
)
'''
# 데이터 프레임 엑셀 저장하기
df_PE.to_excel("df_PE.xlsx", index=False)
'''
base_data = [["10001", "이현지", "영업팀", "영업"],
             ["10002", "김성수", "영업팀", "영업"],
             ["10003", "박한성", "영업팀", "사무"],
             ["10004", "김지우", "영업팀", "영업"],
             ["10005", "서광덕", "개발1팀", "기술"],
             ["10006", "임지훈", "개발1팀", "기술"],
             ["10007", "강형민", "개발1팀", "기술"],
             ["10008", "조성우", "개발1팀", "사무"],
             ["10009", "이인혁", "개발2팀", "기술"],
             ["10010", "장은지", "개발2팀", "기술"],
             ["10011", "황선희", "개발2팀", "기술"],
             ["10012", "이석희", "개발2팀", "기술"]]

# for 구문을 사용하여 기본 데이터를 df_PE 데이터프레임에 일괄 입력하기
for idx, base in enumerate(base_data):
    for col_idx, col_name in enumerate(["사번", "이름", "부서", "직무"]):
        df_PE.loc[idx, col_name] = base[col_idx]


def dept_eval(emp_no, att, eff, perf, know, rel, df):
    grade_dict = {"A+": 100, "A": 90, "B+": 85, "B": 80,
                  "C+": 75, "C": 70, "D+": 65, "D": 60, "F": 50}

    df.loc[df.사번 == emp_no, ["근무태도", "업무효율", "업무성과", "업무지식", "대인관계"]] = \
        [grade_dict[att], grade_dict[eff], grade_dict[perf],
            grade_dict[know], grade_dict[rel]]  # 해당 값에 딕셔너리를 활용하여 점수 넣어주기
    return df


df_PE = dept_eval("10001", "A+", "B+", "A", "A", "D", df_PE)
df_PE.loc[df_PE.사번 == "10001", ["사번", "이름", "부서",
                                "근무태도", "업무효율", "업무성과", "업무지식", "대인관계"]]
print(df_PE.loc[df_PE.사번 == "10001"])


# =====================================================================================
'''
1) 평가할 부서 입력 받고 해당 부서 직원의 사번, 이름, 부서명, 직무 출력
2) 평가 대상 사원의 사번을 받아 입력되거나 입력한 사번이 있는지 존재 확인. 없을 경우 적절한 메시지 후 재 입력
3) 사번 적합시 근무태도, 업무효율, 업무성과, 업무지식, 대인관계 순서로 점수 입력
4) 해당 피 평가자의 평가 입력이 종료될 시 해당 평가자의 사번, 이름과 함께 위의 다섯 분야의 점수를 A+식으로 출력하여 확인 가능 구현
1.1 + 2.5 (4명당) 85 
'''


def get_dept(df):
    dept_lst = list(set(df_PE["부서"]))
    while True:
        dept_sel = input(f"평가할 부서명 {dept_lst} 중에서 입력하세요: ")
        if dept_sel in dept_lst:
            break
        print(f"{dept_sel}은 적합한 부서명이 아닙니다.")
    return dept_sel


def show_dept_emp(dept_name, df):
    df = df.loc[df.부서 == dept_name, ["부서", "사번", "이름", "직무"]]
    print(df)


def get_emp_no(dept_name, df):
    emp_no_lst = list(df.loc[df.부서 == dept_name, "사번"])

    while True:
        show_dept_emp(dept_name, df)
        emp_no_sel = input(f"평가할 {dept_name} 사원번호를 입력하세요:")
        if emp_no_sel in emp_no_lst:
            break
        print(f"{emp_no_sel}은 적합한 사번이 아닙니다.")

    return emp_no_sel
