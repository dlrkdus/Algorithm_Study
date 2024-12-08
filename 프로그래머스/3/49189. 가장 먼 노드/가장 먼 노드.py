from collections import deque, defaultdict
def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)  
        
    visited = [0 for i in range(n+1)]
    visited[1] = 1
    distance = [float('inf')] * (n + 1)    
    distance[1] = 0 
    distance[0] = -1
    d = deque([1])

    while d:
        now = d.popleft()
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                distance[neighbor ] = distance[now] + 1
                d.append(neighbor)

    return distance.count(max(distance))
    