import sys
sys.setrecursionlimit(10000)


def dfs(x,y):
    nx = [1, 1, -1, -1, 1, -1, 0, 0]
    ny = [0, 1, 0, 1, -1, -1, 1, -1]
    for i in range(8):
        new_x=x+nx[i]
        new_y=y+ny[i]
        if 0<=new_x<h and 0<=new_y<w: #행:h 열:w 헷갈림 주의
            if m[new_x][new_y]==1 and visited[new_x][new_y]==0:
                visited[new_x][new_y]=1
                dfs(new_x,new_y)

while(True):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    m = [list(map(int, input().split())) for _ in range(h)]
    #리스트 컴프리헨션으로 이중리스트 입력 받기
    visited=[[0 for j in range(w)] for i in range(h)]
    count=0
    for i in range(h): #행:h 열:w 헷갈림 주의
        for j in range(w):
            if m[i][j]==1 and visited[i][j]==0:
                dfs(i,j)
                count+=1
    print(count)

    



