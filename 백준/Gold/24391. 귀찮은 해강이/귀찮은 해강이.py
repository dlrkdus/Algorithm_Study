import sys
input=sys.stdin.readline
# 우선 부모를 찾는 연산이 필요하다. 
def find_parent(parent,x):
    if parent[x]!=x: #부모와 자식이 같지 않다면 
        parent[x] = find_parent(parent,parent[x])#그 부모를 타고 올라가며 최종 부모를 찾는다. 
    return parent[x] 

#합병
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b) # 두 원소의 부모를 찾는다. 
    if a!=b: # 두 부모가 다르다면 다른 집합이므로 병합 가능하다. 
        parent[a]=b

n,m = map(int,input().split()) #정점, 간선 
parent = []
count = 0
# 부모 리스트 초기화 
for i in range(n+1):
    parent.append(i)
for _ in range(m):
    A, B = map(int,input().split()) 
    union(parent,A,B)

arr = list(map(int,input().split()))

for i in range(1,len(arr)):
    if find_parent(parent,arr[i-1])!=find_parent(parent,arr[i]):
        count+=1

print(count)



