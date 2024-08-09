from collections import deque
n = int(input())
arr = []
d = deque()
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

max_area = -1
nx = [0,0,1,-1]
ny = [1,-1,0,0]

def bfs(height,a,b):
    d.append([a,b])
    while d:
        x,y = d.popleft()
        for i in range(4):
            new_x = x+nx[i]
            new_y = y+ny[i]
            if 0<=new_x<n and 0<=new_y<n:
                if arr[new_x][new_y]>height and not visited[new_x][new_y]:
                    visited[new_x][new_y]=1
                    d.append([new_x,new_y])


for i in range(max(max(i) for i in arr)):
    count=0
    visited = [[0 for i in range(n)]for j in range(n)]
    for a in range(n):
        for b in range(n):
            if arr[a][b]>i and not visited[a][b]:
                bfs(i,a,b)
                count+=1
    max_area = max(max_area,count)

print(max_area)

