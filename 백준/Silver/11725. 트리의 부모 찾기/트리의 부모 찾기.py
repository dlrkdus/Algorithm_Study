import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    


haveParent=[0]*(n+1)

def dfs(node):
    for a in arr[node]:
        if not haveParent[a]:
            haveParent[a]=node
            dfs(a)

dfs(1)

for i in range(2, n+1):
    print(haveParent[i])






