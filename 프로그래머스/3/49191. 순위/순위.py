from collections import Counter
def solution(n, results):
    rank = [[0]*n for _ in range(n)] # 0이면 경기 결과 모름
    for win, lose in results:
        rank[win-1][lose-1] = 1 # 1이면 이긴거
        rank[lose-1][win-1] = -1 # -1이면 진거
    
    # 조건값이 작으므로 완탐(플로이드 와샬)으로 풀 수 있다.
    
    for k in range(n):                  # 1. 모든 노드를 중간점(경로)로 가정하며
        for i in range(n):              # 2. 점수판을 순회
            for j in range(n):          # 3. 만약 i가 k에 이겼고, k가 j에 이겼다면 
                if rank[i][j] == 0:     # i는 j에게도 이김 (지는 것도 동일)
                    if rank[i][k] == 1 and rank[k][j] == 1:
                        rank[i][j] = 1
                    elif rank[i][k] == -1 and rank[k][j] == -1:
                        rank[i][j] = -1
    ans = 0
    for i in range(n):
        if Counter(rank[i])[0] == 1:
            ans += 1

    return ans

