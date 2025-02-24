from collections import defaultdict
# N을 i번 써서 만들 수 있는 경우를 딕셔너리에 담자.
# 숫자 N을 최소로 사용해서 number로 만들기
def solution(N, number):
    answer = -1
    dp = defaultdict(set)
    dp[1].add(N)
    if N == number:
        return 1
    for i in range(2,10):
        dp[i].add(int(str(N)*i)) # 55, 555,,
        for j in range(1, i): # 이전거랑 조합해야 함
            for v1 in dp[j]:
                for v2 in dp[i-j]:
                    dp[i].add(v1+v2)
                    dp[i].add(v1-v2)
                    dp[i].add(v1*v2)
                    if v2!=0:
                        dp[i].add(v1//v2)

    for i in range(1,10):
        if number in dp[i]:
            if i<=8:
                return i
    return answer
        

    