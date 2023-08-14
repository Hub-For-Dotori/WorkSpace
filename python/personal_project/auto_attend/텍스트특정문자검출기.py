def fileopen(data, target): 
    with open(data,'r',encoding='UTF8') as file:    
        text = file.read()        
        if target in text   :        
            flag = True            
            splitdata = text.split()            
        else :        
            flag = False      
            splitdata = None
    return flag, splitdata
def count_word(data,TargetText):
    count = 0
    for i in data :
        if TargetText in i :
            count += 1
    return  count


filepath = "C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/url_code.txt"
TargetText = input("찾고자 하는 단어 입력 : ")
flag, splitdata = fileopen(filepath,TargetText)
print(TargetText+"라는 단어가 포함된 횟수 : ",count_word(splitdata,TargetText))