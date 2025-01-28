from itertools import combinations
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chickens = []
homes = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append([i,j])
        if arr[i][j] == 2:
            chickens.append([i,j])

def get_chicken_load(home, chicken):
    cl = 100000000000
    for c in chicken:
        load = abs(c[0]-home[0]) + abs(c[1]-home[1])
        cl = min(cl,load)
    return cl

answer = 1000000000

for comb in list(combinations(chickens,M)):
    result = []
    for home in homes:
        result.append(get_chicken_load(home,comb))
    answer = min(answer,sum(result))
        
print(answer)

    

