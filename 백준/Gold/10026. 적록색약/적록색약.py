import sys
sys.setrecursionlimit(10000) #파이썬에서 재귀 한도를 풀어준다.

N = int(input())

arr = [list(input()) for _ in range(N)]
visited = [[0] * (N+1) for _ in range(N+1)]

count_normal=0
count_blind=0
nx=[0,0,1,-1]
ny=[1,-1,0,0]

def dfs(row,col):
    visited[row][col]=1
    for i in range(4):
        new_row=row+nx[i]
        new_col=col+ny[i]
        if 0<=new_row<N and 0<=new_col<N and arr[row][col]==arr[new_row][new_col] and visited[new_row][new_col]==0:
            dfs(new_row,new_col)

for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            dfs(i,j)
            count_normal+=1

for i in range(N):
    for j in range(N):
        if arr[i][j]=='R' or arr[i][j]=='G':
            arr[i][j]='C'
        visited[i][j]=0

for i in range(N): 
    for j in range(N):
        if visited[i][j]==0:
            dfs(i,j)
            count_blind+=1

print(count_normal,count_blind)
 
