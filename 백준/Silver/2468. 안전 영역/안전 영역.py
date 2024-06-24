import copy
import sys
sys.setrecursionlimit(10000)
from collections import deque

N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
maxA = max(max(row) for row in a)
minA = min(min(row) for row in a)
max_area = 0
nx = [0,0,-1,1]
ny = [1,-1,0,0]

def bfs(i,j,height):
    d = deque()
    d.append([i,j])

    while(d):
        a,b = d.popleft()
        for x in range (4):
            new_x = a+nx[x]
            new_y = b+ny[x]
            if 0<=new_x<N and 0<=new_y<N:
                if arr[new_x][new_y]>height:
                    arr[new_x][new_y]=0
                    d.append([new_x,new_y])

for height in range(maxA+1):
    count=0
    arr = copy.deepcopy(a)
    for i in range(N):
        for j in range(N):
            if  arr[i][j]>height:
                bfs(i,j,height)
                count+=1

    max_area = max(max_area,count)

print(max_area)
