from collections import deque
def solution(n, computers):
    visited = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i,n,computers,visited)
            answer+=1
    return answer

def dfs(i,n,computers,visited):
    visited[i]=1
    for x in range(n):
        if computers[i][x]==1 and not visited[x]:
            dfs(x,n,computers,visited)


