from collections import deque
N, K = map(int,input().split())
MAX = 10** 5
visited = [0 for i in range(MAX+ 1)]
result = [0 for i in range(MAX+ 1)]
q = deque()
q.append(N)
while q:
    n = q.popleft()
    distance = [n,-1,1]
    if n == K:
        break
    for i in range(3):
        if 0<=n+distance[i] <= MAX and not visited[n+distance[i]]:
            visited[n+distance[i]] = 1
            if i== 0:
                result[n+distance[i]] = result[n] 
            else:
                result[n+distance[i]] = result[n] + 1
            q.append(n+distance[i])

print(result[K])
