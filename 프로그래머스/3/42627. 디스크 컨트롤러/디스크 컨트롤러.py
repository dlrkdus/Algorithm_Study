import heapq
# 평균 대기시간을 줄이는게 관건이겠지? 그러려면 실행 시간이 짧은 것을 우선적으로 실행하는게 유리할거야 
def solution(jobs):
    sum, now, i = 0,0,0
    start = -1
    hq = []
    
    while i<len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(hq,[j[1],j[0]])
        if len(hq) > 0:
            current = heapq.heappop(hq)
            start = now
            now += current[0]
            sum += (now - current[1])
            i+=1
        else:
            now +=1
    return int(sum/len(jobs))