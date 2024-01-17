n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
tmp=[0]*m #m개 뽑는다.
visited=[0]*n #n개의 배열

def dfs(level):   
    if level==m:
        print(*tmp)
        return
    for i in range(n):
        if visited[i]==0:
            visited[i]=1 #방문!
            tmp[level]=arr[i]
            dfs(level+1) #다음 원소 뽑기
            visited[i]=0
dfs(0)