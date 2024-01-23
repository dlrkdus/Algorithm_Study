from collections import deque
def solution(priorities, location):
    answer = 0
    p=deque(priorities)
    while p:
        if p[0]==max(p):
            answer+=1
            p.popleft()
            if location==0:
                break
            else:
                location-=1
        else:
            p.append(p.popleft())
            if location==0:
                location+=(len(p)-1)
            else:
                location-=1
            
            
    
    return answer