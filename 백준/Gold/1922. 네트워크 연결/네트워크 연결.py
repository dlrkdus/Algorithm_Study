import sys 
input = sys.stdin.readline
N= int(input())
M= int(input())
parent = [i for i in range(N+1)]
value = []

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b]=a


for _ in range(M):
    a, b, c = map(int,input().split())
    value.append([c,a,b])

value.sort()
result = 0

for v in value:
    if find(v[1])!=find(v[2]): #같은 집합이 아니다 = 사이클이 아니다 
        union(v[1],v[2])
        result+=v[0]

print(result)



