T= int(input())

def dfs(i,sum):
    global count
    if sum>K or i ==N:
        if sum==K:
            count+=1
        return 
    dfs(i+1,sum)
    dfs(i+1,sum+arr[i])


for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 0
    dfs(0,0)
    print(f"#{test_case}", count)
        
