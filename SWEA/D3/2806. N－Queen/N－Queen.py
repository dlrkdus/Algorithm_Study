T=int(input())

def check(row):
    for i in range(row):
        # 같은 열에 위치한 퀸이 있으면 False
        if nq[row]==nq[i]:
            return False
        # 부호 반전 (열-열) = 행-행 이라면 같은 대각선 상에 있다.
        # (i+1,j+1), (i+1,j-1), (i-1,j+1), (i-1,j-1) 와 (i,j) 관계를 생각해보자.
        if abs(nq[row]-nq[i])==row-i:
            return False
    return True




def dfs(row):
    global count
    if row == N: #N번째 행까지 모든 퀸의 열 위치가 정해졌다면 1가지 경우이므로
        count+=1
    else:
        for col in range(N): #행별로 어느 열인지, 즉 nq[row]=col이면 row행 col 열에 퀸 위치
            nq[row]=col # 열 위치 지정 (퀸 두기)
            if check(row): # 다음 행에 퀸 둘 수 있는지 확인, True라면 계속 탐색, False라면 dfs 종료
                dfs(row+1)


    
for test_case in range(1,T+1):
    count =0
    N = int(input())
    nq = [0]* N #i번째 행의 퀸 열 위치, 행별로 떼서 생각한다.

    dfs(0)

    print(f"#{test_case}",count)
