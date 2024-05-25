import sys
sys.setrecursionlimit(10000) #파이썬에서 재귀 한도를 풀어준다.

def dfs(x,y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4): #상하좌우 4가지 경우 따지기
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0 #방문했다면 0으로 초기화 (visited)
                dfs(nx, ny)


t=int(input())
for _ in range(t):
    count=0
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(m)] #m은 행 n은 열
    for _ in range(k):
        c, r= map(int, input().split())
        matrix[c][r]=1
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)

