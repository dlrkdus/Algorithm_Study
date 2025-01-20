from collections import deque
from collections import defaultdict
# N = 도시 개수, M = 도로 개수, K = 최단 거리, X = 출발 도시
N, M, K, X = map(int,input().split())
graph = defaultdict(list)
visited = [0 for i in range(N+1)]
distance = [1 for i in range(N+1)]
visited[X] = 1
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque()
q.append(X)
while q:
    now = q.popleft()
    for neighbor in graph[now]:
        if not visited[neighbor]:
            visited[neighbor] = 1
            distance[neighbor]+=distance[now]
            q.append(neighbor)

result = False
for i in range(len(distance)):
    if distance[i]-1 == K:
        result = True
        print(i)

if result == False:
    print(-1)