import heapq
# 평균 대기시간을 줄이는게 관건이겠지? 그러려면 실행 시간이 짧은 것을 우선적으로 실행하는게 유리할거야 
def solution(jobs):
    sum, now, i = 0,0,0
    start = -1
    hq = []
    
    while i<len(jobs):
        for j in jobs:
            if start < j[0] <= now: # 디스크가 실행되는 동안(start ~ now) 들어온 요청부터 처리
                heapq.heappush(hq,[j[1],j[0]]) # 실행 시간이 짧은 순으로 처리
        if len(hq) > 0:
            current = heapq.heappop(hq)
            start = now
            # current[0] = 작업 소요 시간, current[1] = 요청 시각
            now += current[0]
            sum += (now - current[1]) # now - current[1] = 요청부터 처리 완료까지의 시간 
            i+=1
        else:
            now +=1 # 잉여 시간이면 now 땡기기
    return int(sum/len(jobs))
