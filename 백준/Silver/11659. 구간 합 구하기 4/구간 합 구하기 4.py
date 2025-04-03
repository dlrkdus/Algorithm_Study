N, M = map(int,input().split())
arr = list(map(int,input().split()))
sum = [0]
s = 0
for i in arr:
    s+=i
    sum.append(s)

for i in range(M):
    x, y = map(int,input().split())
    result = sum[y] - sum[x-1]
    print(result)
 