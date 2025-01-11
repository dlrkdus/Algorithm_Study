from collections import deque, defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0]) # 양방향 그래프로 설정
    distance = [0 for i in range(n+1)]
    visited = [0 for i in range(n+1)]
    visited[1] = 1
    q= deque()
    q.append(1)
    while q:
        now = q.popleft()
        neighbors = graph[now]
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = 1
                distance[neighbor]= distance[now]+1
                q.append(neighbor)
    return distance.count(max(distance))
            
        
            
    