Income_Per_Hour = 0.0
Working_Time_Per_Week = 0.0
Total_income_Per_Month = 0.0
Working_Day_Per_Week = 0
Total_income_Per_Week = 0.0
Fixed_working = 0
week_cnt = 0
retry=1

def Holiday_Pay_Cal(InPH,WoTi,WoDaPeWe): # 일급 = 주휴수당 일하는 시간이 불규칙하여 각각 다르다면 -> 주에 총 일하는 시간 / 주에 일하는 날 수 
    Holiday_Pay = WoTi*InPH/WoDaPeWe
    return Holiday_Pay

def income_Per_week(InPH,WoTi):
    return InPH*WoTi

def Section_Div():
    print("=======================================================\n=======================================================")
    

while (re):
    
    Section_Div()
    if (week_cnt==0):
    
        Income_Per_Hour = float(input("받는 시급으로 입력해주세요 ( 2022년 기준 최저시급 9160원 ) : "))     
        Working_Time_Per_Week = float(input("주당 일하는 시간을 입력해주세요 ( 30시간 30분 이라면 30.5로 입력 하세요 ) : "))
        Working_Day_Per_Week = int(input("주에 일하는 일 수를 작성 하시오 : "))
        Fixed_working = int(input("주에 고정된 근무시간을 갖는가?"))
    
    else : 
        
        Working_Time_Per_Week = float(input("주당 일하는 시간을 입력해주세요 ( 30시간 30분 이라면 30.5로 입력 하세요 ) : "))
        Working_Day_Per_Week = int(input("주에 일하는 일 수를 작성 하시오 : "))
    
    while (Income_Per_Hour<=0 and Working_Time_Per_Week <= 0 and Working_Day_Per_Week<=0):
        
        Section_Div()
        Income_Per_Hour = float(input("다시 받는 시급으로 입력해주세요 ( 2022년 기준 최저시급 9160원 ) : "))     
        Working_Time_Per_Week = float(input("다시 주당 일하는 시간을 입력해주세요 ( 30시간 30분 이라면 30.5로 입력 하세요 ) : "))
        Working_Day_Per_Week = int(input("다시 주에 일하는 일 수를 작성 하시오 : "))
    
    while (Fixed_working != 1 and Fixed_working != 0):
        
        Fixed_working = int(input("다시 입력하시오.\n주에 고정된 근무시간을 갖는가?"))
        
    Section_Div()
    
    print(str(week_cnt+1)+"주차")
    
    if (Working_Time_Per_Week<15):
        Total_income_Per_Week=income_Per_week(Income_Per_Hour,Working_Time_Per_Week)
    
    else :
        Total_income_Per_Week=income_Per_week(Income_Per_Hour,Working_Time_Per_Week)+Holiday_Pay_Cal(Income_Per_Hour,Working_Time_Per_Week,Working_Day_Per_Week)
        print(Total_income_Per_Week)
    
    if (Fixed_working == 1):
        Total_income_Per_Month= 4*Total_income_Per_Week
    else : 
        Total_income_Per_Month=Total_income_Per_Month+Total_income_Per_Week   
             
    print("주급은 : "+str(Total_income_Per_Week)+"원 입니다")
    
    week_cnt = week_cnt+1
    
    if (week_cnt>=4 or Fixed_working == 1):
        print("월급은 : "+str(Total_income_Per_Month)+"원 입니다")
        
        while(True):
            
            re=int(input("다시 할 것이면 1, 아닌 경우 0을 누르시오 : "))
            while(re != 0 and re != 1):
            
                re=int(input("다시 입력하세요.\n다시 할 것이면 1, 아닌 경우 0을 누르시오 : "))
            
            if (re==1):     
                week_cnt = 0
                break        
                
            elif (re==0): 
                break
            
    else :
        pass
        
            