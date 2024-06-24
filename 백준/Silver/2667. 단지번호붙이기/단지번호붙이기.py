N = int(input())

a = [list(input()) for i in range(N)]
visited = [[0 for i in range(N)]for j in range(N)]
result = []
count = 0

def dfs(i,j):
    global cnt
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    for x in range(4):
        new_x = i+nx[x]
        new_y = j+ny[x]
        if 0<=new_x<N and 0<=new_y<N and not visited[new_x][new_y]:
            if a[new_x][new_y]=='1':
                visited[new_x][new_y]=1
                cnt+=1
                dfs(new_x,new_y)
                


for i in range(N):
    for j in range(N):
        cnt = 1
        if a[i][j]=='1' and not visited[i][j]:
            visited[i][j]=1
            dfs(i,j)
            count+=1
            result.append(cnt)

print(count)
result.sort()

for i in result:
    print(i)


