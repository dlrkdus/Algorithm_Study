from collections import defaultdict

def solution(N, number):
    if N == number:
        return 1

    # defaultdict를 사용해 초기값을 자동으로 set()으로 설정
    dp = defaultdict(set)
    dp[1].add(N)  # N을 1번 사용한 경우

    # N을 몇 번 사용했는가
    for i in range(2, 9):
        num = int(str(N) * i)  # N을 i번 반복한 숫자
        dp[i].add(num)

        # 이전 값들로 새로운 값 생성
        for j in range(1, i):
		        # dp[j] = N을 j번 사용해서 나올 수 있는 경우
		        # dp[5] = 1,4 / 2,3 / 3,2/ 4,1의 조합을 모두 구한다. 
            for v1 in dp[j]:
                for v2 in dp[i - j]:
                    dp[i].add(v1 + v2)
                    dp[i].add(v1 - v2)
                    dp[i].add(v1 * v2)
                    if v2 != 0:  # 0으로 나누기 방지
                        dp[i].add(v1 // v2)

        # 원하는 숫자를 찾은 경우
        if number in dp[i]:
            return i

    return -1  # 8번 이하로 만들 수 없는 경우