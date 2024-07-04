def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union(x,y):	#더 작은 비용을 기준으로 병합
    x_parent = get_parent(x)
    y_parent = get_parent(y)
    if cost[x_parent] > cost[y_parent]:
        cost[x_parent] = 0
        parent[x_parent] = y_parent
    else:
        cost[y_parent] = 0
        parent[y_parent] = x_parent

n, m, k = map(int, input().split())

cost = [0]  #친구비 리스트
for c in list(map(int, input().split())):
    cost.append(c)

parent = [i for i in range(n+1)]    #부모 노드 저장할 리스트

for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

total_cost = sum(cost)
#총 비용이 예산보다 크다면 친구 다 사귈 수 없다.
if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")