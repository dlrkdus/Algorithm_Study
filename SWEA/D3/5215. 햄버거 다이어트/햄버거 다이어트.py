T=int(input())
 
def dfs(idx,cal_sum,like_sum):
    if cal_sum > L or idx == N:
        if cal_sum <= L:
            comb.append(like_sum)
        return
    dfs(idx+1, cal_sum+ingredient[idx][1],like_sum+ingredient[idx][0])
    dfs(idx+1, cal_sum,like_sum)
 
 
for test_case in range(1,T+1):
    N, L = map(int,input().split())
    ingredient = []
    comb = []
    for _ in range(N):
        x=list(map(int,input().split()))
        ingredient.append(x)
    dfs(0,0,0)
    print(f"#{test_case}",max(comb))
