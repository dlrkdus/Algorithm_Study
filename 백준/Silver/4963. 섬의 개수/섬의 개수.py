import sys
sys.setrecursionlimit(10000) #dfs, bfs 문제에선 반드시 사용
def dfs(i,j):
    nx = [0,0,1,1,1,-1,-1,-1]
    ny = [1,-1,0,1,-1,0,1,-1]
    for x in range(8):
        new_x = i+nx[x]
        new_y = j+ny[x]
        if 0<=new_x<h and 0<=new_y<w and not visited[new_x][new_y]:
            if island[new_x][new_y]==1:
                visited[new_x][new_y]=1
                dfs(new_x,new_y)


while(True):
    w,h = map(int,input().split())
    visited = [[0 for i in range(w)]for j in range(h)]
    if w==0 and h==0:
        break

    island = [list(map(int,input().split())) for j in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island[i][j]==1:
                dfs(i,j)
                count+=1

    print(count)


