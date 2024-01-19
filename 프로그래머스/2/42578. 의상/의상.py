def solution(clothes):
    arr={}
    for i in range(len(clothes)):
        arr[clothes[i][1]]=arr.get(clothes[i][1],0)+1
    answer=1
    for i in arr.values():
        answer*=(i+1) #한 종류를 아예 안 입는 경우도 있기 때문에 +1
    return answer-1 #아무것도 입지 않는 경우도 있기 때문에 -1