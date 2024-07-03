import sys
input=sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a != b:
        parent[a] = b

V, E = map(int, input().split())
arr, parent = [], [i for i in range(V)]

for _ in range(E):
    v1, v2, dist = map(int, input().split())
    arr.append([dist, v1-1, v2-1])

arr.sort() # 가중치를 정렬한다. 

result = 0
for a in arr:
    if find(a[1]) == find(a[2]): # 부모가 같다 = 같은 집합이다 = 사이클
        continue

    union(a[1], a[2])
    result += a[0]

print(result)