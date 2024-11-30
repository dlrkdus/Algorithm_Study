from collections import deque
def solution(maps):
    answer = []
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    maps = convert(maps)
    visited = [[0 for i in range(len(maps[0]))]for j in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                d = deque()
                d.append([i,j])
                count = int(maps[i][j])
                visited[i][j] = 1
                while d:
                    x, y =d.popleft()
                    for a in range(4):
                        new_x = x + nx[a]
                        new_y = y + ny[a]
                        if 0<=new_x<len(maps) and 0<=new_y<len(maps[0]) and maps[new_x][new_y] != "X" and not visited[new_x][new_y]:
                            visited[new_x][new_y] = 1
                            d.append([new_x,new_y])
                            count += int(maps[new_x][new_y])
                answer.append(count)
    if len(answer)==0:
        return [-1]
    return sorted(answer)


def convert(maps):
    return [list(row) for row in maps]