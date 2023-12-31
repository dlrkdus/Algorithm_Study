from collections import deque

n,m,v=map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1   

def dfs(v): #백트래킹이 없어서 코드가 단순하다. 
    visited[v]=1 #방문시 1 표시. 방문 유무와 연결 유무 두 가지가 필요하다. 
    print(v,end=" ") #end=" "는 마지막 출력을 줄바꿈이 아닌 공백으로 바꿔준다.
    for i in range(1,n+1): #그래프의 깊이만큼 돌며 
        if visited[i]==0 and graph[v][i]==1: #방문하지 않은 노드이자 v와 연결된 노드를 찾아준다. 
                                             #연결을 어떻게 표현할지 고민했는데 행값에 v를 넣어주면 되는거였다.
            dfs(i) #연결된 노드가 새로운 v로 올라간다. 
dfs(v)
visited=[0]*(n+1)

def bfs(v): #큐는 선입선출
  q = deque() #큐 생성
  q.append(v)       
  visited[v] = 1   
  while q:
    v = q.popleft() #popleft()는 deque에서만 사용 가능
    print(v, end = " ")
    for i in range(1, n + 1):
      if visited[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visited[i] = 1
print()
bfs(v)