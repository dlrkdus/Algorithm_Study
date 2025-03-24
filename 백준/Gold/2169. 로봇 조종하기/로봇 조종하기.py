n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# 첫줄부터 업데이트 
for i in range(1,m):
    arr[0][i] += arr[0][i-1]

for i in range(1, n):
    # 점화식 = max(max(위,왼), max(위,오))
    # 위 초기화, 왼 위 비교, 위 오 비교

    # 1. 위에서 내려온 경우로 초기화해준다.
    fromLeft = [arr[i][j] + arr[i-1][j] for j in range(m)]
    fromRight = [arr[i][j] + arr[i-1][j] for j in range(m)]

    # 2. 위 vs 왼
    for j in range(1, m):
        fromLeft[j] = max(fromLeft[j], fromLeft[j-1]+arr[i][j])
    # 3. 위 vs 오
    for j in range(m-2, -1, -1):
        fromRight[j] = max(fromRight[j], fromRight[j+1]+arr[i][j])
    # 4. (위 vs 왼) vs (위 vs 오)
    for j in range(m):
        arr[i][j] = max(fromLeft[j], fromRight[j])

print(arr[-1][-1])