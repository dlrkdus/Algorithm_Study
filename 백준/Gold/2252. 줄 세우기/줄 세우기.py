from collections import deque
N, M = map(int,input().split())
indegree = [0 for i in range(N+1)]
graph = [[] for _ in range(N + 1)]

# 진입차수 기록하고 1씩 빼면서 0인 것들 출력하자 
for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1

d= deque()
#이걸 bfs로 풀어야할듯 

def bfs():
    for i in range(1,N+1):
        if indegree[i]==0:
            d.append(i)

    while d:
        idx = d.popleft()
        print(idx,end=" ")
        for i in graph[idx]:
            indegree[i]-=1
            if indegree[i]==0:
                d.append(i)           

bfs()




