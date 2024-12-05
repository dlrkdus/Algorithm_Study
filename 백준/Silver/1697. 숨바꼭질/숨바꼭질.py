from collections import deque
N, K = map(int,input().split())
MAX = 10 **5
visited = [0] * (MAX+1)
arr = [0] * (MAX+1)
d = deque()
d.append(N)

while d:
    x = d.popleft()
    if x == K:
        print(arr[K])
        break
    for i in [x-1,x+1,2*x]:
        if 0<=i<=MAX and not visited[i]:
            visited[i] = 1
            arr[i] = arr[x] + 1 
            d.append(i)

