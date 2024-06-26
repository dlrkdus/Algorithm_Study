import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

#상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

def bfs():
     while q:
         x, y = q.popleft()
         for i in range(4):  
             nextX = x + dx[i] 
             nextY = y + dy[i]
             if 0 <= nextX < n and 0 <= nextY < m and box[nextX][nextY] == 0:
                box[nextX][nextY] = box[x][y] + 1 
                q.append([nextX, nextY])
bfs()

answer = 0
for line in box:
     for tomato in line:
         if tomato == 0:
             print(-1)
             exit(0)
     answer = max(answer, max(line)) 
print(answer-1)