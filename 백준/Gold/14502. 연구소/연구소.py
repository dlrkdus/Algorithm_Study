from itertools import combinations
from collections import deque
import copy
N,M = map(int,input().split())
map = [list(map(int,input().split()))for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []

def make_walls(map, wall):
    new_map = copy.deepcopy(map)
    for w in wall:
        new_map[w[0]][w[1]] = 1
    return new_map
    
def bfs(map):
    visited = [[0 for i in range(M)]for j in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and map[i][j] == 2:
                d = deque()
                d.append([i,j])
                while d:
                    x,y = d.popleft()
                    for a in range(4):
                        new_x = x + dx[a]
                        new_y = y + dy[a]
                        if 0<=new_x<N and 0<=new_y<M:
                            if not visited[new_x][new_y] and map[new_x][new_y]==0:
                                visited[new_x][new_y] = 1
                                map[new_x][new_y] = 2
                                d.append([new_x, new_y])
    return sum(row.count(0) for row in map)

# 3개의 벽을 세우는 모든 경우의 수를 구한다. 
walls = list(combinations([(i,j) for i in range(N)for j in range(M)if map[i][j] == 0],3))
for wall in walls:
    new_map = make_walls(map,wall)
    result.append(bfs(new_map))

print(max(result))


