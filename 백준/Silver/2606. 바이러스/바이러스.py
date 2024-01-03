n=int(input()) #노드
v=int(input()) #간선
graph = [[] for _ in range(n+1)]
visited=[0]*(n+1)
count=0

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v]=1
    global count
    count+=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)

dfs(1)
print(count-1)