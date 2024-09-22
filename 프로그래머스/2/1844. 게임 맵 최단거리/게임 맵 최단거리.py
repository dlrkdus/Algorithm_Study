from collections import deque
def solution(maps):
    n = len(maps) #세로
    m = len(maps[0]) #가로
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    d=deque()
    d.append((0,0))
    visited = [[0 for i in range(m)]for j in range(n)]
    visited[0][0]=1
    def bfs():
        while d:
            x,y = d.popleft()
            for i in range(4):
                new_x = x + nx[i]
                new_y = y + ny[i]
                if 0<=new_x<n and 0<=new_y<m and maps[new_x][new_y]!=0:
                    if not visited[new_x][new_y]:
                        visited[new_x][new_y]=1
                        maps[new_x][new_y]+=maps[x][y]
                        d.append((new_x,new_y))
    bfs()
    for row in maps:
        print(row)
        print()
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]
            
        


                
                
        