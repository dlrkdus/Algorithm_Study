import sys
sys.setrecursionlimit(10000) #dfs, bfs 문제에선 반드시 사용
from collections import deque

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
def bfs(x,y):
    nx = [1, 1, -1, -1, 1, -1, 0, 0]
    ny = [0, 1, 0, 1, -1, -1, 1, -1]
    q = deque()
    q.append([x, y]) #큐에 시작좌표 넣어주기
    while q:
        a,b=q.popleft() #a,b=x,y
        for i in range(8):
            new_x=a+nx[i]
            new_y=b+ny[i]
            if 0<=new_x<h and 0<=new_y<w:
                if m[new_x][new_y]==1:
                    m[new_x][new_y]=0
                    q.append([new_x,new_y]) #재귀 대신 큐에 넣어주기 
        #만약 주변에 남은 섬이 없다면 q.append가 실행되지 않아 큐가 종료된다.(빈 큐)
                

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
                #bfs(i,j)
                dfs(i,j)
                count+=1
    print(count)
