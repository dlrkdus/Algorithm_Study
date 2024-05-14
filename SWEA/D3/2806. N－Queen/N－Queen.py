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
            if check(row): #만약 해당 열에 놓을 수 있다면 다음 행의 열 위치 탐색
                dfs(row+1) #만약 row 행의 모든 열에 False가 반환된다면 백트래킹으로 이전 dfs(이전 행)로 돌아가 다음 열을 탐색함
             
# 즉 행별로 모든 열을 탐색했는데 False라면 이전 행의 열에 놓을 수 없는 것이므로 백트래킹으로 돌아가 
# 이전 행의 다음 열을 탐색하는 것이다. 
# 그렇게 계속 돌아가다 초기의 dfs까지 종료되면 count 는 증가 없이 0이 되는 것. 

    
for test_case in range(1,T+1):
    count =0
    N = int(input())
    nq = [0]* N #i번째 행의 퀸 열 위치, 행별로 떼서 생각한다.

    dfs(0)
    print(f"#{test_case}",count)
