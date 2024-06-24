from collections import deque
N = int(input())
d = deque([i for i in range(1,N+1)])

while(True):
    if len(d)<=1:
        break
    d.popleft()
    if len(d)<=1:
        break
    d.append(d.popleft())

print(d[0])