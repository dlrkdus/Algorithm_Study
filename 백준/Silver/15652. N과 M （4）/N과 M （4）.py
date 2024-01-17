n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]
tmp=[0]*m #m개 뽑는다.

def dfs(level,index):   
    if level==m:
        print(*tmp)
        return
    for i in range(index,n):
        tmp[level]=arr[i]
        dfs(level+1,i) #다음 원소 뽑기
dfs(0,0)