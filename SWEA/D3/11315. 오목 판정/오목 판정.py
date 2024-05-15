
T = int(input())

def check(i,j,n):
    global count
    global result
    if count >= 5:
        result = "YES"
    new_x = i+nx[n]
    new_y = j+ny[n]
    if 0<=new_x<N and 0<=new_y<N and arr[new_x][new_y]=='o':
        count+=1
        check(new_x, new_y,n)
    else:
        return

    #대각선 체크 


for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        x = list(input().strip())  # 입력을 문자열로 받아 리스트로 변환
        arr.append(x)
    result = "NO"
    nx = [1,-1,1,0,-1,0,1,-1]
    ny = [1,-1,0,1,0,-1,-1,1]
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='o':
                for n in range(8):
                    count=1
                    check(i,j,n)
            if result =="YES":
                break
    print(f'#{test_case} {result}')


    