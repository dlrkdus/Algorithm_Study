from collections import deque

d=deque()
T=int(input())
for i in range(T):
    count=0
    cmd = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    d=deque(imp)
    c_index=cmd[1]

    while(True):
        if d[0]==max(d): #맨앞의 수가 최대일때
            d.popleft()
            count+=1
            if c_index==0: #최대이자 찾는 수 =>결과!               
                print(count)
                break
            else: #최대지만 찾는 수 X                              
                c_index-=1
        else: #맨앞의 수가 최대가 아닐때
            d.append(d.popleft()) #일단 뒤로 보내자
            if c_index==0: #찾는 수지만 최대는 아닐때
                c_index=len(d)-1 #찾는 수는 맨뒷자리
            else: #찾는 수도 아니고 최대도 아닐 때
                c_index-=1

        
        
