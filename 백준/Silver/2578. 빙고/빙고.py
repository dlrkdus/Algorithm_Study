arr = [list(map(int,input().split())) for _ in range(5)]
nums = [list(map(int,input().split())) for _ in range(5)]
checked = [[0]*5 for _ in range(5)]

# 사회자가 부른 숫자 순서를 1차원 리스트로 펼치기
calls = sum(nums, [])

def count_bingo():
    bingo = 0
    # 가로 줄 체크
    for row in checked:
        if sum(row) == 5:
            bingo += 1
    # 세로 줄 체크
    for col in zip(*checked):
        if sum(col) == 5:
            bingo += 1
    # 대각선 
    if all(checked[i][i] for i in range(5)):
        bingo += 1
    # 대각선 
    if all(checked[i][4 - i] for i in range(5)):
        bingo += 1
    return bingo

for count, num in enumerate(calls, start=1):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                checked[i][j] = 1
                break

    if count_bingo() >= 3:
        print(count)
        break