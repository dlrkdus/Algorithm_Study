import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

V, E = map(int,input().split())
K = int(input()) #시작 정점 
hq = [] #heapq 로 가중치 자동 정렬 
dp = [INF]*(V+1)
graph = [[] for i in range(V+1)]

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(hq,(0,start))

    while hq:
        now_weight, now_node = heapq.heappop(hq)
        if now_weight > dp[now_node]:
            continue
        for next_node, next_weight in graph[now_node]:
            weightSum = now_weight + next_weight
            if weightSum < dp[next_node]:
                dp[next_node]=weightSum
                heapq.heappush(hq,(weightSum,next_node))

for _ in range(E):
    u, v, w = map(int,input().split()) # u -> v 가중치 w
    graph[u].append([v,w])

Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i]==INF else dp[i])

