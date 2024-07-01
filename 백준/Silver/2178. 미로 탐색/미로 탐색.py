from collections import deque
N, M  = map(int,input().split())
arr = [list(map(int,input())) for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
arr[0][0]=0
nx = [0,0,-1,1]
ny = [1,-1,0,0]
d = deque()
d.append([0,0])

def bfs():
    while d:
        x,y = d.popleft()
        if x==N-1 and y==M-1:
            return
        for i in range(4):
            new_x = x+nx[i]
            new_y = y+ny[i]
            if 0<=new_x<N and 0<=new_y<M and arr[new_x][new_y]!=0:
                if not visited[new_x][new_y]:
                    visited[new_x][new_y]=1
                    arr[new_x][new_y]=arr[x][y]+1
                    d.append([new_x,new_y])





bfs()
print(arr[N-1][M-1]+1)



