from itertools import combinations
N = int(input())
arr = [list(map(str,input().split()))for _ in range(N)]
nothing = []
teachers = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "X":
            nothing.append([i,j])
        if arr[i][j] == "T":
            teachers.append([i,j])
            
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def can_not_see():
    for t in teachers:
        for i in range(4): # 상하좌우 한 방향씩 모두 탐색
            nx,ny = t[0],t[1]
            while True:
                nx +=dx[i]
                ny +=dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    break
                if arr[nx][ny] == "O":
                    break
                if arr[nx][ny] =="S":
                    return False
    return True


answer = "NO"
for comb in list(combinations(nothing,3)):
    for (x,y) in comb:
        arr[x][y] ="O"
    if can_not_see():
        answer = "YES"
        break
    for (x,y) in comb:
        arr[x][y] ="X"
    
print(answer)