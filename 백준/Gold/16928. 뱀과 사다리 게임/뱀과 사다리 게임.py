from collections import deque
N, M = map(int,input().split())
ladders = {}
snakes = {}
maps = [0] * 101
visited = [0]* 101
for _ in range(N):
    x, y = map(int,input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int,input().split())
    snakes[u] = v

d = deque()
d.append(1)
visited[1] = 1

while d:
    x = d.popleft()
    if x == 100:
        print(maps[x])
        break
    for i in range(1,7):
        num = x + i
        if 0<num<=100 and not visited[num]:
            # bfs에서는 뱀이든 사다리든 모두 탐색에 포함해야 한다. 
            # 뱀이 숫자를 감소시키더라도 결과적으로 해당 경로가 최단 경로가 될 수도 있기 때문이다.
            # 이처럼 bfs는 가능한 모든 경우를 고려한다. 
            if num in ladders.keys():
                num = ladders[num]
            elif num in snakes.keys():
                num = snakes[num]
            if not visited[num]: # 방문된 곳이라면 굳이 최소 횟수 갱신 X 
                visited[num] = 1
                maps[num] = maps[x] + 1
                d.append(num)