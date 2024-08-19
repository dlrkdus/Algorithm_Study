import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N+1)]

def dfs(node):
    for v in graph[node]:
        if not visited[v]:
            visited[v]=1
            dfs(v)

count=0
for i in range(1,N+1):
    if not visited[i]:
        visited[i]=1
        dfs(i)
        count+=1

print(count)
