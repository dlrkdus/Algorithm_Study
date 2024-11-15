def solution(N, number):
    if N == number:
        return 1
    dp = {} # 딕셔너리로 선언
    dp.setdefault(1, set()).add(N) # value를 집합으로 선언
    for i in range(2,9):
        num = int(str(N) * i)
        dp.setdefault(i, set()).add(num)
        # 이전 값들로 새로운 값 생성
        for j in range(1, i):
            for v1 in dp[j]:
                for v2 in dp[i - j]:
                    dp[i].add(v1 + v2)
                    dp[i].add(v1 - v2)
                    dp[i].add(v1 * v2)
                    if v2 != 0:  # 0으로 나누기 방지
                        dp[i].add(v1 // v2)
    
        if number in dp[i]:
            return i
    return -1