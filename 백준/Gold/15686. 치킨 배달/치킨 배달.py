# abs(i-x) + abs(j-y)

n,m = map(int,input().split())
arr=[]
house = []
chicken = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
    for j in range(n):
        if arr[i][j]==1:
            house.append([i,j])
        if arr[i][j]==2:
            chicken.append([i,j])

tmp = [0 for i in range(m)]
visited = [0 for i in range(m)]
result = []
def dfs(idx,level):
    if idx==m:
        r = 0
        for h in house:
            min_count=99999
            count=0
            for c in tmp:
                count=(abs(h[0]-c[0])+abs(h[1]-c[1]))
                min_count = min(min_count,count)
            r+=min_count
        result.append(r)
        return
    for i in range(level, len(chicken)):
        tmp[idx]=chicken[i]
        dfs(idx+1,i+1)

dfs(0,0)
print(min(result))