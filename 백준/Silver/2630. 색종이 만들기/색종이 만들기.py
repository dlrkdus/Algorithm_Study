import sys
sys.setrecursionlimit(100000)
N = int(input())

arr =[list(map(int,input().split())) for i in range(N)]

blue = 0
white = 0

def divide(i,j,N):
    global blue
    global white
    check = arr[i][j]

    for x in range(i,i+N):
        for y in range(j,j+N):
            if arr[x][y]!=check:
                N//=2
                divide(i,j,N)
                divide(i,j+N,N)
                divide(i+N,j,N)
                divide(i+N,j+N,N)
                return 
    if check ==0:
        white+=1
    else:
        blue+=1

divide(0,0,N)

print(white)
print(blue)


