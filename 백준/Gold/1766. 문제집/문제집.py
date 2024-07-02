import heapq
N, M = map(int,input().split())
graph = [[]for i in range(N+1)]
indegree = [0 for i in range(N+1)]
hq = []
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B) #A 이후에 오는 문제들 누적 
    indegree[B]+=1 #진입차수 누적 

def bfs():
    for i in range(1,N+1):
        if indegree[i]==0:
            heapq.heappush(hq,i)

    while hq:
        idx = heapq.heappop(hq)
        print(idx,end=" ")
        for i in graph[idx]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(hq,i)

bfs()

