arr=list(map(str,input()))
count=0
stick=0
i=0
while True:
    if arr[i]=="(":
        if arr[i+1]==")": #레이저일 때
            i+=1
            count+=stick
            #print("레이저로 자름(+",stick,"):",count)
        else: #쇠막대기일 때
            stick+=1
    else: #레이저가 아니고 쇠막대기 종료
        stick-=1
        count+=1   
        #print("쇠막대기 종료(+",1,"):",count)
    i+=1
    if i>len(arr)-1:
        break
    

print(count)
        


