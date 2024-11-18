
# 약간 냅색 문제 st .. 
def solution(arr):
    n = len(arr)
    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]
    
    # 초기화: 숫자에 대해 최댓값과 최솟값은 동일
    for i in range(0, n, 2):  # 숫자 위치만
        dp_max[i][i] = int(arr[i])
        dp_min[i][i] = int(arr[i])
    
    for length in range(3,n+1,2): # 괄호의 길이
        for start in range(0,n-length+1,2): # 시작 범위
            end = start+length-1 # 끝 범위
            for d_idx in range(start+1,end,2): # 연산자 위치
                if arr[d_idx] == "+":
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][d_idx-1] + dp_max[d_idx+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][d_idx-1] + dp_min[d_idx+1][end])
                elif arr[d_idx] == "-":
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][d_idx-1] - dp_min[d_idx+1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][d_idx-1] - dp_max[d_idx+1][end])
                    
    
    return dp_max[0][n-1]