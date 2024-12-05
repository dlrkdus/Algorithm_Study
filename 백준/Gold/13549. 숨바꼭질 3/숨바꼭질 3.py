from collections import deque
N, K = map(int,input().split())
MAX = 10 **5
visited = [0] * (MAX+1)
arr = [0] * (MAX+1)
d = deque()
d.append(N)
min_cnt = 0

while d:
    now = d.popleft()
    if now == K:
        print(arr[K])
        break
    for next in [2*now, now-1,now+1]:
        if 0<=next<=MAX and not visited[next]:
            visited[next] = 1
            if next == 2*now:
                arr[next] = arr[now]
            else:
                arr[next] = arr[now] + 1 
            d.append(next)
