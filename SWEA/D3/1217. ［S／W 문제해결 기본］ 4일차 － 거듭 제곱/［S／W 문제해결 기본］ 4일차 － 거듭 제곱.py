def cal(N, M):
    n = N
    while(M>1):
        N*=n
        M-=1
    return N

for test_case in range(1,11):
    T = int(input())
    N, M = map(int,input().split())

    result = cal(N,M)
    print(f"#{T}", result)

            
