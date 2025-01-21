from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int,input().split())
    board[x-1][y-1] = 1

L = int(input())
rotations = []
for _ in range(L):
    X, C = input().split()
    rotations.append([int(X), C])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

time = 0
x, y = 0,0
d = 0
board[x][y] = 2
snake = deque()
snake.append([x,y])
rotation_idx = 0

while True:
    # 전진
    nx = x + dx[d]
    ny = y + dy[d]
    time +=1
    # 충돌 검사
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        break
    # 사과가 없다면 꼬리 줄어듦
    if board[nx][ny] != 1:
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    snake.append([nx,ny]) # 머리는 무조건 큐에 넣어준다.
    board[nx][ny] = 2
    x, y = nx, ny

    if rotation_idx < L and time == rotations[rotation_idx][0]:
        if rotations[rotation_idx][1] == "D":
            d = (d+1)%4
        else:
            d = (d-1)%4
        rotation_idx +=1

print(time)
