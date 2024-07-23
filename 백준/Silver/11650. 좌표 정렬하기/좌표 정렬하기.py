N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])

result = sorted(arr)

for a in result:
    print(' '.join(map(str,a)))
