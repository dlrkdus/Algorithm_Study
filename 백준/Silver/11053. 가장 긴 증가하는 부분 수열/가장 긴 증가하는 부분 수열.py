N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 최소 길이는 1(자기 자신 포함)

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:  # 증가하는 부분 수열이 가능할 때
            dp[i] = max(dp[i], dp[j] + 1) # 기존 VS j까지의 LIS + 1

# 즉, dp[i]는 i번째 문자를 반드시 포함했을 때의 LIS 길이다.
# 왜 LIS는 dp[i]를 i번째까지 중 LIS의 길이 로 구하는게 아니라 i번째 문자를 포함한 LIS 로 푸는가?
# arr[i]가 arr[j]보다 크다는 것은 arr[j]를 포함하는 LIS보다는 무조건 + 1 인게 확정이기 때문이다.
# 따라서 출력할 때도 마지막 문자를 포함하는 LIS가 아닌, 전체 LIS 중 가장 큰 값으로 출력해야 한다.
print(max(dp)) 