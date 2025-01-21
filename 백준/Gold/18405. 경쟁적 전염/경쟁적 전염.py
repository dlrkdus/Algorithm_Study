from collections import deque
# N*N , K개 종류의 바이러스
N, K = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(N)]
# S초 후에 (X,Y)의 바이러스 종류 구하기
S, X, Y = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append((arr[i][j],i,j,0))

virus.sort()
d = deque(virus)

while d:
    virus,x,y,time = d.popleft()
    if time == S:
        break
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0<=new_x<N and 0<=new_y<N and arr[new_x][new_y] == 0:
            arr[new_x][new_y] = virus
            d.append([virus,new_x,new_y,time+1])


print(arr[X-1][Y-1])