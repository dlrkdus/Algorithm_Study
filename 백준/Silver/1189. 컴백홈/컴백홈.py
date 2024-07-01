R, C, K = map(int,input().split())
arr = [list(input()) for j in range(R)]
visited = [[0 for i in range(C)]for j in range(R)]
visited[R-1][0]=1
result = []

def dfs(i,j,cnt):
    nx = [0,0,-1,1]
    ny = [1,-1,0,0]
    if (i,j) == (0,C-1):
        result.append(cnt)
        return 
    for x in range(4):
        new_x = i+nx[x]
        new_y = j+ny[x]
        if 0<=new_x<R and 0<=new_y<C and not visited[new_x][new_y]:
            if arr[new_x][new_y]!='T':
                visited[new_x][new_y]=1
                dfs(new_x, new_y,cnt+1)
                visited[new_x][new_y]=0


dfs(R-1,0,1)
answer = 0

for i in result:
    if i == K:
        answer+=1

print(answer)