from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1 for i in range(101)]for j in range(101)]
    visited = [[0 for i in range(101)]for j in range(101)]
    numbering(rectangle,graph)
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    q = deque()
    q.append([cx,cy])
    visited[cx][cy] = 1
    answer =0
    while q:
        cx, cy = q.popleft()
        if cx == ix and cy == iy :
            answer = graph[cx][cy] //2
            break
        for i in range(4):
            new_x = cx + nx[i]
            new_y = cy + ny[i]
            if 0<new_x<=100 and 0<new_y<=100:
                if not visited[new_x][new_y] and graph[new_x][new_y]>=1:
                    visited[new_x][new_y]=1
                    graph[new_x][new_y]+=graph[cx][cy]
                    q.append([new_x,new_y])
    return answer
        

def numbering(rectangle,graph):
    for r in rectangle:
        x1,y1,x2,y2 = r[0]*2, r[1]*2, r[2]*2, r[3]*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if (x1<i<x2 and y1<j<y2):
                    graph[i][j]=0 # 내부는 0으로 채움
                elif graph[i][j]!=0:
                    graph[i][j]=1 # 테두리는 1로 채움 
    