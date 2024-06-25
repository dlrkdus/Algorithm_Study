import heapq
N = int(input())
hq = []
S = []
for i in range(N):
    s = list(map(int,input().split()))
    S.append(s)

S.sort()
hq = [] # 종료 시간을 담을 heapq , h[0]은 가장 이른 종료시간대가 된다

for i in range(N):
    heapq.heappush(hq, S[i][1]) # 일단 종료시간을 넣어주자
    if hq[0]<=S[i][0]: # 시작 시간이 종료 시간보다 뒤라면
        heapq.heappop(hq) # 한 강의실로 배정            

print(len(hq))





